from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class CitaVacunacionBase(BaseModel):
    fecha: datetime
    estado: str
    id_mascota: int
    id_veterinario: int
    id_vacuna: int


class CitaVacunacionCreate(CitaVacunacionBase):
    pass


class CitaVacunacionUpdate(BaseModel):
    fecha: Optional[datetime] = None
    estado: Optional[str] = None
    id_mascota: Optional[int] = None
    id_veterinario: Optional[int] = None
    id_vacuna: Optional[int] = None


class CitaVacunacionResponse(CitaVacunacionBase):
    id: int

    model_config = {
        "from_attributes": True
    }