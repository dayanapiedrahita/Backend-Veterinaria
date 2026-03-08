from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.sede_schema import SedeCreate, SedeUpdate, SedeResponse
from crud.sede_crud import get_sedes, get_sede, create_sede, update_sede, delete_sede
from entities.sede import Sede

router = APIRouter(prefix="/sedes", tags=["Sedes"])

@router.get("/", response_model=list[SedeResponse])
def listar_sedes(db: Session = Depends(get_db)):
    return get_sedes(db)

@router.get("/{sede_id}", response_model=SedeResponse)
def obtener_sede(sede_id: int, db: Session = Depends(get_db)):
    sede = get_sede(db, sede_id)
    if not sede:
        raise HTTPException(status_code=404, detail="Sede no encontrada")
    return sede

@router.post("/", response_model=SedeResponse)
def crear_sede(sede: SedeCreate, db: Session = Depends(get_db)):
    return create_sede(db, sede)

@router.put("/{sede_id}", response_model=SedeResponse)
def actualizar_sede(sede_id: int, sede: SedeUpdate, db: Session = Depends(get_db)):
    updated = update_sede(db, sede_id, sede)
    if not updated:
        raise HTTPException(status_code=404, detail="Sede no encontrada")
    return updated

@router.delete("/{sede_id}", response_model=SedeResponse)
def eliminar_sede(sede_id: int, db: Session = Depends(get_db)):
    deleted = delete_sede(db, sede_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Sede no encontrada")
    return deleted