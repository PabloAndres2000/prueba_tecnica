import time
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()
logger = logging.getLogger(__name__)

DATABASE_URL = os.getenv("DATABASE_URL",)

def wait_for_db_connection():
    retries = 5
    delay = 5  
    while retries > 0:
        try:
            engine = create_engine(DATABASE_URL)
            with engine.connect():
                logger.info("Conexión a la base de datos exitosa")
                return engine
        except SQLAlchemyError as e:
            logger.warning(f"Conexión fallida. Intentando nuevamente en {delay} segundos... ({retries} intentos restantes)")
            time.sleep(delay)
            retries -= 1
    raise Exception("No se pudo conectar a la base de datos después de varios intentos.")

engine = wait_for_db_connection()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    except SQLAlchemyError as e:
        db.rollback()  
        logging.error(f"Error de base de datos: {e}")  
        raise
    finally:
        try:
            db.close()  
        except Exception as e:
            logging.error(f"Error al cerrar la sesión: {e}")
