from sqlalchemy import Column, Integer, String
from database import Base

class Sede(Base):
    __tablename__ = "sede"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    direccion = Column(String, nullable=False)
    telefono = Column(String, nullable=False)