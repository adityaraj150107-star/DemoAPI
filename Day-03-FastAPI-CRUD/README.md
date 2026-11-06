# Day 03 — FastAPI Users CRUD API

## Objective
Build a standalone FastAPI Users API and understand Create, Read, Update, and Delete operations, HTTP methods, request bodies, path parameters, status codes, and error handling.

## Folder structure
```text
Day-03-FastAPI-CRUD/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── api/
│       ├── __init__.py
│       └── v1/
│           ├── __init__.py
│           └── endpoints/
│               ├── __init__.py
│               └── users.py
├── requirements.txt
└── README.md
```

## Setup — Windows PowerShell
Run from this folder:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Swagger UI: http://127.0.0.1:8000/docs

## API endpoints

| Operation | Method | Endpoint |
|---|---|---|
| Create | POST | `/api/v1/users` |
| Read all | GET | `/api/v1/all_users` |
| Read one | GET | `/api/v1/fetch/user/{user_id}` |
| Update | PUT | `/api/v1/user/{user_id}` |
| Delete | DELETE | `/api/v1/user/{user_id}` |

## Create user example
```json
{
  "name": "Aditya Raj",
  "email": "aditya@example.com",
  "phone": "9876543210",
  "status": "active"
}
```

## Update user example
PUT replaces the complete editable record, so send all required fields.

```json
{
  "name": "Aditya Rajput",
  "email": "aditya.rajput@example.com",
  "phone": "9876543210",
  "status": "active"
}
```

## Validation and error handling
- Name and email are required for create and replace.
- Name length must be 2–100 characters.
- Email must have a basic valid format.
- Phone is optional; if provided, it must be 7–20 characters.
- Status must be `active` or `inactive`.
- Unknown fields are rejected.
- Duplicate email returns HTTP 409.
- Missing user returns HTTP 404.
- Invalid request data returns HTTP 422.

## Important
This Day 03 exercise uses temporary in-memory storage. Records reset when the server restarts. Pydantic V2 request/response models are covered in Day 04, and PostgreSQL with SQLAlchemy is covered in Day 05.

Test all five endpoints in Swagger UI and capture your own successful request/response screenshots before submission.
