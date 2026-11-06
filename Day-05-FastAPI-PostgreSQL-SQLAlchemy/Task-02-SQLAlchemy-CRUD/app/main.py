from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from . import crud, models
from .database import Base, engine, get_db
from .schemas import UserCreate, UserResponse, UserUpdate

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="DemoAPI — V3 SQLAlchemy CRUD",
    description="Day 05 task: FastAPI CRUD using SQLAlchemy ORM and PostgreSQL.",
    version="3.0.0",
)


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok", "version": "v3"}


@app.post(
    "/api/v3/users/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Users V3"],
)
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_user(db, payload)
    except IntegrityError:
        raise HTTPException(status_code=409, detail="A user with this email already exists.")


@app.get("/api/v3/users/", response_model=list[UserResponse], tags=["Users V3"])
def read_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    if skip < 0 or not 1 <= limit <= 100:
        raise HTTPException(status_code=422, detail="skip must be >= 0 and limit must be between 1 and 100.")
    return crud.get_users(db, skip=skip, limit=limit)


@app.get("/api/v3/users/{user_id}", response_model=UserResponse, tags=["Users V3"])
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found.")
    return user


@app.put("/api/v3/users/{user_id}", response_model=UserResponse, tags=["Users V3"])
def replace_user(user_id: int, payload: UserUpdate, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found.")
    try:
        return crud.update_user(db, user, payload)
    except IntegrityError:
        raise HTTPException(status_code=409, detail="A user with this email already exists.")


@app.delete("/api/v3/users/{user_id}", tags=["Users V3"])
def remove_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found.")
    crud.delete_user(db, user)
    return {"message": "User deleted successfully.", "user_id": user_id}
