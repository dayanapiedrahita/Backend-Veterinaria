from pydantic import BaseModel
from typing import Optional


class VeterinarioBase(BaseModel):
    nombre: str
    especialidad: str
    sede_id: int


class VeterinarioUpdate(BaseModel):
    nombre: Optional[str]
    especialidad: Optional[str]
    sede_id: Optional[int]


class VeterinarioResponse(VeterinarioBase):
    id: int

    model_config = {"from_attributes": True}
