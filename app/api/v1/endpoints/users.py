# app/api/v1/endpoints/users.py
from fastapi import APIRouter, Depends, HTTPException
from app.db.database import users_collection
from app.models.user import UserCreate, UserResponse
from app.core.security import get_password_hash

users_router = APIRouter()

@users_router.post("/users", response_model=UserResponse)
async def create_user(user: UserCreate):
    if users_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="User already exists")
    user_data = user.dict()
    user_data["hashed_password"] = get_password_hash(user.password)
    del user_data["password"]
    users_collection.insert_one(user_data)
    return UserResponse(email=user.email, id=str(user_data["_id"]))
