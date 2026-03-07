from pydantic import BaseModel
from datetime import date, time


class CitaVacunacionBase(BaseModel):
    fecha: date
    hora: time
    estado: str
    aplicada: bool
    id_mascota: int
    id_veterinario: int
    id_vacuna: int

class CitaVacunacionCreate(CitaVacunacionBase):
    pass


class CitaVacunacionResponse(CitaVacunacionBase):
    id: int

    class Config:
        from_attributes = True