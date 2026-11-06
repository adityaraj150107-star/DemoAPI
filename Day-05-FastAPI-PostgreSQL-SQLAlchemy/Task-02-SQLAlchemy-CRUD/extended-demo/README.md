# DemoAI v3 — Day 5: PostgreSQL + FastAPI SQLAlchemy CRUD

This project covers the two Day 5 tasks for the PMS Portal:

- **Task 1 — PostgreSQL:** relational `users` and `tasks` tables, primary keys, foreign key, constraints and indexes.
- **Task 2 — SQLAlchemy CRUD:** working FastAPI endpoints for users and tasks, task assignment, task-status filtering, and a user's details with all tasks.

## Tech stack

- Python 3.11+ (recommended: Python 3.12)
- FastAPI
- SQLAlchemy 2.x
- PostgreSQL 15+ with psycopg 3
- Pydantic 2
- SQLite fallback is supported

## Project structure

```text
DemoAI-v3/
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
├── postman/
│   └── DemoAI-v3.postman_collection.json
├── sql/
│   └── task1_postgresql.sql
├── tests/
│   └── test_api.py
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

## 1. Create PostgreSQL database

Install PostgreSQL, then create a database named `pms_portal`:

```sql
CREATE DATABASE pms_portal;
```

The FastAPI app creates its tables automatically on startup. You can also run `sql/task1_postgresql.sql` in pgAdmin or `psql` to complete Task 1 separately.

Set the connection string in your terminal before starting the app:

**Windows PowerShell**
```powershell
$env:DATABASE_URL="postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/pms_portal"
```

**macOS/Linux**
```bash
export DATABASE_URL="postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/pms_portal"
```

Replace `YOUR_PASSWORD` with your PostgreSQL password.

## 2. SQLite fallback (if PostgreSQL installation fails)

No database server is needed. Set:

**Windows PowerShell**
```powershell
$env:DATABASE_URL="sqlite:///./pms.db"
```

**macOS/Linux**
```bash
export DATABASE_URL="sqlite:///./pms.db"
```

The same API and CRUD operations work with SQLite. Mention to your instructor that SQLite was used as the fallback.

## 3. Install and run

```bash
python -m venv .venv
```

Activate the environment:

**Windows**
```powershell
.venv\Scripts\Activate.ps1
```

**macOS/Linux**
```bash
source .venv/bin/activate
```

Install dependencies and start the server:

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
- Health check: http://127.0.0.1:8000/

## 4. API endpoints

### Users

| Method | Endpoint | Description |
|---|---|---|
| POST | `/users` | Create user |
| GET | `/users` | List users |
| GET | `/users/{user_id}` | User details including all tasks |
| PUT | `/users/{user_id}` | Update user |
| DELETE | `/users/{user_id}` | Delete user |

### Tasks

| Method | Endpoint | Description |
|---|---|---|
| POST | `/tasks` | Create task and assign to user |
| GET | `/tasks` | List tasks |
| GET | `/tasks?status=pending` | Filter by task status |
| GET | `/tasks?user_id=1` | Filter by assigned user |
| GET | `/tasks/{task_id}` | Get one task |
| PUT | `/tasks/{task_id}` | Update task / reassign task |
| DELETE | `/tasks/{task_id}` | Delete task |

Allowed task statuses: `pending`, `in progress`, `done`.

User statuses: `active`, `inactive`.

## 5. Example requests

Create a user (`POST /users`):
```json
{
  "name": "Aarav Sharma",
  "email": "aarav@example.com",
  "phone": "9876543210",
  "status": "active"
}
```

Create a task assigned to user 1 (`POST /tasks`):
```json
{
  "title": "Build login API",
  "description": "Create and test the login endpoint",
  "status": "pending",
  "user_id": 1
}
```

Change task status (`PUT /tasks/1`):
```json
{
  "status": "in progress"
}
```

Get a user's details and tasks (`GET /users/1`).

## 6. Validation and error handling

- **422 Unprocessable Entity:** Pydantic validation errors, invalid email, missing required values, invalid status, invalid ID query values.
- **404 Not Found:** user/task does not exist, or task assignment references a missing user.
- **409 Conflict:** duplicate user email.
- **204 No Content:** successful deletes.

## 7. Test with Postman

Import `postman/DemoAI-v3.postman_collection.json` into Postman. Set collection variable `base_url` to `http://127.0.0.1:8000`, then run requests in order: create user, create task, list/filter tasks, get user with tasks, update, and delete.

You can also test through Swagger UI at `/docs`.

## 8. Run automated tests

The tests use an isolated SQLite database:

```bash
pytest -q
```

## 9. GitHub

From the project folder:

```bash
git init
git add .
git commit -m "Day 5: PostgreSQL schema and FastAPI SQLAlchemy CRUD"
git branch -M main
git remote add origin https://github.com/adityaraj150107-star/DemoAI.git
git push -u origin main
```

If the repository already has a remote, check it with `git remote -v` before adding another. Review the existing repository before pushing; do not overwrite existing work blindly.
