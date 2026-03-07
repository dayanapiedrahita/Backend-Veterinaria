from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base



class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True)
    rol = Column(String, nullable=False)  # "cliente" o "veterinario"

    cliente_id = Column(Integer, ForeignKey("cliente.id"), nullable=True)
    veterinario_id = Column(Integer, ForeignKey("veterinario.id"), nullable=True)



    