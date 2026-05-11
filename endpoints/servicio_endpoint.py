from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from database import get_db
from entities.servicio import Servicio
from entities.cita_vacunacion import CitaVacunacion

router = APIRouter()

@router.get("/")
def get_servicios(db: Session = Depends(get_db)):
    return db.query(Servicio).all()

@router.get("/estadisticas/uso")
def get_servicios_estadisticas(db: Session = Depends(get_db)):
    # Agrupamos citas por servicio y contamos
    resultados = db.query(
        Servicio.nombre.label("nombre_servicio"),
        func.count(CitaVacunacion.id).label("total_citas")
    ).join(CitaVacunacion, Servicio.id == CitaVacunacion.servicio_id).group_by(Servicio.nombre).all()
    
    return resultados