from pydantic import BaseModel
from datetime import date

class MascotaBase(BaseModel):
    nombre: str
    especie: str
    raza: str
    fecha_nacimiento: date
    id_cliente: int


class MascotaCreate(MascotaBase):
    pass


class MascotaResponse(MascotaBase):
    id: int

    class Config:
        orm_mode = True