from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from database import get_db
from entities.mascota import Mascota

router = APIRouter()

@router.get("/")
async def get_razas_animal():
    # Datos básicos para que el selector de razas en Animales funcione
    return [
        {"id": 1, "nombre": "Labrador"},
        {"id": 2, "nombre": "Bulldog"},
        {"id": 3, "nombre": "Persa"},
        {"id": 4, "nombre": "Siamés"},
        {"id": 5, "nombre": "Criollo"}
    ]

@router.get("/estadisticas/populares")
def get_razas_populares(db: Session = Depends(get_db)):
    """Retorna las razas más populares con conteo de mascotas"""
    try:
        resultados = db.query(
            Mascota.raza.label("nombre_raza"),
            func.count(Mascota.id).label("total_animales")
        ).group_by(Mascota.raza).order_by(func.count(Mascota.id).desc()).all()
        
        return [
            {"raza": r.nombre_raza, "cantidad": r.total_animales} 
            for r in resultados if r.nombre_raza
        ]
    except Exception as e:
        return {"error": str(e)}

@router.get("/estadisticas/uso")
def get_razas_estadisticas(db: Session = Depends(get_db)):
    """Retorna estadísticas de uso de razas (compatibilidad)"""
    try:
        resultados = db.query(
            Mascota.raza.label("nombre_raza"),
            func.count(Mascota.id).label("total_animales")
        ).group_by(Mascota.raza).all()
        
        return [
            {"raza": r.nombre_raza, "cantidad": r.total_animales} 
            for r in resultados if r.nombre_raza
        ]
    except Exception as e:
        return {"error": str(e)}