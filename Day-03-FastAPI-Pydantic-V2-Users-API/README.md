# Day 03 — FastAPI Users API with Pydantic V2

## Objective
Create validated request and response models for the Users master using Pydantic V2 and organize the API by version.

## Tasks
- [ ] Understand Pydantic V2 request and response models.
- [ ] Define required and optional user fields.
- [ ] Add sensible default values.
- [ ] Apply type checks and field constraints.
- [ ] Validate email and other user inputs.
- [ ] Provide clear validation error messages.
- [ ] Implement or review Users CRUD endpoints.
- [ ] Keep V1 and V2 endpoints organized separately.
- [ ] Verify endpoints through Swagger UI or Postman.

## Current application locations

- Models: `app/models/user.py`
- V1 endpoints: `app/api/v1/endpoints/users.py`
- V2 endpoints: `app/api/v2/endpoints/users.py`
- Application entry point: `app/main.py`

## V2 endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/api/v2/users/` | Create a user |
| GET | `/api/v2/users/` | List users |
| GET | `/api/v2/users/{user_id}` | Get a user |
| PUT | `/api/v2/users/{user_id}` | Replace a user |
| PATCH | `/api/v2/users/{user_id}` | Partially update a user |
| DELETE | `/api/v2/users/{user_id}` | Delete a user |

## Run locally

```powershell
uvicorn app.main:app --reload
```

Open Swagger UI at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Deliverables
- Pydantic V2 user schemas.
- Versioned Users API.
- Validation and CRUD endpoint examples.

## Notes
The current demo uses in-memory storage. Data resets when the app restarts; V1 and V2 do not share the same in-memory records.

**Status:** Documentation structure created. Run and verify the endpoints before marking implementation tasks complete.
