from sqlalchemy.orm import Session
from app.models.holiday import Holiday
from app.utils.exceptions import HolidayException
from datetime import datetime as dt

class HolidayRepository:

    @staticmethod
    def check_exist_holiday_by_date(db: Session, date: str) -> bool:
        """
        Verifica si existe un feriado para la fecha dada.

        Args:
            db (Session): La sesión de la base de datos para realizar la consulta.
            date (str): La fecha del feriado a verificar en formato "dd-mm-yyyy".

        Returns:
            bool: True si existe un feriado para la fecha, de lo contrario False.
        """
        date_convert = dt.strptime(date, "%d-%m-%Y").date()
        holiday = db.query(Holiday).filter(Holiday.fecha == date_convert).first()
        return holiday is not None
    
    @staticmethod
    def add_holiday(db: Session, holiday_data: dict):
        """
        Agrega un feriado a la base de datos.

        Args:
            db (Session): La sesión de la base de datos para agregar el feriado.
            holiday_data (dict): Los datos del feriado, incluyendo 'fecha', 'nombreFeriado', 'tipo', 
                                 'descripcion' (opcional), y 'dia_semana'.

        Returns:
            Holiday: El objeto de feriado agregado a la base de datos.
        """
        holiday_data['fecha'] = dt.strptime(holiday_data['fecha'], "%d-%m-%Y").date()
        
        holiday = Holiday(
            fecha=holiday_data['fecha'],
            nombreFeriado=holiday_data['nombreFeriado'],
            tipo=holiday_data['tipo'],
            descripcion=holiday_data.get('descripcion', ''),
            dia_semana=holiday_data['dia_semana']
        )

        db.add(holiday)
        db.commit()
        db.refresh(holiday)
        return holiday
    
    @staticmethod
    def filter_holiday_by_date(db: Session, date: str):
        """
        Obtiene un feriado por fecha.

        Args:
            db (Session): La sesión de la base de datos para realizar la consulta.
            date (str): La fecha del feriado en formato "yyyy-mm-dd".

        Returns:
            Optional[Holiday]: El objeto de feriado si existe, de lo contrario None.
        """
        date_convert = dt.strptime(date, "%Y-%m-%d").date()
        return db.query(Holiday).filter(Holiday.fecha == date_convert).first()
