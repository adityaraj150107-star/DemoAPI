# Task 2 — FastAPI V3 + SQLAlchemy CRUD

## Objective
Build a REST API using FastAPI, SQLAlchemy ORM, and PostgreSQL. This task demonstrates database connection setup, ORM models, Pydantic schemas, and complete CRUD operations.

## Requirements
- Python 3.10+
- PostgreSQL server running
- Database: `demoapi_day5`

## Setup (Windows PowerShell)

Run from this folder:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

Edit `.env` and set your own PostgreSQL password. Example:

```env
DATABASE_URL=postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/demoapi_day5
```

Create the database in pgAdmin before starting the API. Do not include angle brackets in the actual password and do not commit `.env`.

## Run

```powershell
uvicorn app.main:app --reload
```

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
- Health: http://127.0.0.1:8000/health

## Test CRUD in Swagger

### Create user — POST /api/v3/users/

```json
{
  "name": "Aditya Raj",
  "email": "aditya@example.com",
  "age": 21,
  "is_active": true
}
```

### List users — GET /api/v3/users/

### Get user — GET /api/v3/users/1

### Update user — PUT /api/v3/users/1

```json
{
  "name": "Aditya Rajput",
  "email": "aditya@example.com",
  "age": 22,
  "is_active": true
}
```

### Delete user — DELETE /api/v3/users/1

A successful create returns HTTP 201, reads return HTTP 200, and a missing user returns HTTP 404. Duplicate email returns HTTP 409.

## Architecture

- `database.py`: SQLAlchemy engine, session factory, and dependency.
- `models.py`: SQLAlchemy User table mapping.
- `schemas.py`: Pydantic request and response models.
- `crud.py`: database CRUD functions.
- `main.py`: FastAPI application and V3 routes.

Tables are created automatically on startup for this learning task. For production projects, use Alembic migrations, stronger configuration/secrets management, authentication, and automated tests.
