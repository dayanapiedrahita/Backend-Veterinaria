from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.vacuna_schema import VacunaCreate, VacunaUpdate, VacunaResponse
from crud.vacuna_crud import get_vacunas, get_vacuna, create_vacuna, update_vacuna, delete_vacuna
from entities.vacuna import Vacuna

router = APIRouter(prefix="/vacuna", tags=["Vacuna"])

@router.get("/", response_model=list[VacunaResponse])
def listar_vacunas(db: Session = Depends(get_db)):
    return get_vacunas(db)

@router.get("/{vacuna_id}", response_model=VacunaResponse)
def obtener_vacuna(vacuna_id: int, db: Session = Depends(get_db)):
    vacuna = get_vacuna(db, vacuna_id)
    if not vacuna:
        raise HTTPException(status_code=404, detail="Vacuna no encontrada")
    return vacuna

@router.post("/", response_model=VacunaResponse)
def crear_vacuna(vacuna: VacunaCreate, db: Session = Depends(get_db)):
    return create_vacuna(db, vacuna)

@router.put("/{vacuna_id}", response_model=VacunaResponse)
def actualizar_vacuna(vacuna_id: int, vacuna: VacunaUpdate, db: Session = Depends(get_db)):
    updated = update_vacuna(db, vacuna_id, vacuna)
    if not updated:
        raise HTTPException(status_code=404, detail="Vacuna no encontrada")
    return updated

@router.delete("/{vacuna_id}", response_model=VacunaResponse)
def eliminar_vacuna(vacuna_id: int, db: Session = Depends(get_db)):
    deleted = delete_vacuna(db, vacuna_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Vacuna no encontrada")
    return deleted