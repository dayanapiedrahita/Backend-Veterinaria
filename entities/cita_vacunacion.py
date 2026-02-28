from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base

class CitaVacunacion(Base):
    __tablename__ = "cita_vacunacion"

    id = Column(Integer, primary_key=True, index=True)
    mascota_id = Column(Integer, ForeignKey("mascota.id"))
    vacuna_id = Column(Integer, ForeignKey("vacuna.id"))
    fecha = Column(DateTime, nullable=False)

    mascota = relationship("Mascota")
    vacuna = relationship("Vacuna")