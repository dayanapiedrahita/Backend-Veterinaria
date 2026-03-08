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


class CitaVacunacionUpdate(BaseModel):
    fecha: date | None = None
    hora: time | None = None
    estado: str | None = None
    aplicada: bool | None = None
    id_mascota: int | None = None
    id_veterinario: int | None = None
    id_vacuna: int | None = None


class CitaVacunacionResponse(CitaVacunacionBase):
    id: int

    class Config:
        from_attributes = True