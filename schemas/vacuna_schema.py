from pydantic import BaseModel

class VacunaBase(BaseModel):
    nombre: str
    fabricante: str
    descripcion: str


class VacunaCreate(VacunaBase):
    pass


class VacunaResponse(VacunaBase):
    id: int

    class Config:
        orm_mode = True