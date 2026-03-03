from pydantic import BaseModel
from typing import Optional

class SedeBase(BaseModel):
    nombre: str
    direccion: str
    telefono: str

class SedeCreate(SedeBase):
    pass

class SedeUpdate(BaseModel):
    nombre: Optional[str]
    direccion: Optional[str]
    telefono: Optional[str]

class SedeResponse(SedeBase):
    id: int

    model_config = {
        "from_attributes": True
    }