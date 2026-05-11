from pydantic import BaseModel
from typing import Optional


class VeterinarioBase(BaseModel):
    nombre: str
    especialidad: Optional[str] = None
    sede_id: int


class VeterinarioUpdate(BaseModel):
    nombre: Optional[str] = None
    especialidad: Optional[str] = None
    sede_id: Optional[int] = None


class VeterinarioResponse(VeterinarioBase):
    id: int

    model_config = {"from_attributes": True}
