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
├── alembic.ini
├── alembic/
│   ├── env.py
│   └── versions/
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

## Database migrations

Database migrations version schema changes so development, test, and production databases can be updated consistently and rolled back when needed, instead of relying on table creation at API startup. Alembic autogenerates migration candidates from the SQLAlchemy models, which must be reviewed before applying. The initial revision creates `users`, `tasks`, and `sessions`; the next revision adds the `work_notes` task column.

Run these commands from this project directory after configuring `.env` and installing `requirements.txt`:

```powershell
# Create a new migration after changing app/models.py
alembic revision --autogenerate -m "describe the schema change"

# Review the generated file in alembic/versions before applying it
alembic upgrade head

# Roll back the most recently applied revision
alembic downgrade -1

# Re-apply the latest revision
alembic upgrade head
```

For a fresh database, apply the checked-in migrations before starting the API or running the seed command. If upgrading a database created by an earlier version of this project, back it up and compare its schema with the revision before using `alembic stamp`; stamping records a revision without applying schema changes and is only safe when the database already matches that revision. Do not run the initial create-tables revision against a database that already contains these tables.

## Deploy on Render

The repository-root `render.yaml` defines a free Python web service and a Render PostgreSQL database. In Render, create a new Blueprint from this repository and select the `main` branch. Review the services before applying the Blueprint.

The Blueprint generates `JWT_SECRET_KEY` and connects the service to its database. When prompted, set these four private variables in Render (do not put their values in Git or this README):

- `SEED_TEACHER_EMAIL`
- `SEED_TEACHER_PASSWORD`
- `SEED_STUDENT_EMAIL`
- `SEED_STUDENT_PASSWORD`

The start command applies `alembic upgrade head`, runs the idempotent seed command, and then starts Uvicorn on Render's `$PORT`. This runs on each service start because Render's pre-deploy command is not available on the free web-service plan; completed migrations and existing seed accounts are left unchanged.

The live API is available at `https://demoapi-task-manager.onrender.com`. Open its `/docs` page for the interactive API documentation or `/health` for the health check.

Render's free web service spins down after 15 minutes without traffic and can take about a minute to wake up. Its free PostgreSQL database expires 30 days after creation; export or migrate the data before then if you need to keep it. See [Render's free plan limitations](https://render.com/docs/free).

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
| GET | `/api/v3/tasks` | Paginated, searchable, filterable tasks (role-scoped) |
| GET | `/api/v3/tasks/{task_id}` | Get a task (teacher or assigned student) |
| PATCH | `/api/v3/tasks/{task_id}` | Teacher edits task; student edits own status/notes |
| DELETE | `/api/v3/tasks/{task_id}` | Delete a task (teacher only) |
| GET | `/api/v3/progress` | Per-student status counts (teacher only) |

Task statuses are `pending`, `in progress`, and `done`. Students may only change their own task status and work notes; the API returns 404 for another student's task. A logged-in student attempting a teacher-only action receives **403 Forbidden**. Missing/invalid authentication receives **401 Unauthorized**. Legacy unauthenticated user create/update/delete routes have been removed; registration is through `/auth/register`.

### Task list pagination, search, and filters

`GET /api/v3/tasks` accepts these optional query parameters:

| Parameter | Default | Description |
|---|---:|---|
| `page` | `1` | 1-based page number (minimum `1`) |
| `limit` | `20` | Page size (between `1` and `100`) |
| `search` | — | Case-insensitive substring match against the task title |
| `status` | — | Filter by `pending`, `in progress`, or `done` |
| `assigned_to` | — | Filter by a positive user ID |

For example, `GET /api/v3/tasks?page=1&limit=10&search=math&status=pending&assigned_to=2`
combines pagination, title search, and both filters. The response remains a JSON
array of task objects. Students always see only their own assigned tasks, even
when query filters are supplied; teachers can list and filter all tasks.
Invalid page sizes, status values, and user IDs return **422 Unprocessable
Entity**.

## Postman
Import `../../postman/DemoAPI-Task-Manager-Auth.postman_collection.json` and create a private environment with `base_url`, `teacher_email`, `teacher_password`, `student_email`, and `student_password`. Leave credentials out of exported/committed collection files. The collection includes task-list requests for pagination, case-insensitive title search, status, and assignee filters. Also try a filtered request as a student to confirm that results remain restricted to that student's assignments.

Run the requests in collection order to test teacher/student login, task assignment and progress, student status/notes updates, refresh-token rotation, forbidden assignment/deletion, invalid login, invalid input, a missing record, missing token, and revoked token. For the expired JWT request, set `ACCESS_TOKEN_MINUTES=1`, restart the API, log in, wait one minute, and send the request. The expired-session request is a separate manual step: first expire a test account's database session in PostgreSQL, then send that request:

```sql
UPDATE sessions
SET expires_at = NOW() - INTERVAL '1 minute'
WHERE user_id = <test_user_id> AND revoked_at IS NULL;
```

Invalid request payloads return 422, duplicate registration returns 409, and unknown records return 404.

## Running the pytest suite

From this directory, install the project dependencies and run the test suite:

```powershell
python -m pip install -r requirements.txt
python -m pytest -q
```

The tests use an isolated in-memory SQLite database and FastAPI's `TestClient`,
so they do not need a running PostgreSQL server. They cover login and student
registration, teacher/student permissions, 401/403 responses, expired and
revoked tokens, task creation/assignment/update/deletion, and task-list
pagination/search/filters.

**Continuous integration (CI)** automatically checks code changes so teams get
consistent feedback and can catch regressions before merging. The GitHub
Actions workflow checks out the repository, sets up Python 3.12, installs this
task's requirements, and runs `python -m pytest -q` on every push and pull
request. A failed test makes the workflow fail; a passing run is visible in the
repository's **Actions** tab.

## Authorization matrix

| Action | Teacher | Student |
|---|---:|---:|
| Create, assign, update, and delete tasks | Yes | No |
| View all tasks/users and progress | Yes | No |
| View own assigned tasks/profile | Yes | Yes |
| Update own task status/work notes | Yes | Yes |
| Change another student's task | Teacher only | No |
