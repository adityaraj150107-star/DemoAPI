# Day 04 — Pydantic V2 Request & Response Models

## Objective
Create Pydantic V2 request and response models for the Users master, including required fields, default values, type checks, constraints, and clear validation errors.

## Tasks
- [ ] Understand Pydantic V2 and BaseModel.
- [ ] Create a UserCreate request model.
- [ ] Create a UserUpdate model.
- [ ] Create a UserResponse model.
- [ ] Identify required and optional fields.
- [ ] Set suitable default values.
- [ ] Add type validation and field constraints.
- [ ] Validate email and other user inputs.
- [ ] Add clear validation error messages.
- [ ] Connect the schemas to FastAPI endpoints.
- [ ] Test valid and invalid request bodies in Swagger UI or Postman.

## Current application locations
- Pydantic models: `app/models/user.py`
- V1 Users endpoints: `app/api/v1/endpoints/users.py`
- V2 Users endpoints: `app/api/v2/endpoints/users.py`
- Application entry point: `app/main.py`

## Run locally

```powershell
uvicorn app.main:app --reload
```

Open Swagger UI at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## V2 Users endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/api/v2/users/` | Create a user |
| GET | `/api/v2/users/` | List users |
| GET | `/api/v2/users/{user_id}` | Get a user |
| PUT | `/api/v2/users/{user_id}` | Replace a user |
| PATCH | `/api/v2/users/{user_id}` | Partially update a user |
| DELETE | `/api/v2/users/{user_id}` | Delete a user |

## Deliverables
- Pydantic V2 request and response schemas.
- Required/optional fields and default values.
- Type checks, field constraints, and validation examples.
- Updated Users API integration.

## Notes
The current demo uses in-memory storage. Data resets when the app restarts; V1 and V2 do not share the same in-memory records. Add screenshots of successful and failed validation requests after testing.

**Status:** Task documentation created. Verify the implementation and tests before marking checklist items complete.
