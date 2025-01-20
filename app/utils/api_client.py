import time
import requests
from app.config.logs import setup_logging

logger = setup_logging()

HOLIDAYS_URL = "https://apis.digital.gob.cl/fl/feriados/2024"
MAX_RETRIES = 3  
RETRY_DELAY = 5 

def get_holidays():
    """
    Obtiene los feriados desde la API de feriados de Chile.

    Esta funcion realiza solicitudes HTTP a la API de feriados y maneja errores en caso de fallos de red 
    o problemas de la API. Si la respuesta es exitosa, retorna los datos en formato JSON, 
    en caso contrario, reintenta hasta un máximo de 'MAX_RETRIES' veces.

    El logger registra los intentos, los errores, y el exito de la operacion. Si no se puede obtener 
    la información despues de los intentos, retorna 'None'.

    Returns:
        dict | None: Datos de los feriados en formato JSON si la solicitud fue exitosa, 
        o 'None' si hubo un error tras los intentos.
    """
    for attempt in range(MAX_RETRIES):
        try:
                        
            headers = {
                "User-Agent": "StoreProject/1.0",
            }
            response = requests.get(HOLIDAYS_URL, headers=headers, timeout=10)
            response.raise_for_status()

            if response.status_code == 200:
                logger.info("Feriados obtenidos exitosamente.")
                return response.json() 
            else:
                logger.error(f"Error de la API {response.status_code}")
                return None
        except requests.exceptions.Timeout:
            logger.error(f"Intento {attempt + 1}: El tiempo de espera de la solicitud se agoto.")
        except requests.exceptions.RequestException as e:
            logger.error(f"Intento {attempt + 1}: Error al obtener los feriados: {e}")

        logger.warning(f"Esperando {RETRY_DELAY} segundos antes de intentar nuevamente...")
        time.sleep(RETRY_DELAY)
    
    return None
