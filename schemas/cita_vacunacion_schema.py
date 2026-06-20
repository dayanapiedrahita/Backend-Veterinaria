from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class CitaVacunacionBase(BaseModel):
    fecha: datetime
    estado: str
    mascota_id: int
    veterinario_id: int
    vacuna_id: int


class CitaVacunacionCreate(CitaVacunacionBase):
    pass


class CitaVacunacionUpdate(BaseModel):
    fecha: Optional[datetime] = None
    estado: Optional[str] = None
    mascota_id: Optional[int] = None
    veterinario_id: Optional[int] = None
    vacuna_id: Optional[int] = None


class CitaVacunacionResponse(CitaVacunacionBase):
    id: int

    model_config = {"from_attributes": True}
