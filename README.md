# DemoAPI

A minimal FastAPI service with one endpoint: `GET /health`.

## Prerequisites

- Docker Desktop installed and running
- Docker Compose v2 (`docker compose`)

## Run with one command

Open PowerShell in this project directory and run:

```powershell
docker compose up --build
```

Keep the terminal open while the API is running.

## Test the API

- Method: `GET`
- URL: `http://localhost:8000/health`
- Expected status: `200 OK`
- Expected JSON:

```json
{
  "status": "ok"
}
```

You can test it in Postman or open the URL in a browser.

Interactive API docs: http://localhost:8000/docs

## Stop the API

Press `Ctrl+C`, then run:

```powershell
docker compose down
```

## Project structure

```text
DemoAPI/
├── app/
│   └── main.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```
