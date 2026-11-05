# Day 02 — Docker Development Environment

## Objective
Create and run a small FastAPI demo service inside a Docker container.

## Tasks
- [ ] Understand Docker images, containers, Dockerfile, and Docker Compose.
- [ ] Install and verify Docker Desktop.
- [ ] Create a FastAPI demo endpoint: `GET /health`.
- [ ] Return a JSON response: `{"status": "ok"}`.
- [ ] Create a Dockerfile.
- [ ] Configure Docker Compose.
- [ ] Build and start the service using Docker.
- [ ] Test the health endpoint using Postman.
- [ ] Capture the successful Postman response.

## Useful commands

```powershell
docker --version
docker compose version
docker compose up --build
docker compose down
```

## Expected health response

```json
{
  "status": "ok"
}
```

## Deliverables
- FastAPI demo API.
- Dockerfile and Docker Compose configuration.
- Successful container run.
- Postman health-check screenshot.

## Notes
The main application files are maintained in the repository root and `app/`. This folder records the work completed for this day.

**Status:** Documentation structure created. Verify each task locally before marking it complete.
