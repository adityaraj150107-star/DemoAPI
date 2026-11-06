from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI, HTTPException, Query, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, selectinload
from sqlalchemy import select

from .database import Base, engine, get_db
from . import models, schemas

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Convenient for a learning project. In production, use Alembic migrations.
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(
    title="PMS Portal API - DemoAI v3",
    description="Day 5 project: PostgreSQL schema + SQLAlchemy CRUD with FastAPI.",
    version="3.0.0",
    lifespan=lifespan,
)

@app.get("/", tags=["Health"])
def home():
    return {"message": "PMS Portal API is running", "docs": "/docs", "version": "3.0.0"}

# ----------------------------- USERS CRUD -----------------------------
@app.post("/users", response_model=schemas.UserSummary, status_code=status.HTTP_201_CREATED, tags=["Users"])
def create_user(payload: schemas.UserCreate, db: Session = Depends(get_db)):
    user = models.User(**payload.model_dump())
    db.add(user)
    try:
        db.commit()
        db.refresh(user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="A user with this email already exists")
    return user

@app.get("/users", response_model=list[schemas.UserSummary], tags=["Users"])
def list_users(skip: int = Query(0, ge=0), limit: int = Query(100, ge=1, le=200), db: Session = Depends(get_db)):
    return db.scalars(select(models.User).offset(skip).limit(limit)).all()

@app.get("/users/{user_id}", response_model=schemas.UserWithTasks, tags=["Users"])
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.scalar(
        select(models.User).options(selectinload(models.User.tasks)).where(models.User.id == user_id)
    )
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{user_id}", response_model=schemas.UserSummary, tags=["Users"])
def update_user(user_id: int, payload: schemas.UserUpdate, db: Session = Depends(get_db)):
    user = db.get(models.User, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(user, key, value)
    try:
        db.commit()
        db.refresh(user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="A user with this email already exists")
    return user

@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Users"])
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.get(models.User, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()

# ----------------------------- TASKS CRUD -----------------------------
@app.post("/tasks", response_model=schemas.TaskRead, status_code=status.HTTP_201_CREATED, tags=["Tasks"])
def create_task(payload: schemas.TaskCreate, db: Session = Depends(get_db)):
    if db.get(models.User, payload.user_id) is None:
        raise HTTPException(status_code=404, detail="Assigned user not found")
    task = models.Task(**payload.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

@app.get("/tasks", response_model=list[schemas.TaskRead], tags=["Tasks"])
def list_tasks(
    task_status: schemas.TaskStatus | None = Query(default=None, alias="status"),
    user_id: int | None = Query(default=None, gt=0),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=200),
    db: Session = Depends(get_db),
):
    statement = select(models.Task)
    if task_status is not None:
        statement = statement.where(models.Task.status == task_status)
    if user_id is not None:
        statement = statement.where(models.Task.user_id == user_id)
    return db.scalars(statement.order_by(models.Task.id).offset(skip).limit(limit)).all()

@app.get("/tasks/{task_id}", response_model=schemas.TaskRead, tags=["Tasks"])
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.get(models.Task, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=schemas.TaskRead, tags=["Tasks"])
def update_task(task_id: int, payload: schemas.TaskUpdate, db: Session = Depends(get_db)):
    task = db.get(models.Task, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    changes = payload.model_dump(exclude_unset=True)
    if "user_id" in changes and db.get(models.User, changes["user_id"]) is None:
        raise HTTPException(status_code=404, detail="Assigned user not found")
    for key, value in changes.items():
        setattr(task, key, value)
    db.commit()
    db.refresh(task)
    return task

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Tasks"])
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.get(models.Task, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
