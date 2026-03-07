from pydantic import BaseModel
from typing import Optional

class VacunaBase(BaseModel):
    nombre: str
    fabricante: str
    descripcion: str
    dosis_requeridas: int

class VacunaCreate(VacunaBase):
    pass

class VacunaUpdate(BaseModel):
    nombre: Optional[str]
    fabricante: Optional[str]
    descripcion: Optional[str]
    dosis_requeridas: Optional[int]

class VacunaResponse(VacunaBase):
    id: int

    model_config = {
        "from_attributes": True
    }