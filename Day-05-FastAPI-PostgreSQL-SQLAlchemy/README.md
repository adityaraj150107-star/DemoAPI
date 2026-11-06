# Day 05 — FastAPI, PostgreSQL & SQLAlchemy

Today's work is divided into the two tasks assigned:

- **Task 1 — PostgreSQL:** database setup, table creation, sample data, and SQL CRUD/query practice.
- **Task 2 — SQLAlchemy CRUD API:** a FastAPI V3 application using SQLAlchemy ORM with PostgreSQL.

## Folder structure

```text
Day-05-FastAPI-PostgreSQL-SQLAlchemy/
├── Task-01-PostgreSQL/
│   ├── README.md
│   └── users_queries.sql
└── Task-02-SQLAlchemy-CRUD/
    ├── README.md
    ├── requirements.txt
    ├── .env.example
    └── app/
        ├── __init__.py
        ├── main.py
        ├── database.py
        ├── models.py
        ├── schemas.py
        └── crud.py
```

---

## Task 1 — PostgreSQL

1. Install PostgreSQL and open pgAdmin or SQL Shell (psql).
2. Create a database named `demoapi_day5`.
3. Open and execute `Task-01-PostgreSQL/users_queries.sql`.
4. Run the SELECT queries to verify the inserted records.

See [Task 1 instructions](Task-01-PostgreSQL/README.md).

## Task 2 — SQLAlchemy CRUD with FastAPI

### 1. Open the task folder

Run these commands from the repository root:

```powershell
cd Day-05-FastAPI-PostgreSQL-SQLAlchemy/Task-02-SQLAlchemy-CRUD
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. Configure PostgreSQL

Create the database `demoapi_day5` in pgAdmin, then copy `.env.example` to `.env` and update the username/password for your local PostgreSQL installation.

Example URL:

```text
postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/demoapi_day5
```

Never commit your real database password.

### 3. Start the API

```powershell
uvicorn app.main:app --reload
```

Open Swagger UI: http://127.0.0.1:8000/docs

### 4. V3 endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | Health check |
| POST | `/api/v3/users/` | Create a user |
| GET | `/api/v3/users/` | List users |
| GET | `/api/v3/users/{user_id}` | Get one user |
| PUT | `/api/v3/users/{user_id}` | Update a user |
| DELETE | `/api/v3/users/{user_id}` | Delete a user |

The SQLAlchemy app creates its `users` table automatically at startup. Use Swagger's **Try it out** to test each operation.

See [Task 2 instructions](Task-02-SQLAlchemy-CRUD/README.md).

## Important

- This Day 05 app is separate from the existing root V1/V2 in-memory learning APIs.
- V3 uses PostgreSQL through SQLAlchemy ORM.
- The database must be running before starting the API.
- Keep `.env` private; only commit `.env.example`.
