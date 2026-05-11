from sqlalchemy import Column, Integer, DateTime, Float, ForeignKey, Boolean
from sqlalchemy.sql import func
from database import Base

class Factura(Base):
    __tablename__ = "factura"

    id = Column(Integer, primary_key=True, index=True)
    id_cita = Column(Integer, ForeignKey("cita_vacunacion.id"), nullable=False)
    id_usuario_pago = Column(Integer, nullable=True)
    costo = Column(Float, nullable=False)
    fecha_generacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_pago = Column(DateTime(timezone=True), nullable=True)
    pagada = Column(Boolean, default=False)