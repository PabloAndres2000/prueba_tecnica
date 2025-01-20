from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.holiday import HolidayService
from app.repositories.holiday import HolidayRepository
from app.config.database import get_db
from app.utils.exceptions import HolidayException
from app.schemas.swagger_response import HolidayResponse

router = APIRouter()

from datetime import datetime as dt
from fastapi import HTTPException

@router.get("/holiday/{date}", response_model=HolidayResponse)
def check_exist_holiday_by_date(
    date: str, 
    db: Session = Depends(get_db)
):
    """
    Obtiene un feriado por fecha.

    Este Endpoint recibe una fecha como parametro de ruta en formato 'yyyy-mm-dd' y verifica si existe un feriado para esa fecha en el año 2024. 
    Si se encuentra un feriado, devuelve la información del mismo en el formato requerido. Si la fecha es invalida o 
    no corresponde a un feriado, se retorna excepciones.

    Args:
        date (str): La fecha en formato 'yyyy-mm-dd' para la cual se desea obtener el feriado.
        db (Session, optional): Sesion de la base de datos, proporcionada por FastAPI mediante Depends.

    Raises:
        HTTPException: Si la fecha no tiene el formato válido, no corresponde al año 2024, o no se encuentra un feriado para la fecha dada.

    Returns:
        dict: Un diccionario con la información del feriado correspondiente, que incluye:
            - 'nombreFeriado': El nombre del feriado.
            - 'fecha': La fecha del feriado en formato 'dd-mm-yyyy'.
            - 'tipo': El tipo de feriado (ej. "nacional").
            - 'descripcion': Una descripción del feriado.
            - 'dia_semana': El día de la semana en que cae el feriado.
    """
    holiday_repo = HolidayRepository()
    
    try:
        input_date = dt.strptime(date, "%Y-%m-%d").date()
        if input_date.year != 2024:
            raise HTTPException(status_code=400, detail="Solo se pueden consultar feriados del año 2024")
        
        holiday = holiday_repo.filter_holiday_by_date(db, date)
        
        if holiday:
            return {
                "nombreFeriado": holiday.nombreFeriado,
                "fecha": holiday.fecha.strftime("%d-%m-%Y"),
                "tipo": holiday.tipo,
                "descripcion": holiday.descripcion,
                "dia_semana": holiday.dia_semana
            }
        else:
            raise HTTPException(status_code=404, detail=f"No se encontro un feriado para la fecha {date}")
    
    except ValueError:
        raise HTTPException(status_code=400, detail="La fecha proporcionada no tiene el formato valido 'yyyy-mm-dd'.")
