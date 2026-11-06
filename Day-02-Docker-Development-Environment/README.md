# Day 02 — Docker Development Environment

## Objective
Build a small FastAPI health-check service, package it with Docker, and run it using Docker Compose.

## Project structure
```text
Day-02-Docker-Development-Environment/
├── app/
│   └── main.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## API
- Method: `GET`
- Endpoint: `/health`
- Expected JSON: `{"status": "ok"}`

## Run without Docker (Windows PowerShell)
Run from this folder:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --app-dir app --reload
```

Open http://127.0.0.1:8000/health and http://127.0.0.1:8000/docs.

## Run with Docker
Make sure Docker Desktop is running, then run from this folder:

```powershell
docker --version
docker compose version
docker compose up --build
```

Test http://localhost:8000/health using a browser or Postman.

Stop the container:

```powershell
docker compose down
```

## Concepts covered
- Image: a packaged application template.
- Container: a running instance of an image.
- Dockerfile: instructions used to build the image.
- Docker Compose: configuration for running the service.

## Submission checklist
- [ ] Docker Desktop installed and running.
- [ ] FastAPI health endpoint returns `{"status": "ok"}`.
- [ ] Docker image builds successfully.
- [ ] Container starts successfully with Docker Compose.
- [ ] Postman response screenshot captured.

Only mark checklist items complete after verifying them on your computer.
