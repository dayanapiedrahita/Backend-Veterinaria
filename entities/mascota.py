from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from database import Base

class Mascota(Base):
    __tablename__ = "mascota"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    especie = Column(String)
    raza = Column(String)
    fecha_nacimiento = Column(Date)

    cliente_id = Column(Integer, ForeignKey("cliente.id"), nullable=False)

    cliente = relationship("Cliente", back_populates="mascotas")
    citas = relationship("CitaVacunacion", back_populates="mascota", cascade="all, delete")