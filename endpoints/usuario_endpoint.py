from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db

 Feat--Pipeline
from entities.usuario import Usuario

from schemas.usuario_schema import (
    ClienteRegistro,
    VeterinarioRegistro,
    LoginSchema,
    UsuarioResponse
)


from schemas.usuario_schema import ClienteRegistro, VeterinarioRegistro, LoginSchema
from schemas.usuario_schema import UsuarioCreate, UsuarioResponse, UsuarioUpdate
 dev
from crud.usuario_crud import (
    register_cliente,
    register_veterinario,
    get_usuario_by_id,
    get_usuarios,
    create_usuario,
    update_usuario,
    delete_usuario,
    contar_usuarios,
)
from core.dependencies import get_current_user
from entities.usuario import Usuario

router = APIRouter()


@router.post("/registro/cliente")
def registrar_cliente(
    data: ClienteRegistro,
    current_user: Usuario = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        return register_cliente(db, data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/registro/veterinario")
def registrar_veterinario(
    data: VeterinarioRegistro,
    current_user: Usuario = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        return register_veterinario(db, data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=list[UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(Usuario).all()


@router.get("/", response_model=list[UsuarioResponse])
def listar_usuarios(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return get_usuarios(db)


@router.post("/", response_model=UsuarioResponse)
def crear_usuario(
    usuario: UsuarioCreate,
    current_user: Usuario = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    try:
        return create_usuario(
            db,
            email=usuario.email,
            rol=usuario.rol,
            cliente_id=usuario.cliente_id,
            veterinario_id=usuario.veterinario_id,
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{usuario_id}", response_model=UsuarioResponse)
def actualizar_usuario(
    usuario_id: int,
    usuario: UsuarioUpdate,
    current_user: Usuario = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    data = usuario.dict(exclude_unset=True)
    try:
        return update_usuario(db, usuario_id, **data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{usuario_id}")
def eliminar_usuario(
    usuario_id: int,
    current_user: Usuario = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    delete_usuario(db, usuario_id)
    return {"exito": True, "mensaje": "Usuario eliminado correctamente"}


@router.get("/total")
def obtener_total_usuarios(db: Session = Depends(get_db)):
    return {"total": contar_usuarios(db)}


@router.get("/estadisticas/cantidad")
def obtener_cantidad_usuarios(db: Session = Depends(get_db)):
    """Retorna la cantidad de usuarios en formato más simple"""
    return {"cantidad": contar_usuarios(db), "total": contar_usuarios(db)}


@router.get("/{usuario_id}", response_model=UsuarioResponse)
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):

    usuario = get_usuario_by_id(db, usuario_id)

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return usuario