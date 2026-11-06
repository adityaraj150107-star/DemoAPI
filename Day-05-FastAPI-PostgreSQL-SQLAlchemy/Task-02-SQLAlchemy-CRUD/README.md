# Task 2 — FastAPI V3 with SQLAlchemy CRUD

## Objective
Build a FastAPI application connected to PostgreSQL using SQLAlchemy ORM, with separated database configuration, ORM model, Pydantic schemas, CRUD functions, and API routes.

## Project structure
```text
Task-02-SQLAlchemy-CRUD/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── crud.py
├── .env.example
├── requirements.txt
└── README.md
```

## Prerequisites
- Python 3.10+
- PostgreSQL service running
- Database `demoapi_day5` created using pgAdmin or psql

## Setup — Windows PowerShell
Run from this folder:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

Edit the local `.env` file with your PostgreSQL username and password:

```env
DATABASE_URL=postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/demoapi_day5
```

Do not commit your real `.env` file or password.

## Start the API
```powershell
uvicorn app.main:app --reload
```

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
- Health: http://127.0.0.1:8000/health

## V3 endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | Health check |
| POST | `/api/v3/users/` | Create user |
| GET | `/api/v3/users/` | List users |
| GET | `/api/v3/users/{user_id}` | Retrieve user |
| PUT | `/api/v3/users/{user_id}` | Update user |
| DELETE | `/api/v3/users/{user_id}` | Delete user |

## Example create payload
```json
{
  "name": "Aditya Raj",
  "email": "aditya@example.com",
  "age": 21,
  "is_active": true
}
```

## Code responsibilities
- `database.py`: reads DATABASE_URL, creates engine and session factory, provides request-scoped sessions.
- `models.py`: SQLAlchemy User table mapping.
- `schemas.py`: Pydantic V2 create/update/response models.
- `crud.py`: database Create, Read, Update, Delete functions.
- `main.py`: FastAPI routes and HTTP error handling.

The SQLAlchemy model creates the table on application startup for this learning task. Task 1's SQL table definition is designed to match the model.

## Test checklist
- [ ] PostgreSQL service is running.
- [ ] Database `demoapi_day5` exists.
- [ ] Local `.env` has the correct DATABASE_URL.
- [ ] API starts without database errors.
- [ ] Create a user and verify HTTP 201.
- [ ] List and fetch users.
- [ ] Update a user.
- [ ] Delete a user.
- [ ] Verify duplicate email and unknown user errors.

For production systems, use Alembic migrations, stronger configuration/secrets management, authentication, and automated tests. This is an internship learning implementation.
