from sqlalchemy import Column, String, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Holiday(Base):
    __tablename__ = "holidays"

    fecha = Column(Date, primary_key=True)
    nombreFeriado = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    descripcion = Column(String, nullable=True)
    dia_semana = Column(String, nullable=False)
