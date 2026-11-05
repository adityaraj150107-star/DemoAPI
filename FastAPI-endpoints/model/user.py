from pydantic import BaseModel, Field, EmailStr, ConfigDict
from typing import Optional


# Common configuration
class UserBase(BaseModel):

    name: str = Field(
        ...,
        min_length=2,
        max_length=50,
        description="Name must contain 2 to 50 characters"
    )

    email: EmailStr = Field(
        ...,
        description="Enter a valid email address"
    )

    age: int = Field(
        ...,
        ge=18,
        le=100,
        description="Age must be between 18 and 100"
    )

    phone: Optional[str] = Field(
        default=None,
        min_length=10,
        max_length=15
    )

    is_active: bool = Field(
        default=True,
        description="User account active status"
    )


# CREATE USER REQUEST
class UserCreate(UserBase):
    pass


# UPDATE USER REQUEST
class UserUpdate(BaseModel):

    name: Optional[str] = Field(
        default=None,
        min_length=2,
        max_length=50
    )

    email: Optional[EmailStr] = None

    age: Optional[int] = Field(
        default=None,
        ge=18,
        le=100
    )

    phone: Optional[str] = Field(
        default=None,
        min_length=10,
        max_length=15
    )

    is_active: Optional[bool] = None


# USER RESPONSE
class UserResponse(UserBase):

    id: int

    model_config = ConfigDict(from_attributes=True)


# LIST USERS RESPONSE
class UsersListResponse(BaseModel):

    message: str
    total_users: int
    data: list[UserResponse]


# GENERAL MESSAGE RESPONSE
class MessageResponse(BaseModel):

    message: str
