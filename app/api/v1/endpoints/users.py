from fastapi import APIRouter, Body, HTTPException
import asyncio

router = APIRouter(prefix="/api/v1", tags=["Users"])

# Temporary in-memory storage. Data resets when the app/container restarts.
users = []
user_id_counter = 1


@router.post("/users", status_code=201)
async def create_user(
    user: dict = Body(
        ...,
        example={
            "name": "Aditya Raj",
            "email": "aditya@gmail.com",
            "phone": "9876543210",
            "status": "active"
        }
    )
):
    global user_id_counter
    await asyncio.sleep(0)

    if not user.get("name") or not user.get("email"):
        raise HTTPException(status_code=400, detail="Name and email are required")

    if any(existing["email"] == user["email"] for existing in users):
        raise HTTPException(status_code=409, detail="Email already exists")

    new_user = {
        "id": user_id_counter,
        "name": user["name"],
        "email": user["email"],
        "phone": user.get("phone"),
        "status": user.get("status", "active")
    }
    users.append(new_user)
    user_id_counter += 1
    return {"message": "User created successfully", "data": new_user}


@router.get("/all_users")
async def get_users():
    await asyncio.sleep(0)
    return {
        "message": "Users fetched successfully",
        "total_users": len(users),
        "data": users
    }


@router.get("/fetch/user/{user_id}")
async def get_user(user_id: int):
    await asyncio.sleep(0)
    for user in users:
        if user["id"] == user_id:
            return {"message": "User fetched successfully", "data": user}
    raise HTTPException(status_code=404, detail="User not found")


@router.put("/user/{user_id}")
async def update_user(
    user_id: int,
    user_data: dict = Body(
        ...,
        example={
            "name": "Aditya Raj Updated",
            "email": "aditya.updated@gmail.com",
            "phone": "9876543210",
            "status": "active"
        }
    )
):
    await asyncio.sleep(0)
    for user in users:
        if user["id"] == user_id:
            new_email = user_data.get("email", user["email"])
            if any(existing["id"] != user_id and existing["email"] == new_email for existing in users):
                raise HTTPException(status_code=409, detail="Email already exists")

            user["name"] = user_data.get("name", user["name"])
            user["email"] = new_email
            user["phone"] = user_data.get("phone", user["phone"])
            user["status"] = user_data.get("status", user["status"])
            return {"message": "User updated successfully", "data": user}
    raise HTTPException(status_code=404, detail="User not found")


@router.delete("/user/{user_id}")
async def delete_user(user_id: int):
    await asyncio.sleep(0)
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")
