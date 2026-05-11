from datetime import date
from typing import Optional
from pydantic import BaseModel


class MascotaBase(BaseModel):
    nombre: str
    especie: str
    raza: str
    fecha_nacimiento: Optional[date] = None
    cliente_id: int


class MascotaCreate(MascotaBase):
    pass


class MascotaUpdate(BaseModel):
    nombre: Optional[str] = None
    especie: Optional[str] = None
    raza: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    cliente_id: Optional[int] = None


class MascotaResponse(MascotaBase):
    id: int

    model_config = {"from_attributes": True}
