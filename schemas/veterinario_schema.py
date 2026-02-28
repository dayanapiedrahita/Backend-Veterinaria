from pydantic import BaseModel

class VeterinarioBase(BaseModel):
    tarjeta_profesional: str
    especialidad: str
    id_sede: int


class VeterinarioCreate(VeterinarioBase):
    id: int  # referencia al usuario


class VeterinarioResponse(VeterinarioBase):
    id: int

    class Config:
        orm_mode = True