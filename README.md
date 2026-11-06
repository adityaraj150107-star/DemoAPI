<div align="center">

# 🚀 DemoAPI

### A Day-by-Day FastAPI Internship Learning & Development Repository

Building REST APIs step by step — from development tools and Git fundamentals to Docker, Pydantic V2, PostgreSQL, and SQLAlchemy ORM.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-REST%20API-009688?logo=fastapi&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-V2-E92063)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-4169E1?logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-D71F00?logo=sqlalchemy&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED?logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-Version%20Control-F05032?logo=git&logoColor=white)

</div>

---

## 👋 About This Repository

**DemoAPI** is my hands-on internship learning repository. It documents my progress through practical daily tasks and demonstrates how I build, structure, test, and improve backend applications using Python and FastAPI.

The repository is organized day by day so that each stage of learning is easy to explore. It includes task notes, implementation code, database scripts, API endpoints, and setup instructions.

## 🎯 Learning Journey at a Glance

| Day | Focus Area | What I Worked On |
|:---:|---|---|
| 01 | Development Setup & Git | Tools setup, Git commands, GitHub repository workflow |
| 02 | Docker Development Environment | FastAPI health-check API, Dockerfile, Docker Compose |
| 03 | FastAPI CRUD | User API endpoints and REST CRUD operations |
| 04 | Pydantic V2 | Request/response schemas, field validation, and error handling |
| 05 | PostgreSQL & SQLAlchemy | SQL queries and a database-backed FastAPI V3 CRUD API |

---

# 📚 Internship Work — Day by Day

## 🟢 Day 01 — Development Tools Setup & Git Fundamentals

**Goal:** Prepare the development environment and understand how to manage code using Git and GitHub.

### Work covered
- Set up the development workspace and essential coding tools.
- Verified the Python and Visual Studio Code environment.
- Practiced Git commands for checking repository status and tracking changes.
- Learned the basic Git workflow: add, commit, push, and pull.
- Worked with GitHub repositories and the remote-origin concept.

### Key commands
```bash
git --version
git status
git add .
git commit -m "Initial project setup"
git push
git pull
```

**Skills:** Python environment · VS Code · Git · GitHub · Version Control

**Day 01 documentation:** [Open Tools Setup & Git notes](Day-01-Tools-Setup-and-Git/README.md)

---

## 🐳 Day 02 — Docker Development Environment

**Goal:** Understand containerized development and run a small FastAPI service with Docker.

### Work covered
- Learned the purpose of Docker images, containers, Dockerfiles, and Docker Compose.
- Set up and verified Docker Desktop.
- Prepared a FastAPI demo service with a health-check endpoint.
- Implemented `GET /health`, returning a JSON status response.
- Created Dockerfile and Docker Compose configuration.
- Built and started the application as a container.
- Practiced checking the API response using Postman.

### Health-check response
```json
{
  "status": "ok"
}
```

### Useful Docker commands
```bash
docker --version
docker compose version
docker compose up --build
docker compose down
```

**Skills:** Docker · Dockerfile · Docker Compose · FastAPI · REST endpoint testing · Postman

**Day 02 documentation:** [Open Docker Development Environment notes](Day-02-Docker-Development-Environment/README.md)

---

## ⚡ Day 03 — FastAPI Users CRUD API

**Goal:** Build REST API endpoints and understand the CRUD workflow using FastAPI.

### Work covered
- Created and organized a FastAPI application.
- Worked with API routes and HTTP methods.
- Implemented the Users resource workflow:
  - **Create** — add a new user.
  - **Read** — retrieve all users or a user by ID.
  - **Update** — modify an existing user.
  - **Delete** — remove a user.
- Practiced request bodies, path parameters, and JSON responses.
- Explored interactive API testing through Swagger UI.

### Main V1 endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/api/v1/users` | Create a user |
| GET | `/api/v1/all_users` | List users |
| GET | `/api/v1/fetch/user/{user_id}` | Fetch a user |
| PUT | `/api/v1/user/{user_id}` | Update a user |
| DELETE | `/api/v1/user/{user_id}` | Delete a user |

**Skills:** Python · FastAPI · REST API · HTTP methods · JSON · CRUD · Swagger UI

**Implementation:** [V1 Users endpoint](app/api/v1/endpoints/users.py) · [Application entry point](app/main.py)

---

## 🧩 Day 04 — Pydantic V2 Request & Response Models

**Goal:** Add structured data validation to the Users API using Pydantic V2.

### Work covered
- Learned how Pydantic models and `BaseModel` work.
- Created request and response schemas for user data.
- Worked with required fields, optional fields, and default values.
- Added data types, field constraints, and input validation.
- Validated user information such as name, email, age, and other fields.
- Connected schemas with FastAPI endpoints.
- Practiced testing valid and invalid request bodies through Swagger UI.

### V2 Users endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/api/v2/users/` | Create a user |
| GET | `/api/v2/users/` | List users |
| GET | `/api/v2/users/{user_id}` | Fetch a user |
| PUT | `/api/v2/users/{user_id}` | Replace user data |
| PATCH | `/api/v2/users/{user_id}` | Partially update a user |
| DELETE | `/api/v2/users/{user_id}` | Delete a user |

**Skills:** Pydantic V2 · BaseModel · Request Models · Response Models · Field Validation · FastAPI · Swagger UI

**Day 04 documentation:** [Open Pydantic V2 task notes](Day-04-Pydantic-V2-Users-Models/README.md)  
**Implementation:** [V2 Users endpoint](app/api/v2/endpoints/users.py)

---

## 🐘 Day 05 — PostgreSQL & SQLAlchemy ORM with FastAPI

**Goal:** Work with a relational database and integrate PostgreSQL into a FastAPI application using SQLAlchemy ORM.

Day 05 is divided into two practical tasks.

### Task 1 — PostgreSQL Database & SQL Queries

- Created and connected to the `demoapi_day5` database.
- Created a Users table with a primary key, unique email, constraints, defaults, and timestamp.
- Practiced inserting, reading, updating, and deleting records.
- Used filtering, sorting, limiting, and aggregate queries.
- Verified database records using PostgreSQL query results.

**SQL concepts:** `CREATE TABLE` · `INSERT` · `SELECT` · `WHERE` · `ORDER BY` · `UPDATE` · `DELETE` · `COUNT` · `GROUP BY`

[Open Task 1 — PostgreSQL instructions & SQL script](Day-05-FastAPI-PostgreSQL-SQLAlchemy/Task-01-PostgreSQL/README.md)

### Task 2 — SQLAlchemy CRUD API (FastAPI V3)

- Connected FastAPI with PostgreSQL using SQLAlchemy 2.x ORM and Psycopg.
- Configured the database engine, session factory, and database dependency.
- Created a SQLAlchemy User model and Pydantic request/response schemas.
- Separated database CRUD logic from API route handlers.
- Implemented Create, Read, Update, and Delete operations.
- Added handling for duplicate email records and users that do not exist.
- Exposed V3 endpoints for interactive testing in Swagger UI.

### V3 API endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | API health check |
| POST | `/api/v3/users/` | Create a user |
| GET | `/api/v3/users/` | List users |
| GET | `/api/v3/users/{user_id}` | Retrieve a user |
| PUT | `/api/v3/users/{user_id}` | Update a user |
| DELETE | `/api/v3/users/{user_id}` | Delete a user |

**Skills:** PostgreSQL · SQL · SQLAlchemy ORM · Psycopg · Pydantic V2 · FastAPI · Database Sessions · CRUD

[Open Task 2 — SQLAlchemy CRUD implementation & setup](Day-05-FastAPI-PostgreSQL-SQLAlchemy/Task-02-SQLAlchemy-CRUD/README.md)

> **Database note:** Day 05 V3 is a separate runnable application from the root V1/V2 learning API. Create the local PostgreSQL database and configure the task's `.env` file before running it. Never commit real database credentials.

---

## 🏗️ Repository Structure

```text
DemoAPI/
│
├── app/
│   ├── main.py
│   ├── models/
│   └── api/
│       ├── v1/
│       │   └── endpoints/
│       └── v2/
│           └── endpoints/
│
├── postman/
│   └── DemoAPI.postman_collection.json
│
├── Day-01-Tools-Setup-and-Git/
├── Day-02-Docker-Development-Environment/
├── Day-04-Pydantic-V2-Users-Models/
│
├── Day-05-FastAPI-PostgreSQL-SQLAlchemy/
│   ├── Task-01-PostgreSQL/
│   └── Task-02-SQLAlchemy-CRUD/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

The root `app/` contains the V1 and V2 learning API. Day 05 contains a separate V3 application that connects to PostgreSQL using SQLAlchemy.

## ▶️ Run the Main FastAPI Application

### 1. Clone the repository
```bash
git clone https://github.com/adityaraj150107-star/DemoAPI.git
cd DemoAPI
```

### 2. Create and activate a virtual environment (Windows PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 3. Start the application
```powershell
uvicorn app.main:app --reload
```

### 4. Explore the API
- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc
- **Health check:** http://127.0.0.1:8000/health

## 🧰 Technology Stack

| Area | Technologies |
|---|---|
| Programming Language | Python |
| Backend Framework | FastAPI |
| Data Validation | Pydantic V2 |
| Database | PostgreSQL |
| ORM & Driver | SQLAlchemy 2.x, Psycopg |
| Containerization | Docker, Docker Compose |
| API Testing | Swagger UI, Postman |
| Version Control | Git, GitHub |

## 📈 Key Learning Outcomes

Through these practical tasks, I am building experience in:

- Setting up and maintaining a Python backend development environment.
- Managing code and project history with Git and GitHub.
- Creating and testing REST APIs with FastAPI.
- Implementing CRUD operations and organizing API versions.
- Validating request and response data with Pydantic V2.
- Containerizing applications with Docker.
- Writing SQL queries and managing relational data with PostgreSQL.
- Connecting FastAPI applications to databases using SQLAlchemy ORM.

## 👨‍💻 Author

**Aditya Rajput**  
BCA Student | Backend Development & AI/ML Enthusiast

- GitHub: [adityaraj150107-star](https://github.com/adityaraj150107-star)
- LinkedIn: [Aditya Rajput](https://www.linkedin.com/in/aditya-rajput-105768409)

---

<div align="center">

**Thanks for visiting DemoAPI!**

⭐ If you find this learning repository useful, feel free to explore the code and give it a star.

</div>
