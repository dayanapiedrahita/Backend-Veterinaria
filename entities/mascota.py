from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Mascota(Base):
    __tablename__ = "mascota"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    especie = Column(String)
    raza = Column(String)
    cliente_id = Column(Integer, ForeignKey("cliente.id"))

    cliente = relationship("Cliente")