<div align="center">

# 🚀 DemoAPI

### Versioned FastAPI Users API · Pydantic v2 · Docker

A clean, extensible learning project demonstrating API versioning, request validation, CRUD operations, and containerized development.

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Async-009688?logo=fastapi&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-v2-E92063)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)

</div>

---

## ✨ Features

- **API versioning:** V1 and V2 run side by side.
- **Users CRUD:** Create, list, retrieve, replace, partially update, and delete users.
- **Pydantic v2:** Typed request/response schemas and validation.
- **Consistent errors:** Clear 404 and duplicate-email 409 responses.
- **Docker:** Dockerfile and Docker Compose support.
- **Interactive docs:** Swagger UI and ReDoc.
- **Postman:** Importable collection for endpoint testing.

## 🧱 Project architecture

```text
DemoAPI/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py
│   └── api/
│       ├── __init__.py
│       ├── v1/
│       │   ├── __init__.py
│       │   └── endpoints/
│       │       ├── __init__.py
│       │       └── users.py
│       └── v2/
│           ├── __init__.py
│           └── endpoints/
│               ├── __init__.py
│               └── users.py
├── postman/
│   └── DemoAPI.postman_collection.json
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .gitignore
├── requirements.txt
└── README.md
```

> `FastAPI-endpoints/` is retained as the original task/reference implementation. The active application runs from the organized `app/` package.

## 🔀 API versions

| Version | Base path | Focus |
|---|---|---|
| V1 | `/api/v1` | Basic Users CRUD |
| V2 | `/api/v2/users` | Pydantic v2 schemas and richer validation |

### Health

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | Container/API health check |

### V1 — Users

| Method | Endpoint |
|---|---|
| POST | `/api/v1/users` |
| GET | `/api/v1/all_users` |
| GET | `/api/v1/fetch/user/{user_id}` |
| PUT | `/api/v1/user/{user_id}` |
| DELETE | `/api/v1/user/{user_id}` |

### V2 — Users

| Method | Endpoint |
|---|---|
| POST | `/api/v2/users/` |
| GET | `/api/v2/users/` |
| GET | `/api/v2/users/{user_id}` |
| PUT | `/api/v2/users/{user_id}` |
| PATCH | `/api/v2/users/{user_id}` |
| DELETE | `/api/v2/users/{user_id}` |

### V2 example request

```json
{
  "name": "Aditya Raj",
  "email": "aditya@example.com",
  "age": 21,
  "phone": "9876543210",
  "is_active": true
}
```

V2 requires a valid email, a name of 2–50 characters, and an age from 18 to 100. Phone is optional; `is_active` defaults to `true`.

## ⚙️ Run locally (Windows PowerShell)

Python 3.10+ is recommended.

```powershell
git clone https://github.com/adityaraj150107-star/DemoAPI.git
cd DemoAPI

py -m venv .venv
.\.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
pip install -r requirements.txt

uvicorn app.main:app --reload
```

Open:

- Swagger: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
- Health: http://127.0.0.1:8000/health

## 🐳 Run with Docker

Make sure Docker Desktop is running:

```powershell
docker compose up --build
```

Stop the containers:

```powershell
docker compose down
```

## 📮 Postman

Import `postman/DemoAPI.postman_collection.json` into Postman. The collection includes the local base URL variable. Start the API before sending requests.

## 📝 Important storage note

This is a learning/demo implementation using in-memory Python dictionaries/lists. Data is reset when the application restarts, and storage is not shared between V1 and V2. A persistent database, migrations, authentication, and automated tests are future improvements—not production features yet.

## 👨‍💻 Author

**Aditya Rajput**  
[GitHub](https://github.com/adityaraj150107-star) · [LinkedIn](https://www.linkedin.com/in/aditya-rajput-105768409)

---

⭐ If you find this project useful, consider giving it a star.


## 📅 Internship Task Log

Work is documented day by day. Each folder contains the objective, task checklist, commands, deliverables, and space for notes/screenshots.

| Day | Topic | Documentation |
|---|---|---|
| Day 01 | Tools Setup & Git Basics | [Open Day 01](Day-01-Tools-Setup-and-Git/README.md) |
| Day 02 | Docker Development Environment | [Open Day 02](Day-02-Docker-Development-Environment/README.md) |
| Day 03 | FastAPI CRUD Operations | [Open Day 03](Day-03-FastAPI-Pydantic-V2-Users-API/README.md) |
| Day 04 | Pydantic V2 Request & Response Models | [Open Day 04](Day-04-Pydantic-V2-Users-Models/README.md) |\n| Day 05 | PostgreSQL + SQLAlchemy CRUD (FastAPI V3) | [Open Day 05](Day-05-FastAPI-PostgreSQL-SQLAlchemy/README.md) |

> **Note:** These folders organize task documentation. The runnable application remains in `app/`, with V1 and V2 kept side by side. Check off tasks only after completing and verifying them.
