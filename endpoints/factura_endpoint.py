from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from database import get_db
# Asumiendo que existe la entidad Factura, si no, se usa el nombre de la tabla
from entities.factura import Factura 

router = APIRouter()

@router.get("/")
def get_facturas(db: Session = Depends(get_db)):
    return db.query(Factura).all()

@router.get("/total-costos")
def get_total_costos(db: Session = Depends(get_db)):
    # Sumamos la columna 'costo' de la tabla factura
    total = db.query(func.sum(Factura.costo)).scalar() or 0
    return {"total_costos": total}