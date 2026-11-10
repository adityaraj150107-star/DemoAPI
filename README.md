<div align="center">

# <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" width="34" height="34" alt="FastAPI"> DemoAPI — FastAPI Internship Work

### Day 01 → Day 05 | Backend Development Learning & Implementation

A day-wise, hands-on backend development repository covering developer setup, Git & GitHub, Docker, REST API development, Pydantic V2 validation, PostgreSQL, and SQLAlchemy ORM.

<p>
  <a href="https://github.com/adityaraj150107-star/DemoAPI"><img src="https://img.shields.io/badge/Repository-DemoAPI-181717?logo=github" alt="GitHub repository"></a>
  <img src="https://img.shields.io/badge/Progress-Day%2001--05-blue" alt="Day 01 to Day 05">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-REST%20API-009688?logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Pydantic-V2-E92063" alt="Pydantic V2">
  <img src="https://img.shields.io/badge/PostgreSQL-Database-4169E1?logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/SQLAlchemy-ORM-D71F00?logo=sqlalchemy&logoColor=white" alt="SQLAlchemy">
  <img src="https://img.shields.io/badge/Docker-Containerization-2496ED?logo=docker&logoColor=white" alt="Docker">
</p>

</div>

---

## 👨‍💻 About This Repository

**DemoAPI** is my practical backend development learning repository. It documents the work completed across five learning days, with each day organized into a separate folder so the code, dependencies, instructions, and deliverables remain easy to understand and maintain.

The repository follows a progressive learning path:

**Development Setup → Docker → FastAPI CRUD → Pydantic V2 → PostgreSQL & SQLAlchemy**

The focus is on understanding how backend APIs are designed, validated, documented, containerized, and connected to a relational database.

---

## 🛠️ Tech Stack

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="42" alt="Python">
  &nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" width="42" alt="FastAPI">
  &nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" width="42" alt="PostgreSQL">
  &nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" width="42" alt="Docker">
  &nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" width="42" alt="Git">
</p>

| Technology | Purpose |
|---|---|
| 🐍 Python | Backend programming language |
| ⚡ FastAPI | High-performance REST API framework |
| 📦 Pydantic V2 | Request validation and response schemas |
| 🗄️ PostgreSQL | Relational database |
| 🔗 SQLAlchemy ORM | Python-based database operations |
| 🔐 JWT | Token-based authentication in Day 05 |
| 🐳 Docker | Application containerization |
| ⚙️ Docker Compose | Container and service configuration |
| 🦄 Uvicorn | ASGI server for running FastAPI |
| 🔧 Git & GitHub | Version control and source-code hosting |

---

## 🗓️ Day-wise Learning & Task Implementation

### Day 01 — Tools Setup & Git Basics

<kbd>FOUNDATION</kbd>

**Objective:** Prepare the development environment and understand the Git/GitHub workflow used to manage project code.

**Tasks & work**
- Set up Python and Visual Studio Code.
- Verify the development environment and terminal commands.
- Understand Git repositories, working tree, staging area, and commits.
- Practice `git init`, `git status`, `git add`, and `git commit`.
- Understand remote repositories, `git push`, and `git pull`.
- Organize the learning work in the DemoAPI GitHub repository.

**Concepts learned:** Development environment, version control, repository, staging, commit history, remote origin, and GitHub.

**Deliverable:** A configured development environment and a GitHub repository for maintaining the day-wise tasks.

[Open Day 01 documentation →](Day-01-Tools-Setup-and-Git/README.md)

---

### Day 02 — Docker Development Environment

<kbd>CONTAINERIZATION</kbd>

**Objective:** Create a small FastAPI health-check API and run it inside a Docker container.

**Tasks & work**
- Learn Docker images, containers, Dockerfiles, and Docker Compose.
- Create a FastAPI application with a `GET /health` endpoint.
- Return a JSON health response: `{"status": "ok"}`.
- Write a Dockerfile to build the application image.
- Configure Docker Compose to start the API.
- Build and run the container, then test the endpoint using a browser or Postman.

**Key files:** `app/main.py`, `Dockerfile`, `docker-compose.yml`, and `requirements.txt`.

**Expected API response**
```json
{
  "status": "ok"
}
```

**Concepts learned:** Containerization, image building, port mapping, container lifecycle, and Compose-based execution.

[Open Day 02 documentation →](Day-02-Docker-Development-Environment/README.md)

---

### Day 03 — FastAPI Users CRUD API

<kbd>REST API DEVELOPMENT</kbd>

**Objective:** Build a Users REST API and understand the four fundamental CRUD operations.

**Tasks & work**
- Create a FastAPI application and organize API routes under the V1 endpoint.
- Implement Create, Read, Update, and Delete operations for users.
- Handle JSON request bodies and URL path parameters.
- Generate user IDs and prevent duplicate email addresses.
- Validate basic user fields and return meaningful HTTP errors.
- Test the endpoints through Swagger UI.

**CRUD endpoint summary**

| Operation | Method | Endpoint |
|---|---|---|
| Create user | POST | `/api/v1/users` |
| Get all users | GET | `/api/v1/all_users` |
| Get user by ID | GET | `/api/v1/fetch/user/{user_id}` |
| Update user | PUT | `/api/v1/user/{user_id}` |
| Delete user | DELETE | `/api/v1/user/{user_id}` |

**Concepts learned:** REST principles, HTTP methods, route parameters, request payloads, CRUD logic, status codes, and exception handling.

**Storage note:** This Day 03 exercise uses in-memory storage. User records reset when the application restarts.

[Open Day 03 documentation →](Day-03-FastAPI-CRUD/README.md)

---

### Day 04 — Pydantic V2 Request & Response Models

<kbd>DATA VALIDATION</kbd>

**Objective:** Create structured Pydantic V2 models for Users API requests and responses, with clear validation rules.

**Tasks & work**
- Create request models for user creation and updates.
- Create response models to define consistent API output.
- Apply required fields, default values, type annotations, and field constraints.
- Validate email format and numeric boundaries.
- Reject unexpected request fields.
- Handle invalid payloads with clear validation responses.
- Test valid and invalid requests through Swagger UI.

**Models covered:** `UserCreate`, `UserUpdate`, `UserResponse`, `UsersListResponse`, and `MessageResponse`.

**Example request**
```json
{
  "name": "Aditya Raj",
  "email": "aditya@example.com",
  "age": 21,
  "phone": "9876543210",
  "is_active": true
}
```

**Concepts learned:** Pydantic V2, schema design, `EmailStr`, `Field`, model configuration, validation, and response serialization.

**Storage note:** Day 04 is a separate learning API using in-memory storage; PostgreSQL persistence is handled in Day 05.

[Open Day 04 documentation →](Day-04-Pydantic-V2-Users-Models/README.md)

---

### Day 05 — PostgreSQL, JWT Authentication & Task Management

<kbd>DATABASE INTEGRATION</kbd>

**Objective:** Practice PostgreSQL and build a database-backed FastAPI task manager with JWT authentication and teacher/student permissions.

Day 05 is divided into two separate tasks inside one Day 05 folder.

#### Task 1 — PostgreSQL Database & SQL Queries

**Work covered**
- Connect to PostgreSQL using pgAdmin.
- Create and use the `demoapi_day5` database.
- Create the `users` table with suitable columns and constraints.
- Insert sample users and retrieve records.
- Practice filtering, sorting, updating, and deleting records.
- Use aggregate queries such as `COUNT` and `GROUP BY`.

**SQL concepts:** `CREATE TABLE`, `INSERT`, `SELECT`, `WHERE`, `ORDER BY`, `UPDATE`, `DELETE`, `COUNT`, and `GROUP BY`.

[Open Task 1 — PostgreSQL →](Day-05-FastAPI-PostgreSQL-SQLAlchemy/Task-01-PostgreSQL/README.md)

#### Task 2 — FastAPI Task Manager with SQLAlchemy ORM

**Work covered**
- Configure the PostgreSQL connection through environment variables.
- Create a SQLAlchemy engine and session factory.
- Add users, hashed passwords, roles, tasks, and revocable refresh-token sessions.
- Implement login, logout, token refresh, and protected FastAPI dependencies.
- Restrict task management, user visibility, and progress reporting by role.
- Test API behavior in pytest and the supplied Postman collection.

**Authentication and task endpoints**

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | API health check |
| POST | `/auth/register`, `/auth/login`, `/auth/refresh`, `/auth/logout` | Authentication/session lifecycle |
| GET | `/auth/me` | Current user's profile |
| POST/GET/PATCH/DELETE | `/api/v3/tasks` | Role-protected task management |
| GET | `/api/v3/progress` | Teacher-only progress report |

**Concepts learned:** PostgreSQL, SQLAlchemy ORM, JWT access/refresh tokens, Argon2 password hashing, session revocation, authentication dependencies, RBAC, and 401 vs 403 errors.

[Open Task 2 — Authenticated Task Manager →](Day-05-FastAPI-PostgreSQL-SQLAlchemy/Task-02-SQLAlchemy-CRUD/README.md)

**Database note:** PostgreSQL is required; the task README also documents using Supabase PostgreSQL when local PostgreSQL is unavailable. The seed command provisions a teacher and student from private environment variables.

---

## 📁 Repository Architecture

The repository is organized into five independent learning days. Day 05 contains two separate tasks: PostgreSQL SQL practice and a database-backed FastAPI application. The Task 2 project now also includes **Alembic database migrations** to version and safely apply schema changes.

```text
DemoAPI/
│
├── Day-01-Tools-Setup-and-Git/
│   └── README.md
│
├── Day-02-Docker-Development-Environment/
│   ├── app/
│   │   └── main.py
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── requirements.txt
│   └── README.md
│
├── Day-03-FastAPI-CRUD/
│   ├── app/
│   │   ├── main.py
│   │   └── api/v1/endpoints/users.py
│   ├── requirements.txt
│   └── README.md
│
├── Day-04-Pydantic-V2-Users-Models/
│   ├── app/
│   │   ├── main.py
│   │   ├── api/v2/endpoints/users.py
│   │   └── models/user.py
│   ├── requirements.txt
│   └── README.md
│
├── Day-05-FastAPI-PostgreSQL-SQLAlchemy/
│   │
│   ├── Task-01-PostgreSQL/
│   │   ├── users_queries.sql
│   │   └── README.md
│   │
│   ├── Task-02-SQLAlchemy-CRUD/
│   │   ├── app/
│   │   │   ├── main.py
│   │   │   ├── auth.py
│   │   │   ├── database.py
│   │   │   ├── dependencies.py
│   │   │   ├── models.py
│   │   │   ├── schemas.py
│   │   │   ├── security.py
│   │   │   ├── seed.py
│   │   │   ├── tasks.py
│   │   │   └── users.py
│   │   │
│   │   ├── alembic/
│   │   │   ├── versions/
│   │   │   │   ├── d5d28bcf185f_create_users_tasks_and_sessions.py
│   │   │   │   └── 3b3f2c0dd5d0_add_work_notes_to_tasks.py
│   │   │   ├── env.py
│   │   │   └── script.py.mako
│   │   │
│   │   ├── tests/
│   │   ├── .env.example
│   │   ├── alembic.ini
│   │   ├── requirements.txt
│   │   └── README.md
│   │
│   └── README.md
│
└── README.md
```

### 🧩 New Alembic Migration Files — Day 05 Task 2

| File / Folder | Purpose |
|---|---|
| `alembic.ini` | Main Alembic configuration, including the migration script location and logging settings. |
| `alembic/env.py` | Connects Alembic to the project's SQLAlchemy models and database URL; provides online and offline migration configuration. |
| `alembic/script.py.mako` | Template used to generate new migration revision files. |
| `alembic/versions/` | Stores the ordered database schema revisions. |
| `d5d28bcf185f_create_users_tasks_and_sessions.py` | Initial migration that creates the `users`, `tasks`, and `sessions` tables, constraints, and indexes. |
| `3b3f2c0dd5d0_add_work_notes_to_tasks.py` | Adds the optional `work_notes` column to the `tasks` table; its downgrade removes that column. |

**Migration workflow:** Update SQLAlchemy models → generate a revision with `alembic revision --autogenerate` → review the generated migration → apply it with `alembic upgrade head`. Use `alembic downgrade -1` to roll back the latest applied revision.

> **Important:** Run Alembic commands from the `Task-02-SQLAlchemy-CRUD` directory after configuring the database connection in `.env`. For an existing database, back it up and verify its schema before applying or stamping revisions. Do not apply the initial create-tables migration to a database that already contains those tables.

---

## ⚙️ Installation & Running Guide

Each day is an independent learning project with its own dependencies. Run the commands from the corresponding day/task folder.

### 1. Clone the repository

```bash
git clone https://github.com/adityaraj150107-star/DemoAPI.git
cd DemoAPI
```

### 2. Open the required Day folder

Example for Day 05 SQLAlchemy:

```powershell
cd Day-05-FastAPI-PostgreSQL-SQLAlchemy/Task-02-SQLAlchemy-CRUD
```

### 3. Create and activate a virtual environment

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 4. Install that task's dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Configure PostgreSQL for Day 05 Task 2

Create the `demoapi_day5` database, copy `.env.example` to `.env`, and update the PostgreSQL connection details and JWT signing key. If local PostgreSQL is unavailable, the Task 2 README explains Supabase PostgreSQL setup.

Example connection format:

```env
DATABASE_URL=postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/demoapi_day5
```

Keep your actual `.env` file private. Never commit database passwords or API secrets.

### 6. Run the FastAPI application

For Day 03 or Day 04, run from that day's folder:

```powershell
uvicorn app.main:app --reload
```

For Day 05 Task 2, use the same command from the Task 2 folder.

For Day 02 Docker execution, follow its README and use:

```powershell
docker compose up --build
```

---

## 📖 API Documentation & Testing

When a FastAPI application is running locally:

| Tool | URL | Use |
|---|---|---|
| Swagger UI | http://127.0.0.1:8000/docs | Explore and test API endpoints |
| ReDoc | http://127.0.0.1:8000/redoc | Read generated API documentation |
| Health endpoint | http://127.0.0.1:8000/health | Check service health where implemented |
| Postman | Configure request to localhost:8000 | Send and verify HTTP requests |

Use the README inside each day folder for the exact routes and request examples.

---

## 📚 Key Learning Outcomes

By working through these five days, the repository demonstrates practice with:

- Setting up a Python backend development environment.
- Managing source code using Git and GitHub.
- Understanding Docker images, containers, and Compose.
- Designing RESTful APIs with FastAPI.
- Implementing CRUD operations and HTTP error handling.
- Creating and validating request/response schemas using Pydantic V2.
- Writing PostgreSQL queries for database operations.
- Connecting FastAPI to PostgreSQL using SQLAlchemy ORM.
- Organizing backend code into routes, schemas, models, database, and CRUD layers.
- Testing APIs through Swagger UI and Postman.

---

## 🔐 Security & Project Notes

- Each day has its own project folder and dependency file to reduce dependency conflicts.
- Day 03 and Day 04 use in-memory data for learning; data resets when their application restarts.
- Day 05 Task 2 uses PostgreSQL for persistent user records.
- Use `.env.example` as a template and keep local secrets out of Git.
- The current Day 05 SQLAlchemy API manages Users. Task status labels are documented separately and do not imply a Tasks CRUD API.
- Run and test each application locally before treating a task as completed.

---

## ✨ Key Features

- 📅 **Day-wise Learning Path** — Five organized days with separate task folders and documentation.
- 🐍 **FastAPI REST APIs** — Build and test backend endpoints using FastAPI.
- 🔄 **CRUD Operations** — Practice creating, reading, updating, and deleting user records.
- ✅ **Pydantic V2 Validation** — Define request and response models with validation rules.
- 🐘 **PostgreSQL Integration** — Create tables and practice SQL queries.
- 🔗 **SQLAlchemy ORM** — Connect FastAPI with PostgreSQL and manage database records.
- 🔐 **JWT Authentication** — Practice login, protected routes, refresh tokens, and role-based access in Day 05.
- 🐳 **Docker Development** — Build and run a containerized FastAPI health-check API.
- 🧪 **API Testing** — Verify endpoints through Swagger UI, Postman, and automated tests where provided.
- 📖 **Task Documentation** — Each day/task includes its own README and run instructions.

## ⚙️ Prerequisites

Before running a task, install the tools required by that task:

- 🐍 Python 3.10 or a compatible version
- 🧰 Visual Studio Code or another Python editor
- 🔧 Git
- 🐳 Docker Desktop (required for Day 02)
- 🐘 PostgreSQL and pgAdmin (required for Day 05 database tasks)
- 📬 Postman (recommended for API testing)

Each day is an independent learning project. Check that day's README for its exact dependencies and setup instructions.

## 📋 Task Status

- `pending`
- `in_progress`
- `done`

## 👤 User Status

- `active`
- `inactive`

---

## 🩺 Troubleshooting

| Issue | Suggested Solution |
|---|---|
| Python command is not recognized | Install Python and enable the PATH option, then reopen the terminal. |
| Module not found | Open the correct Day/Task folder, activate its virtual environment, and install its `requirements.txt`. |
| Uvicorn command is not recognized | Activate the virtual environment and install the task dependencies. |
| Port 8000 is already in use | Stop the process using the port or run the API on another port. |
| Docker command fails | Start Docker Desktop and wait until the engine is running. |
| PostgreSQL connection fails | Check that PostgreSQL is running and verify the database name, username, password, host, and port in `.env`. |
| API returns 401 or 403 | Check the authentication token and the role/permissions required by the endpoint. |

## 🔒 Security Best Practices

- Keep real passwords, database URLs, JWT secrets, and API keys inside local environment variables.
- Never commit the actual `.env` file; use an `.env.example` template for required variable names.
- Use password hashing instead of storing plain-text passwords.
- Protect private endpoints with authentication and appropriate authorization checks.
- Validate incoming request data before processing it.
- Do not expose database credentials or sensitive tokens in screenshots, logs, or public documentation.

## 🎯 Learning Objectives

This repository provides practical experience with:

- Python backend development and environment setup.
- Git and GitHub version-control workflows.
- Docker images, containers, Dockerfiles, and Docker Compose.
- REST API design and CRUD operations using FastAPI.
- Request validation and response serialization using Pydantic V2.
- SQL queries, relational database concepts, and PostgreSQL.
- SQLAlchemy engine, sessions, ORM models, and database-backed CRUD.
- JWT authentication, refresh-token flow, and role-based access control.
- API testing through Swagger UI, Postman, and pytest.

## 🔮 Future Improvements

Possible next steps for this learning repository:

- Add more automated unit and integration tests.
- Add structured logging and consistent error responses.
- Add CI checks with GitHub Actions.
- Add API rate limiting and production configuration examples.
- Deploy selected APIs to a cloud hosting platform.
- Add more authentication and authorization test cases.

## 🤝 Contributing

This repository is maintained as a practical learning project. Suggestions and improvements are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make a focused change and test it.
4. Commit with a clear message.
5. Open a pull request describing the change.

## 👤 Author

**Aditya Rajput**  
BCA Student | Backend Development | Python & FastAPI Learner

<p>
  <a href="https://github.com/adityaraj150107-star"><img src="https://img.shields.io/badge/GitHub-adityaraj150107--star-181717?logo=github" alt="GitHub"></a>
  <a href="https://www.linkedin.com/in/aditya-rajput-105768409"><img src="https://img.shields.io/badge/LinkedIn-Aditya%20Rajput-0A66C2?logo=linkedin&logoColor=white" alt="LinkedIn"></a>
</p>

---

<div align="center">

**Thanks for visiting DemoAPI!**

*Learning by building, one day at a time.*

</div>
