from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.cita_vacunacion_schema import (
    CitaVacunacionCreate,
    CitaVacunacionUpdate,
    CitaVacunacionResponse,
)
from crud.cita_vacunacion_crud import (
    get_citas_vacunacion,
    get_cita_vacunacion,
    create_cita_vacunacion,
    update_cita_vacunacion,
    delete_cita_vacunacion,
)
from entities.cita_vacunacion import CitaVacunacion
from core.dependencies import get_current_user
from entities.usuario import Usuario

router = APIRouter(tags=["CitasVacunacion"])


@router.get("/", response_model=list[CitaVacunacionResponse])
def listar_citas(db: Session = Depends(get_db)):
    return get_citas_vacunacion(db)


@router.get("/{cita_id}", response_model=CitaVacunacionResponse)
def obtener_cita(cita_id: int, db: Session = Depends(get_db)):
    cita = get_cita_vacunacion(db, cita_id)
    if not cita:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return cita


@router.post("/", response_model=CitaVacunacionResponse)
def crear_cita(
    cita: CitaVacunacionCreate,
    current_user: Usuario = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return create_cita_vacunacion(db, cita)


@router.put("/{cita_id}", response_model=CitaVacunacionResponse)
def actualizar_cita(
    cita_id: int,
    cita: CitaVacunacionUpdate,
    current_user: Usuario = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    updated = update_cita_vacunacion(db, cita_id, cita)
    if not updated:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return updated


@router.delete("/{cita_id}", response_model=CitaVacunacionResponse)
def eliminar_cita(
    cita_id: int,
    current_user: Usuario = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    deleted = delete_cita_vacunacion(db, cita_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return deleted
