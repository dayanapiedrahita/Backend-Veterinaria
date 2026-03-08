from sqlalchemy import Column, Integer, ForeignKey, DateTime, Boolean, String
from sqlalchemy.orm import relationship
from database import Base

class CitaVacunacion(Base):
    __tablename__ = "cita_vacunacion"

    id = Column(Integer, primary_key=True, index=True)
    
    fecha = Column(DateTime, nullable=False)
    estado = Column(String, nullable=False, default="programada")
 

    mascota_id = Column(Integer, ForeignKey("mascota.id"), nullable=False)
    vacuna_id = Column(Integer, ForeignKey("vacuna.id"), nullable=False)
    veterinario_id = Column(Integer, ForeignKey("veterinario.id"), nullable=False)

    mascota = relationship("Mascota", back_populates="citas")
    vacuna = relationship("Vacuna", back_populates="citas")
    veterinario = relationship("Veterinario", back_populates="citas")