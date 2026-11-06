"""Day 03: Basic Users CRUD endpoints for FastAPI V1.

This version intentionally uses simple request dictionaries and in-memory
storage so the CRUD and HTTP concepts are easy to understand. Pydantic V2
request/response schemas are introduced separately in the Day 04 V2 API.
"""
import re
from typing import Any

from fastapi import APIRouter, Body, HTTPException, status

router = APIRouter(prefix="/api/v1", tags=["Users - V1"])

# Temporary in-memory storage for the Day 03 learning task.
# Records are lost when the application restarts.
users: dict[int, dict[str, Any]] = {}
_next_user_id = 1

_VALID_STATUSES = {"active", "inactive"}
_EMAIL_PATTERN = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")


def _validate_user_payload(payload: dict[str, Any], *, partial: bool = False) -> dict[str, Any]:
    """Validate basic fields without introducing the Day 04 Pydantic task."""
    allowed_fields = {"name", "email", "phone", "status"}
    unknown_fields = set(payload) - allowed_fields
    if unknown_fields:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Unknown field(s): {', '.join(sorted(unknown_fields))}",
        )

    required_fields = {"name", "email"}
    if not partial:
        missing = required_fields - payload.keys()
        if missing:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"Required field(s) missing: {', '.join(sorted(missing))}",
            )

    cleaned = dict(payload)

    if "name" in cleaned:
        name = cleaned["name"]
        if not isinstance(name, str) or not 2 <= len(name.strip()) <= 100:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="name must be a string containing 2 to 100 characters.",
            )
        cleaned["name"] = name.strip()

    if "email" in cleaned:
        email = cleaned["email"]
        if not isinstance(email, str) or not _EMAIL_PATTERN.fullmatch(email.strip()):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="email must be a valid email address.",
            )
        cleaned["email"] = email.strip().lower()

    if "phone" in cleaned and cleaned["phone"] is not None:
        phone = cleaned["phone"]
        if not isinstance(phone, str) or not 7 <= len(phone.strip()) <= 20:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="phone must be a string containing 7 to 20 characters.",
            )
        cleaned["phone"] = phone.strip()

    if "status" in cleaned:
        user_status = cleaned["status"]
        if not isinstance(user_status, str) or user_status not in _VALID_STATUSES:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="status must be either 'active' or 'inactive'.",
            )

    return cleaned


def _get_user_or_404(user_id: int) -> dict[str, Any]:
    user = users.get(user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} was not found.",
        )
    return user


def _ensure_email_is_unique(email: str, *, exclude_user_id: int | None = None) -> None:
    for existing_id, existing_user in users.items():
        if existing_id != exclude_user_id and existing_user["email"] == email:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="A user with this email address already exists.",
            )


@router.post(
    "/users",
    status_code=status.HTTP_201_CREATED,
    summary="Create a user",
)
async def create_user(
    payload: dict[str, Any] = Body(
        ...,
        example={
            "name": "Aditya Raj",
            "email": "aditya@example.com",
            "phone": "9876543210",
            "status": "active",
        },
    ),
):
    global _next_user_id

    cleaned = _validate_user_payload(payload)
    _ensure_email_is_unique(cleaned["email"])

    new_user = {
        "id": _next_user_id,
        "name": cleaned["name"],
        "email": cleaned["email"],
        "phone": cleaned.get("phone"),
        "status": cleaned.get("status", "active"),
    }
    users[_next_user_id] = new_user
    _next_user_id += 1

    return {"message": "User created successfully.", "data": new_user}


@router.get("/all_users", summary="Get all users")
async def get_users():
    user_list = list(users.values())
    return {
        "message": "Users fetched successfully.",
        "total_users": len(user_list),
        "data": user_list,
    }


@router.get("/fetch/user/{user_id}", summary="Get a user by ID")
async def get_user(user_id: int):
    return {
        "message": "User fetched successfully.",
        "data": _get_user_or_404(user_id),
    }


@router.put(
    "/user/{user_id}",
    summary="Replace a user's details",
)
async def update_user(
    user_id: int,
    payload: dict[str, Any] = Body(
        ...,
        example={
            "name": "Aditya Rajput",
            "email": "aditya.updated@example.com",
            "phone": "9876543210",
            "status": "active",
        },
    ),
):
    existing_user = _get_user_or_404(user_id)
    cleaned = _validate_user_payload(payload)
    _ensure_email_is_unique(cleaned["email"], exclude_user_id=user_id)

    updated_user = {
        "id": user_id,
        "name": cleaned["name"],
        "email": cleaned["email"],
        "phone": cleaned.get("phone"),
        "status": cleaned.get("status", "active"),
    }
    users[user_id] = updated_user

    return {"message": "User updated successfully.", "data": updated_user}


@router.delete(
    "/user/{user_id}",
    summary="Delete a user",
)
async def delete_user(user_id: int):
    _get_user_or_404(user_id)
    del users[user_id]
    return {"message": "User deleted successfully.", "user_id": user_id}
