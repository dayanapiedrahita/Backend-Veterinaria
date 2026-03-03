from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Vacuna(Base):
    __tablename__ = "vacuna"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    fabricante = Column(String)
    dosis_requeridas = Column(Integer, nullable=False)

    citas = relationship("CitaVacunacion", back_populates="vacuna")