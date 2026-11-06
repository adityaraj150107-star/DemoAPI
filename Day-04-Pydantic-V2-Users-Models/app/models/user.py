"""Pydantic v2 request and response schemas for the Users API."""
from pydantic import BaseModel, ConfigDict, EmailStr, Field, model_validator


class UserBase(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str = Field(..., min_length=2, max_length=50, description="User's full name")
    email: EmailStr = Field(..., description="A valid email address")
    age: int = Field(..., ge=18, le=100, description="Age must be between 18 and 100")
    phone: str | None = Field(default=None, min_length=10, max_length=15)
    is_active: bool = Field(default=True, description="Whether the account is active")


class UserCreate(UserBase):
    """Request schema for creating a user."""


class UserUpdate(BaseModel):
    """Request schema for partial updates; omitted fields remain unchanged."""

    model_config = ConfigDict(extra="forbid")

    name: str | None = Field(default=None, min_length=2, max_length=50)
    email: EmailStr | None = None
    age: int | None = Field(default=None, ge=18, le=100)
    phone: str | None = Field(default=None, min_length=10, max_length=15)
    is_active: bool | None = None

    @model_validator(mode="after")
    def reject_null_for_non_nullable_fields(self):
        # Optional means a field may be omitted, not set to null.
        # Phone is the only field that is nullable in the user model.
        for field_name in self.model_fields_set:
            if field_name != "phone" and getattr(self, field_name) is None:
                raise ValueError(f"{field_name} cannot be null.")
        return self


class UserResponse(UserBase):
    id: int


class UsersListResponse(BaseModel):
    message: str
    total_users: int
    data: list[UserResponse]


class MessageResponse(BaseModel):
    message: str
