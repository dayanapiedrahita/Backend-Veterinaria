from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Veterinario(Base):
    __tablename__ = "veterinario"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    especialidad = Column(String)
    sede_id = Column(Integer, ForeignKey("sede.id"))

    sede = relationship("Sede")