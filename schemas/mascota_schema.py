from datetime import date
from pydantic import BaseModel
from typing import Optional


class MascotaBase(BaseModel):
    nombre: str
    especie: Optional[str] = None
    raza: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    cliente_id: Optional[int] = None


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
