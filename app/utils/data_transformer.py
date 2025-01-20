from datetime import datetime
from typing import List, Dict
from app.config.logs import setup_logging
logger = setup_logging()

def transform_holiday_data(holidays_data: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Transforma los datos de los feriados obtenidos de la API al formato requerido por el modelo 'Holiday'.

    Esta función recibe una lista de diccionarios con los datos de los feriados obtenidos desde la API, 
    valida y transforma la informacion en un formato compatible para los atributos del modelo. Si alguno de los 
    campos requeridos ('nombre', 'fecha', 'tipo') falta o la fecha es inválida, se registra un error 
    y el feriado se omite. El resultado es una lista de diccionarios con los datos transformados.

    Args:
        holidays_data (List[Dict[str, str]]): Lista de diccionarios con los datos de los feriados obtenidos de la API.

    Returns:
        List[Dict[str, str]]: Lista de diccionarios con los feriados transformados al formato adecuado para la base de datos.
    """
    transformed = []
    for holiday in holidays_data:

        nombre = holiday.get('nombre')
        fecha = holiday.get('fecha')
        tipo = holiday.get('tipo')
        descripcion = holiday.get('comentarios') or nombre

        if not all([nombre, fecha, tipo]):
            logger.error(f"Feriado invalido: {holiday}")
            continue

        try:
            fecha_formateada = datetime.strptime(fecha, "%Y-%m-%d").strftime("%d-%m-%Y")
            dia_semana = datetime.strptime(fecha, "%Y-%m-%d").strftime("%A")
        except ValueError as e:
            logger.error(f"Error formateando la fecha {fecha}: {e}")
            continue

        transformed.append({
            'nombreFeriado': nombre,
            'fecha': fecha_formateada,
            'tipo': tipo,
            'descripcion': descripcion,
            'dia_semana': dia_semana
        })
    return transformed
