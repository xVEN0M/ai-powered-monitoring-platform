from fastapi import FastAPI

from database.database import engine
from database.base import Base
from models.user import User
from auth.auth_routes import router as auth_router
from routes.user_routes import router as user_router
from models.device import Device
from routes.device_routes import router as device_router
from routes.scan_routes import router as scan_router

Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="AI-Powered Enterprise Network Security & Monitoring Platform"
)
app.include_router(device_router)
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(scan_router)

@app.get("/")
def home():
    return {
        "message": "Backend is working successfully!"
    }

@app.get("/health")
def health():
    return {
        "status": "Running",
        "backend": "Healthy",
        "version": "1.0.0"
    }