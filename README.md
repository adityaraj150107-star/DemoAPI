# 🚀 DemoAPI — FastAPI Backend Development

<p align="center">
  <strong>A hands-on backend development project covering FastAPI, Docker, PostgreSQL, SQLAlchemy, authentication, testing, CI, and cloud deployment.</strong>
</p>

<p align="center">
  <a href="https://github.com/adityaraj150107-star/DemoAPI"><img src="https://img.shields.io/badge/GitHub-DemoAPI-181717?logo=github&logoColor=white" alt="GitHub"></a>
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-REST%20API-009688?logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/PostgreSQL-Database-4169E1?logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/SQLAlchemy-ORM-D71F00?logo=sqlalchemy&logoColor=white" alt="SQLAlchemy">
  <img src="https://img.shields.io/badge/Docker-Containerization-2496ED?logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/Render-Deployed-46E3B7?logo=render&logoColor=black" alt="Render">
  <img src="https://img.shields.io/badge/CI-GitHub%20Actions-2088FF?logo=githubactions&logoColor=white" alt="GitHub Actions">
</p>

---

## 📌 Overview

**DemoAPI** is a practical, day-wise backend development repository. It documents the journey from development environment setup and Git fundamentals to building, validating, testing, containerizing, and deploying REST APIs with FastAPI.

The repository is organized into five learning days. Day 05 contains two separate tasks: PostgreSQL query practice and a database-backed Task Manager API using SQLAlchemy.

**Learning path:**

`Development Setup → Docker → FastAPI CRUD → Pydantic V2 → PostgreSQL & SQLAlchemy → Authentication → Testing & CI → Render Deployment`

## ✨ Features

- ⚡ **FastAPI REST APIs** — Build APIs with organized routes and interactive documentation.
- 🔢 **API Versioning** — Practice versioned user endpoints across the learning tasks.
- 🔄 **CRUD Operations** — Create, read, update, and delete user and task records.
- ✅ **Pydantic V2** — Validate request data and define consistent response schemas.
- 🐘 **PostgreSQL** — Store persistent application data and practice SQL queries.
- 🔗 **SQLAlchemy ORM** — Work with database models, sessions, and relationships.
- 🔄 **Alembic Migrations** — Track schema changes with revision history and rollback support.
- 🔐 **JWT Authentication** — Access/refresh tokens, protected routes, and session revocation.
- 👥 **Role-Based Access Control** — Teacher and student permissions for task management.
- 🐳 **Docker & Compose** — Build and run a containerized FastAPI development environment.
- 🧪 **Testing** — Verify API behavior with Postman, Swagger UI, and pytest.
- ⚙️ **GitHub Actions CI** — Run automated tests on pushes and pull requests.
- ☁️ **Render Deployment** — Host the Task Manager API with a PostgreSQL database.

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
| ⚡ FastAPI | REST API framework |
| 📦 Pydantic V2 | Request validation and response schemas |
| 🐘 PostgreSQL | Relational database |
| 🔗 SQLAlchemy | Object-relational mapping |
| 🔄 Alembic | Database schema migrations |
| 🔐 JWT / Argon2 | Token authentication and password hashing |
| 🐳 Docker | Application containerization |
| ⚙️ Docker Compose | Container and service configuration |
| 🦄 Uvicorn | ASGI application server |
| 🧪 Pytest / Postman | Automated and manual API testing |
| 🔁 GitHub Actions | Continuous Integration |
| ☁️ Render | Cloud hosting and PostgreSQL deployment |

## 🗓️ Day-wise Learning & Implementation

### Day 01 — Tools Setup & Git Basics

**Objective:** Prepare the development environment and understand version control.

- Set up Python and Visual Studio Code.
- Understand repositories, working tree, staging, and commits.
- Practice `git init`, `git status`, `git add`, and `git commit`.
- Work with remote repositories using `git push` and `git pull`.

[Open Day 01 documentation →](Day-01-Tools-Setup-and-Git/README.md)

### Day 02 — Docker Development Environment

**Objective:** Create a small FastAPI health-check API and run it in Docker.

- Learn images, containers, Dockerfiles, and Docker Compose.
- Implement `GET /health` returning a JSON health response.
- Build the image and start the container.
- Test the endpoint using Postman or a browser.

**Expected response**
```json
{
  "status": "ok"
}
```

[Open Day 02 documentation →](Day-02-Docker-Development-Environment/README.md)

### Day 03 — FastAPI Users CRUD API

**Objective:** Build a REST API and implement the four CRUD operations.

- Create, read, update, and delete user records.
- Work with HTTP methods, path parameters, and JSON request bodies.
- Handle duplicate email addresses and invalid requests.
- Test endpoints using Swagger UI.

| Operation | Method | Endpoint |
|---|---|---|
| Create user | POST | `/api/v1/users` |
| Get all users | GET | `/api/v1/all_users` |
| Get user by ID | GET | `/api/v1/fetch/user/{user_id}` |
| Update user | PUT | `/api/v1/user/{user_id}` |
| Delete user | DELETE | `/api/v1/user/{user_id}` |

**Storage:** This learning exercise uses in-memory storage; records reset when the application restarts.

[Open Day 03 documentation →](Day-03-FastAPI-CRUD/README.md)

### Day 04 — Pydantic V2 Validation

**Objective:** Define structured request and response models with validation rules.

- Create user request and response schemas.
- Apply field types, required fields, defaults, and constraints.
- Validate email formats and numeric boundaries.
- Handle invalid payloads and test validation responses.

[Open Day 04 documentation →](Day-04-Pydantic-V2-Users-Models/README.md)

### Day 05 — PostgreSQL & SQLAlchemy

Day 05 is divided into two independent tasks.

#### Task 01 — PostgreSQL Queries

- Practice `INSERT`, `SELECT`, `UPDATE`, and `DELETE`.
- Understand tables, records, and relational database operations.
- Work with the `demoapi_day5` database.

[Open Task 01 documentation →](Day-05-FastAPI-PostgreSQL-SQLAlchemy/Task-01-PostgreSQL/README.md)

#### Task 02 — FastAPI Task Manager

- Connect FastAPI to PostgreSQL using SQLAlchemy ORM.
- Implement task management with teacher/student roles.
- Add JWT access and refresh token authentication.
- Hash passwords using Argon2 and support session revocation.
- Add pagination, title search, status filters, and task assignment.
- Manage database schema changes using Alembic.
- Write pytest API tests and run them through GitHub Actions.
- Deploy the application and PostgreSQL database using Render.

**Main API endpoints**

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Health check |
| POST | `/auth/register` | Register a student |
| POST | `/auth/login` | Login and create a session |
| POST | `/auth/refresh` | Rotate refresh token |
| POST | `/auth/logout` | Revoke current session |
| GET | `/auth/me` | Get current user profile |
| GET | `/api/v3/users/` | List users (teacher only) |
| GET | `/api/v3/users/{user_id}` | Get user profile |
| POST / GET | `/api/v3/tasks` | Create or list tasks |
| GET / PATCH / DELETE | `/api/v3/tasks/{task_id}` | Retrieve, update, or delete a task |
| GET | `/api/v3/progress` | Student progress report (teacher only) |

**Task statuses:** `pending`, `in progress`, and `done`.

[Open Task 02 documentation →](Day-05-FastAPI-PostgreSQL-SQLAlchemy/Task-02-SQLAlchemy-CRUD/README.md)

---

## 📂 Repository Structure

```text
DemoAPI/
├── .github/
│   └── workflows/
│       └── tests.yml
├── Day-01-Tools-Setup-and-Git/
│   └── README.md
├── Day-02-Docker-Development-Environment/
│   ├── app/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── requirements.txt
│   └── README.md
├── Day-03-FastAPI-CRUD/
│   ├── app/
│   ├── requirements.txt
│   └── README.md
├── Day-04-Pydantic-V2-Users-Models/
│   ├── app/
│   ├── requirements.txt
│   └── README.md
├── Day-05-FastAPI-PostgreSQL-SQLAlchemy/
│   ├── Task-01-PostgreSQL/
│   │   └── README.md
│   ├── Task-02-SQLAlchemy-CRUD/
│   │   ├── app/
│   │   ├── alembic/
│   │   ├── tests/
│   │   ├── .env.example
│   │   ├── alembic.ini
│   │   ├── requirements.txt
│   │   └── README.md
│   └── README.md
├── postman/
│   ├── collections/
│   ├── environments/
│   ├── globals/
│   └── *.postman_collection.json
├── render.yaml
└── README.md
```

## 🚀 Getting Started

### Prerequisites

Install the tools required for the task you want to run:

- Python 3.10 or newer
- Visual Studio Code
- Git
- Docker Desktop (Day 02)
- PostgreSQL (Day 05)
- Postman (recommended for API testing)

### 1. Clone the repository

```bash
git clone https://github.com/adityaraj150107-star/DemoAPI.git
cd DemoAPI
```

### 2. Navigate to a task folder

Example — Day 05 Task 02:

```powershell
cd Day-05-FastAPI-PostgreSQL-SQLAlchemy/Task-02-SQLAlchemy-CRUD
```

### 3. Create and activate a virtual environment

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Configure environment variables

Copy `.env.example` to `.env`, create the `demoapi_day5` PostgreSQL database, and update the database connection and JWT secret.

Example:

```env
DATABASE_URL=postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/demoapi_day5
JWT_SECRET_KEY=YOUR_PRIVATE_SECRET
ACCESS_TOKEN_MINUTES=15
REFRESH_TOKEN_DAYS=7
```

Never commit your real `.env`, database password, JWT secret, or seed credentials.

### 6. Apply database migrations

Run from the Task 02 directory:

```powershell
alembic upgrade head
alembic current
alembic history
```

After changing SQLAlchemy models, generate a migration, review it, and then apply it:

```powershell
alembic revision --autogenerate -m "describe the schema change"
alembic upgrade head
```

### 7. Start the API

```powershell
uvicorn app.main:app --reload
```

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc
- **Health check:** http://127.0.0.1:8000/health

Each day is an independent learning project. Use the README inside that day/task folder for its exact setup and run instructions.

## 🐳 Docker

Day 02 contains the Docker development environment.

From the Day 02 directory, build and start the application:

```bash
docker compose up --build
```

Run in the background:

```bash
docker compose up --build -d
```

Useful commands:

```bash
docker compose ps
docker compose logs -f
docker compose down
```

See the [Day 02 README](Day-02-Docker-Development-Environment/README.md) for the complete Docker setup.

## 🌐 Live Deployment — Render

<p align="center">
  <a href="https://demoapi-task-manager.onrender.com"><img src="https://img.shields.io/badge/Live%20API-Render-46E3B7?logo=render&logoColor=black" alt="Live API"></a>
  <a href="https://demoapi-task-manager.onrender.com/docs"><img src="https://img.shields.io/badge/Swagger-API%20Documentation-85EA2D?logo=swagger&logoColor=black" alt="Swagger UI"></a>
  <a href="https://demoapi-task-manager.onrender.com/health"><img src="https://img.shields.io/badge/Health-Check-success" alt="Health check"></a>
</p>

The **Day 05 Task Manager API** is deployed on Render and connected to a Render PostgreSQL database.

| Resource | Link | Purpose |
|---|---|---|
| Live API | [Open DemoAPI](https://demoapi-task-manager.onrender.com) | Deployed API base URL |
| Swagger UI | [Open API Docs](https://demoapi-task-manager.onrender.com/docs) | Explore and test endpoints |
| Health Check | [Check API Health](https://demoapi-task-manager.onrender.com/health) | Verify service response |

### Deployment configuration

The repository-root `render.yaml` Blueprint defines:

- A Python web service named `demoapi-task-manager`.
- A Render PostgreSQL database named `demoapi-task-manager-db`.
- The Task 02 application directory as the service root.
- Dependency installation from `requirements.txt`.
- Startup migrations, seed setup, and Uvicorn server command.
- Automatic deployment after configured checks pass.

### Required private environment variables

| Variable | Purpose |
|---|---|
| `DATABASE_URL` | Render PostgreSQL connection string |
| `JWT_SECRET_KEY` | Generated JWT signing secret |
| `ACCESS_TOKEN_MINUTES` | Access token lifetime |
| `REFRESH_TOKEN_DAYS` | Refresh session lifetime |
| `SEED_TEACHER_EMAIL` / `SEED_TEACHER_PASSWORD` | Initial teacher account |
| `SEED_STUDENT_EMAIL` / `SEED_STUDENT_PASSWORD` | Initial student account |

Keep all passwords and secret values in Render's private environment settings. Do not add them to this README or commit them to GitHub.

> **Render free-plan note:** The free web service may spin down after 15 minutes without traffic, so its first request after inactivity can take about a minute. The free PostgreSQL database expires 30 days after creation. Export or migrate any data you need to keep. See [Render free plan details](https://render.com/docs/free).

For the full deployment procedure, see [Task 02 — Deploy on Render](Day-05-FastAPI-PostgreSQL-SQLAlchemy/Task-02-SQLAlchemy-CRUD/README.md#deploy-on-render).

## 🔁 Continuous Integration — GitHub Actions

The workflow at `.github/workflows/tests.yml` runs the Task Manager pytest suite when code is pushed or a pull request is opened.

**CI workflow:**

1. Check out the repository.
2. Set up Python 3.12.
3. Install Task 02 dependencies.
4. Run `python -m pytest -q`.

Continuous Integration (CI) automatically checks code changes so test failures can be identified before changes are merged.

## 🧪 API Testing

Use Swagger UI or the Postman collections included in this repository.

1. Start the relevant FastAPI application.
2. Open `/docs` in your browser.
3. Select an endpoint and click **Try it out**.
4. Enter the required parameters or JSON body.
5. Execute the request and inspect the response.

Run automated tests for Day 05 Task 02 from its directory:

```powershell
python -m pytest -q
```

## 🗄️ Database Migrations — Alembic

Alembic manages database schema changes through versioned migration files instead of relying on automatic table creation when the API starts.

Common commands:

| Command | Purpose |
|---|---|
| `alembic revision --autogenerate -m "message"` | Generate a migration candidate |
| `alembic upgrade head` | Apply all pending migrations |
| `alembic current` | Show the current database revision |
| `alembic history` | Display migration history |
| `alembic downgrade -1` | Roll back one revision |

Always review generated migration files before applying them. Back up an existing database and verify its schema before applying the initial create-tables migration.

## 🩺 Troubleshooting

| Issue | Suggested solution |
|---|---|
| Python command not recognized | Install Python, enable PATH, and reopen the terminal. |
| Module not found | Activate the correct virtual environment and install that task's requirements. |
| Uvicorn not recognized | Activate the environment and install dependencies. |
| Port 8000 is occupied | Stop the conflicting process or use another port. |
| Docker command fails | Start Docker Desktop and wait for the engine to become ready. |
| PostgreSQL connection fails | Check database name, username, password, host, port, and service status. |
| API returns 401 | Check the access token and session validity. |
| API returns 403 | Check whether the logged-in user's role permits the operation. |
| Render service is slow to respond | The free service may be waking from inactivity. |

## 🔐 Security Best Practices

- Keep database credentials, JWT secrets, and seed passwords in environment variables.
- Never commit the actual `.env` file.
- Use `.env.example` with placeholder values for configuration guidance.
- Store passwords using secure hashing; never store plain-text passwords.
- Protect private endpoints with authentication and role-based authorization.
- Do not expose secrets in screenshots, logs, or public documentation.
- Review database migrations before applying them to an existing database.

## 🎯 Learning Outcomes

Through this repository, I have practiced:

- Python backend development and environment setup.
- Git and GitHub version-control workflows.
- Docker images, containers, Dockerfiles, and Docker Compose.
- REST API design and CRUD operations with FastAPI.
- Request validation using Pydantic V2.
- PostgreSQL queries and relational database concepts.
- SQLAlchemy ORM models, sessions, and database operations.
- Alembic migration generation, upgrades, history, and rollbacks.
- JWT authentication, refresh tokens, and role-based access control.
- API testing with Swagger UI, Postman, and pytest.
- Continuous Integration with GitHub Actions.
- Deployment of a FastAPI application and PostgreSQL database on Render.

## 🤝 Contributing

This repository is maintained as a practical learning project. Suggestions and improvements are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make a focused change and test it.
4. Commit with a clear message.
5. Open a pull request describing the change.

## 👤 Author

**Aditya Rajput**  
BCA Student | Backend Development | Python & FastAPI

<p>
  <a href="https://github.com/adityaraj150107-star"><img src="https://img.shields.io/badge/GitHub-adityaraj150107--star-181717?logo=github" alt="GitHub"></a>
  <a href="https://www.linkedin.com/in/aditya-rajput-105768409"><img src="https://img.shields.io/badge/LinkedIn-Aditya%20Rajput-0A66C2?logo=linkedin&logoColor=white" alt="LinkedIn"></a>
</p>

---

<p align="center">
  <strong>Thanks for visiting DemoAPI!</strong><br>
  <em>Learning by building, one day at a time.</em>
</p>
