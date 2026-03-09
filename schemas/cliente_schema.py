from pydantic import BaseModel
from typing import Optional


class ClienteBase(BaseModel):
    nombre: str
    telefono: str
    direccion: str


class ClienteUpdate(BaseModel):
    nombre: Optional[str]
    telefono: Optional[str]
    direccion: Optional[str]


class ClienteResponse(ClienteBase):
    id: int

    model_config = {"from_attributes": True}
