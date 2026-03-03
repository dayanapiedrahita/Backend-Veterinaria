from pydantic import BaseModel
from typing import Optional

class VeterinarioBase(BaseModel):
    nombre: str
    telefono: str
    especialidad: str
    id_sede: int

class VeterinarioUpdate(BaseModel):
    nombre: Optional[str]
    telefono: Optional[str]
    especialidad: Optional[str]
    id_sede: Optional[int]

class VeterinarioResponse(VeterinarioBase):
    id: int

    model_config = {
        "from_attributes": True
    }