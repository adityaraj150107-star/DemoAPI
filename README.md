# DemoAPI — Docker + FastAPI Users CRUD

A single FastAPI application combining the Docker health-check task and the Users CRUD task.

## Features

- `GET /health` health check
- Create, list, fetch, update and delete users
- Async route handlers
- JSON request/response bodies and HTTP status codes
- Dockerfile and Docker Compose support
- Postman collection included

## User fields

`name`, `email`, `phone`, `status`

> Note: This learning version uses in-memory storage. Users are lost when the application/container restarts. A database can be added as a next step.

## Run with Docker

Requirements: Docker Desktop running and Docker Compose v2.

```powershell
docker compose up --build
```

Open:
- Swagger UI: http://localhost:8000/docs
- Health check: http://localhost:8000/health

Stop with `Ctrl+C`, then:

```powershell
docker compose down
```

## API endpoints

Base URL: `http://localhost:8000`

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | Health check |
| POST | `/api/v1/users` | Create a user |
| GET | `/api/v1/all_users` | List all users |
| GET | `/api/v1/fetch/user/{user_id}` | Fetch one user |
| PUT | `/api/v1/user/{user_id}` | Update a user |
| DELETE | `/api/v1/user/{user_id}` | Delete a user |

### Example POST body

```json
{
  "name": "Aditya Raj",
  "email": "aditya@gmail.com",
  "phone": "9876543210",
  "status": "active"
}
```

## Postman

Import `postman/DemoAPI.postman_collection.json` into Postman. Run requests in this order:

1. Health check
2. Create user
3. Get all users
4. Get user by ID (newly created user has ID 1 after a fresh start)
5. Update user
6. Delete user

The collection uses `http://127.0.0.1:8000` as its base URL.

## Project structure

```text
DemoAPI/
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── endpoints/
│   │           └── users.py
│   └── main.py
├── FastAPI-endpoints/       # Original task files retained for reference
├── postman/
│   └── DemoAPI.postman_collection.json
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```
