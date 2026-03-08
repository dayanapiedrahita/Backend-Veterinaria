from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Cliente(Base):
    __tablename__ = "cliente"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    telefono = Column(String)
    direccion = Column(String)
    email = Column(String, unique=True)

    mascotas = relationship("Mascota", back_populates="cliente")
    usuario = relationship("Usuario", back_populates="cliente", uselist=False)