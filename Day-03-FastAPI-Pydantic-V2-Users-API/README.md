# Day 03 — FastAPI Users CRUD Operations

## Objective

Build a basic Users REST API with FastAPI and understand the four CRUD operations, HTTP methods, path parameters, request bodies, status codes, and error handling.

**Storage for this learning task:** Python in-memory dictionary. Data resets when the application restarts. PostgreSQL and SQLAlchemy are covered separately in Day 05.

## Project files

The Day 03 implementation is part of the main application:

```text
DemoAPI/
├── app/
│   ├── main.py
│   └── api/
│       └── v1/
│           └── endpoints/
│               └── users.py
└── Day-03-FastAPI-Pydantic-V2-Users-API/
    └── README.md
```

- `app/main.py` — creates the FastAPI app and registers the versioned routers.
- `app/api/v1/endpoints/users.py` — Day 03 CRUD implementation.
- `app/api/v2/endpoints/users.py` — separate V2 validation exercise; not required to complete this Day 03 task.

## Setup and run (Windows PowerShell)

Run commands from the repository root:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open Swagger UI: http://127.0.0.1:8000/docs

## API endpoints

All Day 03 routes use the `/api/v1` prefix.

| Operation | Method | Endpoint | Success |
|---|---|---|---|
| Create user | POST | `/api/v1/users` | 201 Created |
| Get all users | GET | `/api/v1/all_users` | 200 OK |
| Get user by ID | GET | `/api/v1/fetch/user/{user_id}` | 200 OK |
| Update user | PUT | `/api/v1/user/{user_id}` | 200 OK |
| Delete user | DELETE | `/api/v1/user/{user_id}` | 200 OK |

## Test the API in Swagger UI

### 1. Create a user — POST /api/v1/users

Request body:

```json
{
  "name": "Aditya Raj",
  "email": "aditya@example.com",
  "phone": "9876543210",
  "status": "active"
}
```

Expected response (ID is assigned automatically):

```json
{
  "message": "User created successfully.",
  "data": {
    "id": 1,
    "name": "Aditya Raj",
    "email": "aditya@example.com",
    "phone": "9876543210",
    "status": "active"
  }
}
```

### 2. Get all users — GET /api/v1/all_users

Returns the total number of users and the list of user records.

### 3. Get one user — GET /api/v1/fetch/user/1

Returns the matching user. An unknown ID returns HTTP 404.

### 4. Update a user — PUT /api/v1/user/1

PUT replaces the user's complete editable record. Send all required fields:

```json
{
  "name": "Aditya Rajput",
  "email": "aditya.rajput@example.com",
  "phone": "9876543210",
  "status": "active"
}
```

### 5. Delete a user — DELETE /api/v1/user/1

Deletes the matching record. An unknown ID returns HTTP 404.

## Validation and error handling

The V1 learning endpoint checks:

- Name and email are required when creating or replacing a user.
- Name must contain 2–100 characters.
- Email must have a basic valid email format.
- Phone is optional; when supplied it must contain 7–20 characters.
- Status must be `active` or `inactive`.
- Extra/unrecognized fields are rejected.
- Duplicate email returns HTTP 409.
- Missing user ID returns HTTP 404.
- Invalid request data returns HTTP 422.

FastAPI also validates the path parameter `user_id` as an integer.

## CRUD concepts covered

| CRUD | HTTP method | Meaning |
|---|---|---|
| Create | POST | Add a new record |
| Read | GET | Retrieve one or many records |
| Update | PUT | Replace an existing record |
| Delete | DELETE | Remove a record |

## Important notes

- This is a learning implementation using in-memory storage, not a production database.
- Restarting Uvicorn clears the Day 03 user records.
- Day 03 focuses on the CRUD and HTTP workflow. Pydantic V2 request/response models are handled in the separate V2 learning work.
- PostgreSQL and SQLAlchemy ORM integration are handled in Day 05.
- Test the endpoints in Swagger UI and capture your own successful request/response screenshots before submitting.

**Verification:** Code and documentation are organized in the repository. Run the steps above locally to verify against your PostgreSQL-independent development environment.
