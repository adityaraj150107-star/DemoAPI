from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import User


def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[User]:
    statement = select(User).order_by(User.id).offset(skip).limit(limit)
    return list(db.scalars(statement).all())


def get_user(db: Session, user_id: int) -> User | None:
    return db.get(User, user_id)
