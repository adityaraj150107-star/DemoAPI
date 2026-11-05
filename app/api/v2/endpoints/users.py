"""Version 2 Users endpoints with Pydantic v2 validation."""
from fastapi import APIRouter, HTTPException, status

from app.models.user import (
    MessageResponse,
    UserCreate,
    UserResponse,
    UserUpdate,
    UsersListResponse,
)

router = APIRouter(prefix="/api/v2/users", tags=["Users - V2"])

# Learning/demo storage. Replace with a database repository for production.
users_db: dict[int, dict] = {}
_next_user_id = 1


def _ensure_email_available(email: str, *, exclude_id: int | None = None) -> None:
    for user_id, user in users_db.items():
        if user_id != exclude_id and user["email"] == email:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail={
                    "code": "EMAIL_ALREADY_EXISTS",
                    "message": "This email is already registered.",
                },
            )


def _get_user_or_404(user_id: int) -> dict:
    user = users_db.get(user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "code": "USER_NOT_FOUND",
                "message": f"User with ID {user_id} does not exist.",
            },
        )
    return user


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(payload: UserCreate):
    global _next_user_id
    _ensure_email_available(str(payload.email))
    user = {"id": _next_user_id, **payload.model_dump()}
    users_db[_next_user_id] = user
    _next_user_id += 1
    return user


@router.get("/", response_model=UsersListResponse)
async def list_users():
    data = list(users_db.values())
    return {"message": "Users fetched successfully", "total_users": len(data), "data": data}


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    return _get_user_or_404(user_id)


@router.put("/{user_id}", response_model=UserResponse)
async def replace_user(user_id: int, payload: UserCreate):
    _get_user_or_404(user_id)
    _ensure_email_available(str(payload.email), exclude_id=user_id)
    updated = {"id": user_id, **payload.model_dump()}
    users_db[user_id] = updated
    return updated


@router.patch("/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, payload: UserUpdate):
    user = _get_user_or_404(user_id)
    changes = payload.model_dump(exclude_unset=True)
    if "email" in changes and changes["email"] is not None:
        _ensure_email_available(str(changes["email"]), exclude_id=user_id)
        changes["email"] = str(changes["email"])
    user.update(changes)
    return user


@router.delete("/{user_id}", response_model=MessageResponse)
async def delete_user(user_id: int):
    _get_user_or_404(user_id)
    del users_db[user_id]
    return {"message": "User deleted successfully"}
