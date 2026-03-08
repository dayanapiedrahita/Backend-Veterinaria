from pydantic import BaseModel
from datetime import date, time
from typing import Optional


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
    fecha: Optional[date] = None
    hora: Optional[time] = None
    estado: Optional[str] = None
    aplicada: Optional[bool] = None
    id_mascota: Optional[int] = None
    id_veterinario: Optional[int] = None
    id_vacuna: Optional[int] = None


class CitaVacunacionResponse(CitaVacunacionBase):
    id: int

    model_config = {
        "from_attributes": True
    }