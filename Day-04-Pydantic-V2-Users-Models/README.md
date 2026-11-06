# Day 04 — Pydantic V2 Request & Response Models

## Objective
Create Pydantic V2 request and response models for a Users API with required fields, defaults, type checks, constraints, and clear validation errors.

## Project structure
```text
Day-04-Pydantic-V2-Users-Models/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   └── v2/endpoints/users.py
│   └── models/user.py
├── requirements.txt
└── README.md
```

## Setup and run — Windows PowerShell
Run from this folder:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Swagger UI: http://127.0.0.1:8000/docs

## Models covered
- `UserCreate`: validates new user data.
- `UserUpdate`: supports partial updates using `model_dump(exclude_unset=True)`.
- `UserResponse`: defines the API response shape.
- `UsersListResponse`: returns a collection and total count.
- `MessageResponse`: standard message response.

## V2 endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/api/v2/users/` | Create user |
| GET | `/api/v2/users/` | List users |
| GET | `/api/v2/users/{user_id}` | Get one user |
| PUT | `/api/v2/users/{user_id}` | Replace user |
| PATCH | `/api/v2/users/{user_id}` | Partially update user |
| DELETE | `/api/v2/users/{user_id}` | Delete user |

## Example request
```json
{
  "name": "Aditya Raj",
  "email": "aditya@example.com",
  "age": 21,
  "phone": "9876543210",
  "is_active": true
}
```

## Validation covered
- Name length constraints.
- Email format validation through `EmailStr`.
- Age boundaries.
- Optional phone field.
- Boolean default for `is_active`.
- Unknown request fields rejected through `extra="forbid"`.
- Duplicate email conflict and user-not-found responses.

## Important
This is a separate learning app using in-memory storage. Data resets when the application restarts. PostgreSQL and SQLAlchemy persistence are covered in Day 05.

Test both valid and invalid payloads in Swagger UI and capture your own screenshots before submission.
