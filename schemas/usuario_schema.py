from pydantic import BaseModel, EmailStr

class UsuarioBase(BaseModel):
    nombre: str
    apellido: str
    documento: str
    telefono: str
    email: EmailStr


class UsuarioCreate(UsuarioBase):
    pass


class UsuarioResponse(UsuarioBase):
    id: int

    class Config:
        orm_mode = True