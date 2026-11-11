import os
from datetime import datetime, timedelta, timezone

os.environ["DATABASE_URL"] = "sqlite://"
os.environ["JWT_SECRET_KEY"] = "test-only-secret-key-with-at-least-32-bytes"

import jwt
import pytest
from fastapi.testclient import TestClient

from app.database import Base, SessionLocal, engine
from app.main import app
from app.models import AuthSession, User
from app.security import JWT_SECRET_KEY, hash_password


@pytest.fixture
def client():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    with SessionLocal() as db:
        db.add_all(
            [
                User(
                    name="Teacher User",
                    email="teacher@example.com",
                    password_hash=hash_password("teacher-pass-123"),
                    role="teacher",
                    is_active=True,
                ),
                User(
                    name="Student User",
                    email="student@example.com",
                    password_hash=hash_password("student-pass-123"),
                    role="student",
                    is_active=True,
                ),
                User(
                    name="Other Student",
                    email="other@example.com",
                    password_hash=hash_password("other-pass-123"),
                    role="student",
                    is_active=True,
                ),
            ]
        )
        db.commit()
    with TestClient(app) as test_client:
        yield test_client
    Base.metadata.drop_all(bind=engine)


def login(client: TestClient, email: str, password: str) -> dict:
    response = client.post(
        "/auth/login",
        json={"email": email, "password": password},
    )
    assert response.status_code == 200
    return response.json()


def use_token(client: TestClient, token: str) -> None:
    client.headers["Authorization"] = f"Bearer {token}"


def test_missing_and_invalid_authentication_returns_401(client: TestClient) -> None:
    assert client.get("/api/v3/tasks").status_code == 401
    assert client.get("/auth/me").status_code == 401
    response = client.post(
        "/auth/login",
        json={"email": "teacher@example.com", "password": "wrong-password"},
    )
    assert response.status_code == 401


def test_student_registration_hashes_password_and_rejects_role_injection(
    client: TestClient,
) -> None:
    payload = {
        "name": "New Student",
        "email": "new@example.com",
        "password": "new-student-pass",
        "role": "teacher",
    }
    response = client.post("/auth/register", json=payload)
    assert response.status_code == 422

    payload.pop("role")
    response = client.post("/auth/register", json=payload)
    assert response.status_code == 201
    assert response.json()["role"] == "student"
    assert "password_hash" not in response.json()
    with SessionLocal() as db:
        user = db.query(User).filter_by(email="new@example.com").one()
        assert user.password_hash != payload["password"]
        assert user.password_hash.startswith("$argon2")

    assert client.post("/auth/register", json=payload).status_code == 409


def test_teacher_task_workflow_and_student_permissions(client: TestClient) -> None:
    teacher = login(client, "teacher@example.com", "teacher-pass-123")
    use_token(client, teacher["access_token"])
    assert client.get("/api/v3/users/").status_code == 200
    student_id = next(
        user["id"]
        for user in client.get("/api/v3/users/").json()
        if user["email"] == "student@example.com"
    )
    created = client.post(
        "/api/v3/tasks",
        json={"title": "Complete exercise"},
    )
    assert created.status_code == 201
    task_id = created.json()["id"]
    assert created.json()["status"] == "pending"
    assignment = client.patch(
        f"/api/v3/tasks/{task_id}",
        json={"assigned_to": student_id},
    )
    assert assignment.status_code == 200
    other_task = client.post(
        "/api/v3/tasks",
        json={"title": "Private other-student task", "assigned_to": student_id + 1},
    )
    assert other_task.status_code == 201
    other_task_id = other_task.json()["id"]
    assert {
        task["id"] for task in client.get("/api/v3/tasks").json()
    } == {task_id, other_task_id}

    use_token(
        client,
        login(client, "student@example.com", "student-pass-123")["access_token"],
    )
    student_tasks = client.get("/api/v3/tasks")
    assert student_tasks.status_code == 200
    assert [task["id"] for task in student_tasks.json()] == [task_id]
    assert client.get(f"/api/v3/tasks/{other_task_id}").status_code == 404
    assert client.patch(
        f"/api/v3/tasks/{other_task_id}",
        json={"status": "done"},
    ).status_code == 404
    updated = client.patch(
        f"/api/v3/tasks/{task_id}",
        json={"status": "in progress", "work_notes": "Started the exercise."},
    )
    assert updated.status_code == 200, updated.text
    assert updated.json()["status"] == "in progress"
    assert updated.json()["work_notes"] == "Started the exercise."

    assert client.patch(
        f"/api/v3/tasks/{task_id}",
        json={"assigned_to": student_id + 1},
    ).status_code == 403
    assert client.delete(f"/api/v3/tasks/{task_id}").status_code == 403
    assert client.get("/api/v3/tasks/99999").status_code == 404
    assert client.get("/api/v3/users/").status_code == 403
    assert client.get("/api/v3/progress").status_code == 403
    assert client.get(f"/api/v3/users/{student_id + 1}").status_code == 404

    use_token(client, teacher["access_token"])
    progress = client.get("/api/v3/progress")
    assert progress.status_code == 200
    row = next(item for item in progress.json()["students"] if item["user_id"] == student_id)
    assert row["in_progress"] == 1
    assert client.patch(
        f"/api/v3/tasks/{task_id}",
        json={"title": "Reviewed exercise"},
    ).status_code == 200
    assert client.delete(f"/api/v3/tasks/{task_id}").status_code == 204
    assert client.get(f"/api/v3/tasks/{task_id}").status_code == 404
    assert client.delete(f"/api/v3/tasks/{other_task_id}").status_code == 204


def test_refresh_rotates_tokens_and_logout_revokes_the_session(
    client: TestClient,
) -> None:
    tokens = login(client, "student@example.com", "student-pass-123")
    refreshed = client.post(
        "/auth/refresh",
        json={"refresh_token": tokens["refresh_token"]},
    )
    assert refreshed.status_code == 200
    next_tokens = refreshed.json()
    assert next_tokens["refresh_token"] != tokens["refresh_token"]
    assert client.post(
        "/auth/refresh",
        json={"refresh_token": tokens["refresh_token"]},
    ).status_code == 401

    use_token(client, next_tokens["access_token"])
    assert client.post("/auth/logout").status_code == 204
    assert client.get("/auth/me").status_code == 401
    assert client.post(
        "/auth/refresh",
        json={"refresh_token": next_tokens["refresh_token"]},
    ).status_code == 401
    use_token(client, tokens["access_token"])
    assert client.get("/auth/me").status_code == 401


def test_expired_access_and_refresh_tokens_are_rejected(client: TestClient) -> None:
    tokens = login(client, "student@example.com", "student-pass-123")
    access_claims = jwt.decode(
        tokens["access_token"],
        JWT_SECRET_KEY,
        algorithms=["HS256"],
        options={"verify_exp": False},
    )
    expired_access = jwt.encode(
        {
            **access_claims,
            "exp": datetime.now(timezone.utc) - timedelta(minutes=1),
        },
        JWT_SECRET_KEY,
        algorithm="HS256",
    )
    use_token(client, expired_access)
    assert client.get("/auth/me").status_code == 401

    refresh_claims = jwt.decode(
        tokens["refresh_token"],
        JWT_SECRET_KEY,
        algorithms=["HS256"],
        options={"verify_exp": False},
    )
    expired_refresh = jwt.encode(
        {
            **refresh_claims,
            "exp": datetime.now(timezone.utc) - timedelta(minutes=1),
        },
        JWT_SECRET_KEY,
        algorithm="HS256",
    )
    assert client.post(
        "/auth/refresh",
        json={"refresh_token": expired_refresh},
    ).status_code == 401


def test_expired_database_session_and_invalid_task_input(client: TestClient) -> None:
    tokens = login(client, "teacher@example.com", "teacher-pass-123")
    session_id = jwt.decode(
        tokens["access_token"],
        JWT_SECRET_KEY,
        algorithms=["HS256"],
    )["sid"]
    with SessionLocal() as db:
        auth_session = db.get(AuthSession, session_id)
        assert auth_session is not None
        auth_session.expires_at = datetime.now(timezone.utc) - timedelta(minutes=1)
        db.commit()

    use_token(client, tokens["access_token"])
    assert client.get("/auth/me").status_code == 401
    tokens = login(client, "teacher@example.com", "teacher-pass-123")
    use_token(client, tokens["access_token"])
    assert client.post("/api/v3/tasks", json={"title": ""}).status_code == 422
    assert client.get("/api/v3/tasks/99999").status_code == 404


def test_student_can_only_read_own_profile(client: TestClient) -> None:
    student = login(client, "student@example.com", "student-pass-123")
    use_token(client, student["access_token"])
    assert client.get("/auth/me").json()["role"] == "student"
    assert client.get("/api/v3/users/2").status_code == 200
    assert client.get("/api/v3/users/3").status_code == 404


def test_task_list_pagination_search_and_filters(client: TestClient) -> None:
    teacher = login(client, "teacher@example.com", "teacher-pass-123")
    use_token(client, teacher["access_token"])
    users = client.get("/api/v3/users/").json()
    student_id = next(
        user["id"] for user in users if user["email"] == "student@example.com"
    )
    other_student_id = next(
        user["id"] for user in users if user["email"] == "other@example.com"
    )
    tasks = [
        {"title": "Math homework", "assigned_to": student_id},
        {"title": "Science essay", "assigned_to": student_id},
        {"title": "History research", "assigned_to": other_student_id},
        {"title": "Math quiz"},
    ]
    task_ids = []
    for task in tasks:
        response = client.post("/api/v3/tasks", json=task)
        assert response.status_code == 201
        task_ids.append(response.json()["id"])
    assert client.patch(
        f"/api/v3/tasks/{task_ids[1]}",
        json={"status": "done"},
    ).status_code == 200
    assert client.patch(
        f"/api/v3/tasks/{task_ids[3]}",
        json={"status": "in progress"},
    ).status_code == 200

    first_page = client.get("/api/v3/tasks", params={"page": 1, "limit": 2})
    second_page = client.get("/api/v3/tasks", params={"page": 2, "limit": 2})
    assert [task["id"] for task in first_page.json()] == task_ids[:2]
    assert [task["id"] for task in second_page.json()] == task_ids[2:]
    assert client.get(
        "/api/v3/tasks",
        params={"page": 3, "limit": 2},
    ).json() == []

    assert {
        task["id"]
        for task in client.get("/api/v3/tasks", params={"search": "mAtH"}).json()
    } == {task_ids[0], task_ids[3]}
    assert [
        task["id"]
        for task in client.get("/api/v3/tasks", params={"status": "done"}).json()
    ] == [task_ids[1]]
    assert {
        task["id"]
        for task in client.get(
            "/api/v3/tasks",
            params={"assigned_to": student_id},
        ).json()
    } == {task_ids[0], task_ids[1]}
    filtered = client.get(
        "/api/v3/tasks",
        params={
            "search": "math",
            "status": "pending",
            "assigned_to": student_id,
        },
    )
    assert [task["id"] for task in filtered.json()] == [task_ids[0]]

    use_token(
        client,
        login(client, "student@example.com", "student-pass-123")["access_token"],
    )
    assert {
        task["id"] for task in client.get("/api/v3/tasks").json()
    } == {task_ids[0], task_ids[1]}
    assert client.get(
        "/api/v3/tasks",
        params={"assigned_to": other_student_id},
    ).json() == []

    for params in (
        {"page": 0},
        {"limit": 101},
        {"status": "invalid"},
        {"assigned_to": 0},
        {"search": ""},
    ):
        assert client.get("/api/v3/tasks", params=params).status_code == 422


def test_seed_command_creates_accounts_without_replacing_existing_users(
    client: TestClient,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from app.seed import main as seed_main

    monkeypatch.setenv("SEED_TEACHER_EMAIL", "seed-teacher@example.com")
    monkeypatch.setenv("SEED_TEACHER_PASSWORD", "private-test-teacher")
    monkeypatch.setenv("SEED_STUDENT_EMAIL", "seed-student@example.com")
    monkeypatch.setenv("SEED_STUDENT_PASSWORD", "private-test-student")
    seed_main()
    seed_main()

    with SessionLocal() as db:
        teacher = db.query(User).filter_by(email="seed-teacher@example.com").one()
        student = db.query(User).filter_by(email="seed-student@example.com").one()
        assert teacher.role == "teacher"
        assert student.role == "student"
        assert teacher.password_hash != "private-test-teacher"
        assert student.password_hash != "private-test-student"
