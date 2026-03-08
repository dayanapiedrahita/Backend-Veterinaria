from pydantic import BaseModel
from typing import Optional

class UsuarioBase(BaseModel):
    email: str
    rol: str

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioUpdate(BaseModel):
    email: Optional[str]
    rol: Optional[str]

class UsuarioResponse(UsuarioBase):
    id: int

    model_config = {
        "from_attributes": True
    }

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

    model_config = {
        "from_attributes": True
    }
