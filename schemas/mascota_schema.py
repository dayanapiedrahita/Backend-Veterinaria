from pydantic import BaseModel
from datetime import date
from typing import Optional

class MascotaBase(BaseModel):
    nombre: str
    especie: str
    raza: str
    fecha_nacimiento: date
    id_cliente: int

class MascotaCreate(MascotaBase):
    pass

class MascotaUpdate(BaseModel):
    nombre: Optional[str]
    especie: Optional[str]
    raza: Optional[str]
    fecha_nacimiento: Optional[date]
    id_cliente: Optional[int]

class MascotaResponse(MascotaBase):
    id: int

    class Config:
        orm_mode = True