# Task 2 — FastAPI Task Manager with PostgreSQL, JWT, and Roles

## Objective
Build a PostgreSQL-backed task manager with SQLAlchemy, JWT access/refresh tokens, revocable login sessions, password hashing, and teacher/student authorization.

## Project structure
```text
Task-02-SQLAlchemy-CRUD/
├── app/
│   ├── auth.py
│   ├── database.py
│   ├── dependencies.py
│   ├── main.py
│   ├── migrations.py
│   ├── models.py
│   ├── schemas.py
│   ├── security.py
│   ├── seed.py
│   ├── tasks.py
│   └── users.py
├── .env.example
├── requirements.txt
└── tests/
```

## Prerequisites
- Python 3.10 or newer
- PostgreSQL 14 or newer (local PostgreSQL or hosted PostgreSQL such as Supabase)
- Database `demoapi_day5` created using pgAdmin or psql

## Installation and database setup — Windows PowerShell
Run from this folder:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

Create the `demoapi_day5` database in PostgreSQL (or create a Supabase project and use its PostgreSQL connection string). Edit `.env`:

```env
DATABASE_URL=postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/demoapi_day5
JWT_SECRET_KEY=<at-least-32-random-bytes>
ACCESS_TOKEN_MINUTES=15
REFRESH_TOKEN_DAYS=7
```

For Supabase, set `DATABASE_URL` to the project's PostgreSQL URI, using the `postgresql+psycopg://` driver prefix and the connection details from Supabase. Use the SSL settings required by your provider. Generate a strong private JWT key locally with:

```powershell
python -c "import secrets; print(secrets.token_urlsafe(48))"
```

Never commit `.env`, real database credentials, seed passwords, or JWT secrets. `.env.example` contains placeholders only.

The API creates missing tables at startup. It also adds `password_hash` and `role` columns to a pre-existing Day 05 `users` table. Existing accounts receive an unusable password marker and student role; those accounts cannot log in until recreated/reset through a controlled process.

## Seed accounts
Public registration always creates a student, so it cannot be used to grant teacher privileges. Set private seed values in `.env` or the current PowerShell session, then run:

```powershell
$env:SEED_TEACHER_EMAIL = "teacher@example.com"
$env:SEED_TEACHER_PASSWORD = "<private-password-at-least-8-characters>"
$env:SEED_STUDENT_EMAIL = "student@example.com"
$env:SEED_STUDENT_PASSWORD = "<private-password-at-least-8-characters>"
python -m app.seed
```

The seed command creates the teacher and student only when absent and never prints or stores their plain-text passwords. Keep actual credentials in a private password manager/Postman environment, not this repository.

## Start the API
```powershell
uvicorn app.main:app --reload
```

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
- Health: http://127.0.0.1:8000/health

## Authentication and session flow
1. `POST /auth/register` creates a student; passwords are Argon2-hashed and never returned.
2. `POST /auth/login` verifies credentials and returns a short-lived access token and a refresh token. Store both securely; send the access token as `Authorization: Bearer <access_token>`.
3. Protected requests validate the JWT and its database session. Expired, revoked, inactive-user, malformed, and wrong-type tokens receive **401 Unauthorized**.
4. `POST /auth/refresh` accepts `{"refresh_token":"..."}`. A successful refresh rotates the refresh token; the old token can no longer be reused.
5. `POST /auth/logout` requires the access token and revokes that token's session. Further use of either token from that session is rejected.
6. `GET /auth/me` returns the authenticated user's safe profile.

The access token defaults to 15 minutes; the refresh session defaults to 7 days. Configure `ACCESS_TOKEN_MINUTES` and `REFRESH_TOKEN_DAYS` in `.env`.

## Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | Health check (public) |
| POST | `/auth/register` | Register a student |
| POST | `/auth/login` | Login and create a session |
| POST | `/auth/refresh` | Rotate refresh token and issue new access token |
| POST | `/auth/logout` | Revoke the current session |
| GET | `/auth/me` | Current user's profile |
| GET | `/api/v3/users/` | List users (teacher only) |
| GET | `/api/v3/users/{user_id}` | Get a profile (teacher or that user) |
| POST | `/api/v3/tasks` | Create/optionally assign a task (teacher only) |
| GET | `/api/v3/tasks` | All tasks for teachers; assigned tasks for students |
| GET | `/api/v3/tasks/{task_id}` | Get a task (teacher or assigned student) |
| PATCH | `/api/v3/tasks/{task_id}` | Teacher edits task; student edits own status/notes |
| DELETE | `/api/v3/tasks/{task_id}` | Delete a task (teacher only) |
| GET | `/api/v3/progress` | Per-student status counts (teacher only) |

Task statuses are `pending`, `in progress`, and `done`. Students may only change their own task status and work notes; the API returns 404 for another student's task. A logged-in student attempting a teacher-only action receives **403 Forbidden**. Missing/invalid authentication receives **401 Unauthorized**. Legacy unauthenticated user create/update/delete routes have been removed; registration is through `/auth/register`.

## Postman
Import `../../postman/DemoAPI-Task-Manager-Auth.postman_collection.json` and create a private environment with `base_url`, `teacher_email`, `teacher_password`, `student_email`, and `student_password`. Leave credentials out of exported/committed collection files.

Run the requests in collection order to test teacher/student login, task assignment and progress, student status/notes updates, refresh-token rotation, forbidden assignment/deletion, invalid login, invalid input, a missing record, missing token, and revoked token. For the expired JWT request, set `ACCESS_TOKEN_MINUTES=1`, restart the API, log in, wait one minute, and send the request. The expired-session request is a separate manual step: first expire a test account's database session in PostgreSQL, then send that request:

```sql
UPDATE sessions
SET expires_at = NOW() - INTERVAL '1 minute'
WHERE user_id = <test_user_id> AND revoked_at IS NULL;
```

Invalid request payloads return 422, duplicate registration returns 409, and unknown records return 404. Automated API tests run with `python -m pytest`.

## Authorization matrix

| Action | Teacher | Student |
|---|---:|---:|
| Create, assign, update, and delete tasks | Yes | No |
| View all tasks/users and progress | Yes | No |
| View own assigned tasks/profile | Yes | Yes |
| Update own task status/work notes | Yes | Yes |
| Change another student's task | Teacher only | No |
