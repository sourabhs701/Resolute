# app/main.py
from fastapi import FastAPI
from app.api.v1.endpoints.auth import auth_router
from mangum import Mangum

app = FastAPI(
    title="FastAPI MongoDB Authentication",
    description="Basic FastAPI app with MongoDB Atlas for authentication",
    version="1.0.0"
)

handler = Mangum(app)

app.include_router(auth_router, prefix="/auth")

@app.get("/")
async def hello():
    return {
        "message": "Hello, World!",
        "documentation": "/docs or /redoc"
    }
