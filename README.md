<div align="center">

# DemoAPI

### FastAPI Internship Practice — Day 01 to Day 05

A structured, hands-on backend development repository. Each day has its own application, dependencies, instructions, and task documentation.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-REST%20API-009688?logo=fastapi&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-V2-E92063)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-4169E1?logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-D71F00?logo=sqlalchemy&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED?logo=docker&logoColor=white)

</div>

---

## Learning roadmap

| Day | Topic | Main deliverable |
|:---:|---|---|
| 01 | Tools Setup & Git | Development setup and Git workflow notes |
| 02 | Docker Development Environment | Containerized FastAPI health-check API |
| 03 | FastAPI CRUD | Standalone Users CRUD REST API |
| 04 | Pydantic V2 | Typed request/response models and validation |
| 05 | PostgreSQL & SQLAlchemy | SQL practice and database-backed V3 CRUD API |

## Repository structure

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
│   ├── Task-01-PostgreSQL/
│   │   ├── users_queries.sql
│   │   └── README.md
│   ├── Task-02-SQLAlchemy-CRUD/
│   │   ├── app/
│   │   │   ├── main.py
│   │   │   ├── database.py
│   │   │   ├── models.py
│   │   │   ├── schemas.py
│   │   │   └── crud.py
│   │   ├── .env.example
│   │   ├── requirements.txt
│   │   └── README.md
│   └── README.md
│
└── README.md
```

## How to use this repository

1. Open the day folder you want to study.
2. Read that folder's README before running commands.
3. Create a virtual environment inside that day folder.
4. Install that day's own `requirements.txt`.
5. Run the application using the command documented for that day.
6. Test endpoints in Swagger UI and save your own screenshots.

Each day is a separate learning project. This avoids dependency conflicts and makes it easy to run one task without affecting another.

## Quick links

- [Day 01 — Tools Setup & Git](Day-01-Tools-Setup-and-Git/README.md)
- [Day 02 — Docker Development Environment](Day-02-Docker-Development-Environment/README.md)
- [Day 03 — FastAPI CRUD](Day-03-FastAPI-CRUD/README.md)
- [Day 04 — Pydantic V2 Users Models](Day-04-Pydantic-V2-Users-Models/README.md)
- [Day 05 — PostgreSQL & SQLAlchemy](Day-05-FastAPI-PostgreSQL-SQLAlchemy/README.md)

## Technology stack

- Python
- FastAPI
- Pydantic V2
- PostgreSQL
- SQLAlchemy ORM
- Psycopg
- Docker and Docker Compose
- Git and GitHub
- Postman and Swagger UI

## Important notes

- Day 03 uses temporary in-memory storage; its records reset when the app restarts.
- Day 04 is a separate Pydantic V2 learning application and also uses in-memory storage.
- Day 05 Task 1 contains PostgreSQL SQL practice.
- Day 05 Task 2 is a separate FastAPI V3 application connected to PostgreSQL through SQLAlchemy.
- Never commit real passwords or API secrets. Use the provided `.env.example` as a template and keep your local `.env` file private.
- Documentation and code are provided for learning. Run and verify each project locally before submitting it.

## Author

**Aditya Rajput**  
BCA Student | Backend Development & AI/ML Enthusiast

- GitHub: [adityaraj150107-star](https://github.com/adityaraj150107-star)
- LinkedIn: [Aditya Rajput](https://www.linkedin.com/in/aditya-rajput-105768409)
