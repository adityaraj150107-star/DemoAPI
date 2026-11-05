from fastapi import APIRouter, HTTPException, status
from model.user import (
    UserCreate,
    UserUpdate,
    UserResponse,
    UsersListResponse,
    MessageResponse
)

router = APIRouter(
    prefix="/api/v2",
    tags=["Users"]
)


# Temporary in-memory database
users_db: dict[int, dict] = {}

# Auto increment ID
user_id_counter = 1


# -----------------------------------------
# 1. CREATE USER (POST)
# -----------------------------------------

@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_user(user: UserCreate):

    global user_id_counter

    # Check duplicate email
    for existing_user in users_db.values():

        if existing_user["email"] == user.email:

            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail={
                    "code": "EMAIL_ALREADY_EXISTS",
                    "message": "This email is already registered"
                }
            )

    # Create new user
    new_user = {
        "id": user_id_counter,
        **user.model_dump()
    }

    # Save user
    users_db[user_id_counter] = new_user

    user_id_counter += 1

    return new_user


# -----------------------------------------
# 2. GET ALL USERS (GET)
# -----------------------------------------

@router.get(
    "/",
    response_model=UsersListResponse
)
async def get_users():

    return {
        "message": "Users fetched successfully",
        "total_users": len(users_db),
        "data": list(users_db.values())
    }


# -----------------------------------------
# 3. GET USER BY ID (GET)
# -----------------------------------------

@router.get(
    "/{user_id}",
    response_model=UserResponse
)
async def get_user(user_id: int):

    user = users_db.get(user_id)

    if user is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "code": "USER_NOT_FOUND",
                "message": f"User with ID {user_id} does not exist"
            }
        )

    return user


# -----------------------------------------
# 4. UPDATE USER (PUT)
# -----------------------------------------

@router.put(
    "/{user_id}",
    response_model=UserResponse
)
async def update_user(
    user_id: int,
    user_data: UserCreate
):

    # Check user exists
    existing_user = users_db.get(user_id)

    if existing_user is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "code": "USER_NOT_FOUND",
                "message": f"User with ID {user_id} does not exist"
            }
        )

    # Check duplicate email
    for existing_id, user in users_db.items():

        if (
            existing_id != user_id
            and user["email"] == user_data.email
        ):

            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail={
                    "code": "EMAIL_ALREADY_EXISTS",
                    "message": "This email is already registered"
                }
            )

    # Update all fields
    updated_user = {
        "id": user_id,
        **user_data.model_dump()
    }

    users_db[user_id] = updated_user

    return updated_user


# -----------------------------------------
# 5. PARTIAL UPDATE USER (PATCH)
# -----------------------------------------

@router.patch(
    "/{user_id}",
    response_model=UserResponse
)
async def patch_user(
    user_id: int,
    user_data: UserUpdate
):

    existing_user = users_db.get(user_id)

    if existing_user is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "code": "USER_NOT_FOUND",
                "message": f"User with ID {user_id} does not exist"
            }
        )

    # Only update fields sent by client
    update_data = user_data.model_dump(
        exclude_unset=True
    )

    # Check duplicate email if email is updated
    if "email" in update_data:

        for existing_id, user in users_db.items():

            if (
                existing_id != user_id
                and user["email"] == update_data["email"]
            ):

                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail={
                        "code": "EMAIL_ALREADY_EXISTS",
                        "message": "This email is already registered"
                    }
                )

    # Update user
    existing_user.update(update_data)

    return existing_user


# -----------------------------------------
# 6. DELETE USER (DELETE)
# -----------------------------------------

@router.delete(
    "/{user_id}",
    response_model=MessageResponse
)
async def delete_user(user_id: int):

    # Check user exists
    if user_id not in users_db:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "code": "USER_NOT_FOUND",
                "message": f"User with ID {user_id} does not exist"
            }
        )

    # Delete user
    del users_db[user_id]

    return {
        "message": "User deleted successfully"
    }
