# Day 03 — FastAPI CRUD Operations

## Objective
Understand and implement Create, Read, Update, and Delete (CRUD) operations for a Users API using FastAPI.

## Tasks
- [ ] Understand HTTP methods: GET, POST, PUT, and DELETE.
- [ ] Create an endpoint to add a user.
- [ ] Create an endpoint to retrieve users.
- [ ] Create an endpoint to retrieve a user by ID.
- [ ] Create an endpoint to update a user.
- [ ] Create an endpoint to delete a user.
- [ ] Understand path parameters and request bodies.
- [ ] Return suitable HTTP status codes and error responses.
- [ ] Try the endpoints using Swagger UI or Postman.

## Current application locations
- Application entry point: `app/main.py`
- V1 Users endpoints: `app/api/v1/endpoints/users.py`
- V2 Users endpoints: `app/api/v2/endpoints/users.py`

## Run locally

```powershell
uvicorn app.main:app --reload
```

Open Swagger UI at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## CRUD overview

| Operation | HTTP method | Purpose |
|---|---|---|
| Create | POST | Add a new user |
| Read | GET | Retrieve users |
| Update | PUT / PATCH | Update user information |
| Delete | DELETE | Remove a user |

## Deliverables
- FastAPI Users CRUD endpoints.
- Understanding of HTTP methods, path parameters, and request bodies.
- API requests demonstrated through Swagger UI or Postman.

## Notes
Add the actual work details, commands, and screenshots here. Mark checklist items complete only after you have performed and verified them.

**Status:** Task documentation organized; verify implementation locally.
