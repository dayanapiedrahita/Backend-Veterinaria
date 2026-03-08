from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db

from schemas.veterinario_schema import VeterinarioUpdate, VeterinarioResponse
from crud.veterinario_crud import get_veterinarios, get_veterinario, update_veterinario, delete_veterinario

<<<<<<< HEAD
router = APIRouter(prefix="/veterinarios", tags=["Veterinarios"])
=======
router = APIRouter(prefix="/veterinario", tags=["Veterinario"])
>>>>>>> 5bd09800c98fc85e16530f65b638b366716b6ff5


@router.get("/", response_model=list[VeterinarioResponse])
def listar_veterinarios(db: Session = Depends(get_db)):
    return get_veterinarios(db)


@router.get("/{veterinario_id}", response_model=VeterinarioResponse)
def obtener_veterinario(veterinario_id: int, db: Session = Depends(get_db)):

    veterinario = get_veterinario(db, veterinario_id)

    if not veterinario:
        raise HTTPException(status_code=404, detail="Veterinario no encontrado")

    return veterinario


@router.put("/{veterinario_id}", response_model=VeterinarioResponse)
def actualizar_veterinario(veterinario_id: int, data: VeterinarioUpdate, db: Session = Depends(get_db)):

    updated = update_veterinario(
        db,
        veterinario_id,
        data.nombre,
        data.especialidad,
        data.sede_id
    )

    if not updated:
        raise HTTPException(status_code=404, detail="Veterinario no encontrado")

    return updated


@router.delete("/{veterinario_id}", response_model=VeterinarioResponse)
def eliminar_veterinario(veterinario_id: int, db: Session = Depends(get_db)):

    deleted = delete_veterinario(db, veterinario_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Veterinario no encontrado")

    return deleted