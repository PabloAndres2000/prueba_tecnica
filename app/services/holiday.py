import time
from sqlalchemy.orm import Session
from app.utils.api_client import get_holidays
from app.utils.data_transformer import transform_holiday_data
from app.repositories.holiday import HolidayRepository
from app.config.logs import setup_logging

class HolidayService:
    def __init__(self, holiday_repo: HolidayRepository, db: Session):
        self.holiday_repo = holiday_repo
        self.db = db
        self.logger = setup_logging()

    def fetch_and_store_holidays(self):
        """
        Obtiene los feriados de la API consumida y los guarda en la base de datos.

        Realiza una llamada a la API para obtener los datos de los feriados, luego transforma los datos 
        y verifica si cada feriado ya está registrado en la base de datos. Si no está registrado, lo agrega.
        Si ya existe, se registra un mensaje indicando que el feriado ya está presente.

        Utiliza los metodos de la clase 'HolidayRepository' para verificar la existencia y agregar los feriados.
        """
        holidays_data = get_holidays()
        if holidays_data:
            transformed_data = transform_holiday_data(holidays_data)
            for holiday in transformed_data:
                existing_holiday = self.holiday_repo.check_exist_holiday_by_date(self.db, holiday['fecha'])
                if not existing_holiday:
                    new_holiday = self.holiday_repo.add_holiday(self.db, holiday)
                    self.logger.info(f"Feriado agregado: {new_holiday.nombreFeriado}")
                else:
                    self.logger.info(f"Feriado ya existe: {holiday['nombreFeriado']}")

        else:
            self.logger.error("No se pudieron obtener los feriados.")



    def run_periodically(self):
        """
        Ejecuta la consulta periódica para obtener y almacenar los feriados.

        Ejecuta en un ciclo infinito, llamando al método `fetch_and_store_holidays()` 
        para obtener y almacenar los feriados a intervalos regulares. Después de cada ejecución, 
        espera 60 segundos antes de realizar la siguiente consulta.

        El propósito de este metodo es garantizar que los feriados se obtengan y almacenen de forma periódica.
        """
        while True:
            self.fetch_and_store_holidays()
            time.sleep(60)  