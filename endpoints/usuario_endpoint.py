from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db

from schemas.usuario_schema import ClienteRegistro, VeterinarioRegistro, LoginSchema
from schemas.usuario_schema import UsuarioResponse
from crud.usuario_crud import (
    register_cliente,
    register_veterinario,
    get_usuario_by_id,
    contar_usuarios,
)

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/registro/cliente")
def registrar_cliente(data: ClienteRegistro, db: Session = Depends(get_db)):
    try:
        return register_cliente(db, data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/registro/veterinario")
def registrar_veterinario(data: VeterinarioRegistro, db: Session = Depends(get_db)):
    try:
        return register_veterinario(db, data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# NOTE: login now handled in autenticar_endpoint

@router.get("/{usuario_id}", response_model=UsuarioResponse)
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):

    usuario = get_usuario_by_id(db, usuario_id)

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return usuario