from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.usuario_schema import UsuarioCreate, UsuarioUpdate, UsuarioResponse
from crud.usuario_crud import get_usuarios, get_usuario, create_usuario, update_usuario, delete_usuario
from entities.usuario import Usuario

router = APIRouter(prefix="/usuario", tags=["Usuario"])

@router.get("/", response_model=list[UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    return get_usuarios(db)

@router.get("/{usuario_id}", response_model=UsuarioResponse)
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = get_usuario(db, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.post("/", response_model=UsuarioResponse)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return create_usuario(db, usuario)

@router.put("/{usuario_id}", response_model=UsuarioResponse)
def actualizar_usuario(usuario_id: int, usuario: UsuarioUpdate, db: Session = Depends(get_db)):
    updated = update_usuario(db, usuario_id, usuario)
    if not updated:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return updated

@router.delete("/{usuario_id}", response_model=UsuarioResponse)
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    deleted = delete_usuario(db, usuario_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return deleted