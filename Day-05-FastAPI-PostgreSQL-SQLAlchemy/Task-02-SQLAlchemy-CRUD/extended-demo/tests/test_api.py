import os
from pathlib import Path

# Ensure tests use an isolated SQLite database, not the developer's PostgreSQL DB.
os.environ["DATABASE_URL"] = "sqlite:///./test_pms.db"

from fastapi.testclient import TestClient
from app.database import Base, engine
from app.main import app

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
client = TestClient(app)

def setup_function():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

def test_user_task_crud_and_filter():
    user_response = client.post("/users", json={
        "name": "Test User", "email": "test@example.com", "phone": "9999999999"
    })
    assert user_response.status_code == 201
    user_id = user_response.json()["id"]

    task_response = client.post("/tasks", json={
        "title": "Test task", "description": "API test",
        "status": "pending", "user_id": user_id
    })
    assert task_response.status_code == 201
    task_id = task_response.json()["id"]

    filtered = client.get("/tasks?status=pending")
    assert filtered.status_code == 200
    assert any(task["id"] == task_id for task in filtered.json())

    detail = client.get(f"/users/{user_id}")
    assert detail.status_code == 200
    assert len(detail.json()["tasks"]) == 1

    updated = client.put(f"/tasks/{task_id}", json={"status": "done"})
    assert updated.status_code == 200
    assert updated.json()["status"] == "done"

def test_missing_user_and_invalid_status():
    assert client.get("/users/9999").status_code == 404
    assert client.post("/tasks", json={
        "title": "Bad task", "status": "blocked", "user_id": 1
    }).status_code == 422
