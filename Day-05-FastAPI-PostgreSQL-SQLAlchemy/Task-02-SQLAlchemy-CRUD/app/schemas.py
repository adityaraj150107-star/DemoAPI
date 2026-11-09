from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, EmailStr, Field, model_validator


TaskStatus = Literal["pending", "in progress", "done"]


class RegisterRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)
    age: int | None = Field(default=None, ge=0, le=120)

    @model_validator(mode="before")
    @classmethod
    def normalize_email(cls, value):
        if isinstance(value, dict) and isinstance(value.get("email"), str):
            normalized = {**value, "email": value["email"].strip().lower()}
            if isinstance(value.get("name"), str):
                normalized["name"] = value["name"].strip()
            value = normalized
        return value


class LoginRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    email: EmailStr
    password: str = Field(min_length=1, max_length=128)

    @model_validator(mode="before")
    @classmethod
    def normalize_email(cls, value):
        if isinstance(value, dict) and isinstance(value.get("email"), str):
            value = {**value, "email": value["email"].strip().lower()}
        return value


class RefreshRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    refresh_token: str = Field(min_length=1)


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: EmailStr
    age: int | None
    is_active: bool
    role: Literal["teacher", "student"]
    created_at: datetime


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: Literal["bearer"] = "bearer"
    expires_in: int
    user: UserResponse


class TaskCreate(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    title: str = Field(min_length=1, max_length=200)
    description: str | None = Field(default=None, max_length=2000)
    assigned_to: int | None = Field(default=None, gt=0)


class TaskUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    title: str | None = Field(default=None, min_length=1, max_length=200)
    description: str | None = Field(default=None, max_length=2000)
    status: TaskStatus | None = None
    assigned_to: int | None = Field(default=None, gt=0)
    work_notes: str | None = Field(default=None, max_length=4000)

    @model_validator(mode="after")
    def require_changes(self):
        if not self.model_fields_set:
            raise ValueError("At least one task field must be provided.")
        return self


class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str | None
    status: TaskStatus
    assigned_to: int | None
    assigned_by: int
    work_notes: str | None
    created_at: datetime
    updated_at: datetime
