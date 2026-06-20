from datetime import date
from pydantic import BaseModel
from typing import Optional
from pydantic import BaseModel


class MascotaBase(BaseModel):
    nombre: str
 Feat--Pipeline
    especie: str
    raza: str
    fecha_nacimiento: Optional[date] = None
    cliente_id: int

    especie: Optional[str] = None
    raza: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
 dev


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
