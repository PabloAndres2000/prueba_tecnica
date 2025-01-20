from pydantic import BaseModel

class HolidayResponse(BaseModel):
    nombreFeriado: str
    fecha: str
    tipo: str
    descripcion: str = ''
    dia_semana: str

    class Config:
        schema_extra = {
            "example": {
                "nombreFeriado": "Año Nuevo",
                "fecha": "01-01-2024",
                "tipo": "Civil",
                "descripcion": "Año Nuevo",
                "dia_semana": "Lunes"
            }
        }
        from_attributes = True