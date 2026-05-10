from pydantic import BaseModel
from typing import Optional


class UsuarioBase(BaseModel):
    email: str
    rol: str
    cliente_id: int | None = None
    veterinario_id: int | None = None


class UsuarioCreate(UsuarioBase):
    pass


class UsuarioUpdate(BaseModel):
    email: Optional[str] = None
    rol: Optional[str] = None
    cliente_id: Optional[int] = None
    veterinario_id: Optional[int] = None


class UsuarioResponse(UsuarioBase):
    id: int

    model_config = {"from_attributes": True}


class ClienteRegistro(BaseModel):
    nombre: str
    telefono: str
    direccion: str
    email: str


class VeterinarioRegistro(BaseModel):
    nombre: str
    especialidad: str
    id_sede: int
    email: str


class LoginSchema(BaseModel):
    email: str
    # password omitted for now; could be added later if credential checking is required


class LoginResponse(BaseModel):
    token: str
    usuario: UsuarioResponse

    model_config = {"from_attributes": True}
