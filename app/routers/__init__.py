from fastapi import APIRouter
from app.routers.holiday import router  as holiday_router

api_router = APIRouter(prefix="/api")

api_router.include_router(holiday_router)
