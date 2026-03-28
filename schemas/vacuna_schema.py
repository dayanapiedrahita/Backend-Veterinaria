from pydantic import BaseModel
from typing import Optional


class VacunaBase(BaseModel):
    nombre: str
    fabricante: str
    dosis_requeridas: int


class VacunaCreate(VacunaBase):
    pass


class VacunaUpdate(BaseModel):
    nombre: Optional[str] = None
    fabricante: Optional[str] = None
    dosis_requeridas: Optional[int] = None


class VacunaResponse(VacunaBase):
    id: int

    model_config = {"from_attributes": True}
