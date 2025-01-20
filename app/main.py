from fastapi import FastAPI, Depends
from app.config.database import get_db, engine
from app.config.logs import setup_logging
from app.models.holiday import Holiday
from app.routers import api_router
from app.services.holiday import HolidayService
from app.repositories.holiday import HolidayRepository
import threading

setup_logging()

Holiday.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_router)

@app.on_event("startup")
async def on_startup():
    db = next(get_db())
    holiday_repo = HolidayRepository()
    holiday_service = HolidayService(holiday_repo, db)
    
    thread = threading.Thread(target=holiday_service.run_periodically)
    thread.daemon = True 
    thread.start()