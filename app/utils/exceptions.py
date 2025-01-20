class HolidayAPIException(Exception):
    """Excepción para errores relacionados con la API de feriados."""
    def __init__(self, message: str):
        super().__init__(message)

class HolidayException(Exception):
    """Excepción para errores al almacenar los feriados en la base de datos."""
    def __init__(self, message: str):
        super().__init__(message)
