from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.veterinario_schema import VeterinarioCreate, VeterinarioUpdate, VeterinarioResponse
from crud.veterinario_crud import get_veterinarios, get_veterinario, create_veterinario, update_veterinario, delete_veterinario
from entities.veterinario import Veterinario

router = APIRouter(prefix="/veterinario", tags=["Veterinario"])

@router.get("/", response_model=list[VeterinarioResponse])
def listar_veterinarios(db: Session = Depends(get_db)):
    return get_veterinarios(db)

@router.get("/{veterinario_id}", response_model=VeterinarioResponse)
def obtener_veterinario(veterinario_id: int, db: Session = Depends(get_db)):
    veterinario = get_veterinario(db, veterinario_id)
    if not veterinario:
        raise HTTPException(status_code=404, detail="Veterinario no encontrado")
    return veterinario

@router.post("/", response_model=VeterinarioResponse)
def crear_veterinario(veterinario: VeterinarioCreate, db: Session = Depends(get_db)):
    return create_veterinario(db, veterinario)

@router.put("/{veterinario_id}", response_model=VeterinarioResponse)
def actualizar_veterinario(veterinario_id: int, veterinario: VeterinarioUpdate, db: Session = Depends(get_db)):
    updated = update_veterinario(db, veterinario_id, veterinario)
    if not updated:
        raise HTTPException(status_code=404, detail="Veterinario no encontrado")
    return updated

@router.delete("/{veterinario_id}", response_model=VeterinarioResponse)
def eliminar_veterinario(veterinario_id: int, db: Session = Depends(get_db)):
    deleted = delete_veterinario(db, veterinario_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Veterinario no encontrado")
    return deleted