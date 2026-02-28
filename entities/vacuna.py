from sqlalchemy import Column, Integer, String
from database import Base

class Vacuna(Base):
    __tablename__ = "vacuna"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    fabricante = Column(String)