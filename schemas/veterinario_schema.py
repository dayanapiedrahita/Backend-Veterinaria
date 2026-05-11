from pydantic import BaseModel
from typing import Optional


class VeterinarioBase(BaseModel):
    nombre: str
 Feat--Pipeline
    especialidad: Optional[str] = None

    especialidad: str
 dev
    sede_id: int


class VeterinarioUpdate(BaseModel):
 Feat--Pipeline
    nombre: Optional[str] = None
    especialidad: Optional[str] = None
    sede_id: Optional[int] = None

    nombre: Optional[str]
    especialidad: Optional[str]
    sede_id: Optional[int]
 dev


class VeterinarioResponse(VeterinarioBase):
    id: int

    model_config = {"from_attributes": True}
