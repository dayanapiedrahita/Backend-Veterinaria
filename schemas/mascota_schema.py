from pydantic import BaseModel
from typing import Optional


class MascotaBase(BaseModel):
    nombre: str
    edad: Optional[str] = None
    genero_id: Optional[str] = None
    raza_id: Optional[str] = None
    usuario_id: Optional[int] = None


class MascotaCreate(MascotaBase):
    pass


class MascotaUpdate(BaseModel):
    nombre: Optional[str] = None
    edad: Optional[str] = None
    genero_id: Optional[str] = None
    raza_id: Optional[str] = None
    usuario_id: Optional[int] = None


class MascotaResponse(MascotaBase):
    id: int

    model_config = {"from_attributes": True}
