from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.mascota_schema import MascotaCreate, MascotaUpdate, MascotaResponse
from crud.mascota_crud import (
    get_mascotas,
    get_mascota,
    create_mascota,
    update_mascota,
    delete_mascota,
)
from entities.mascota import Mascota

router = APIRouter(prefix="/mascotas", tags=["Mascotas"])


@router.get("/", response_model=list[MascotaResponse])
def listar_mascotas(db: Session = Depends(get_db)):
    return get_mascotas(db)


@router.get("/{mascota_id}", response_model=MascotaResponse)
def obtener_mascota(mascota_id: int, db: Session = Depends(get_db)):
    mascota = get_mascota(db, mascota_id)
    if not mascota:
        raise HTTPException(status_code=404, detail="Mascota no encontrada")
    return mascota


@router.post("/", response_model=MascotaResponse)
def crear_mascota(mascota: MascotaCreate, db: Session = Depends(get_db)):
    return create_mascota(db, mascota)


@router.put("/{mascota_id}", response_model=MascotaResponse)
def actualizar_mascota(
    mascota_id: int, mascota: MascotaUpdate, db: Session = Depends(get_db)
):
    updated = update_mascota(db, mascota_id, mascota)
    if not updated:
        raise HTTPException(status_code=404, detail="Mascota no encontrada")
    return updated


@router.delete("/{mascota_id}", response_model=MascotaResponse)
def eliminar_mascota(mascota_id: int, db: Session = Depends(get_db)):
    deleted = delete_mascota(db, mascota_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Mascota no encontrada")
    return deleted
