import logging
import os

def setup_logging():
    # Crear la carpeta para el archivo de logs si no existe
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Configuración básica del logging
    logger = logging.getLogger()
    if not logger.hasHandlers():  # Verifica si el logger ya tiene handlers
        # Configurar el nivel y formato
        logging.basicConfig(
            level=logging.DEBUG,  # Cambié el nivel a DEBUG para capturar todos los logs
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.StreamHandler(),  # Para ver los logs en la consola
                logging.FileHandler(f"{log_dir}/app.log")  # Para escribir los logs en el archivo
            ]
        )
    return logger

setup_logging()
