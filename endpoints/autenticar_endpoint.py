from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from crud.usuario_crud import login_usuario
from schemas.usuario_schema import LoginSchema, LoginResponse

router = APIRouter(prefix="/autenticar", tags=["Autenticación"])


@router.post("/login", response_model=LoginResponse)
def login(credentials: LoginSchema, db: Session = Depends(get_db)):
    """Login sencillo que busca usuario por email y devuelve un token simulado"""
    usuario = login_usuario(db, credentials.email)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas"
        )

    # en un sistema real generar JWT u otro token
    token = f"token_{usuario.id}"
    return LoginResponse(token=token, usuario=usuario)