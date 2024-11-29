# app/auth.py
from fastapi import APIRouter, Depends, HTTPException, Header
from fastapi.security import OAuth2PasswordBearer
from app.core.security import verify_token
from app.models.user import User, Token
from app.db.database import users_collection
from app.core.security import verify_password, get_password_hash, create_access_token

auth_router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

@auth_router.post("/register")
async def register(user: User):
    if users_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="User already exists")
    hashed_password = get_password_hash(user.password)
    user_data = {"email": user.email, "hashed_password": hashed_password}
    users_collection.insert_one(user_data)
    return {"message": "User registered successfully"}

@auth_router.post("/login", response_model=Token)
async def login(user: User):
    db_user = users_collection.find_one({"email": user.email})
    if not db_user or not verify_password(user.password, db_user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@auth_router.get("/verify")
async def protected_route(username: str = Depends(verify_token)):
    return {"message": f"Welcome, {username}!"}
