from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Veterinario(Base):
    __tablename__ = "veterinario"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    especialidad = Column(String)

    sede_id = Column(Integer, ForeignKey("sede.id"), nullable=False)

    sede = relationship("Sede", back_populates="veterinarios")
    citas = relationship("CitaVacunacion", back_populates="veterinario")
    usuario = relationship("Usuario", back_populates="veterinario", uselist=False)