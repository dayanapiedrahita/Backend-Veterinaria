from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta

from database import get_db
from crud.usuario_crud import login_usuario
from schemas.usuario_schema import LoginSchema, LoginResponse
from core.security import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter(tags=["Autenticación"])


@router.post("/login", response_model=LoginResponse)
def login(credentials: LoginSchema, db: Session = Depends(get_db)):
    """Login con JWT - valida email y devuelve token JWT"""
    usuario = login_usuario(db, credentials.email)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Credenciales inválidas",
            headers={"WWW-Authenticate": "Bearer"}
        )

    # Generar JWT token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": usuario.email, "id": usuario.id},
        expires_delta=access_token_expires
    )
    
    return LoginResponse(token=access_token, usuario=usuario)
