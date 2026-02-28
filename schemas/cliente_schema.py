from pydantic import BaseModel

class ClienteBase(BaseModel):
    direccion: str


class ClienteCreate(ClienteBase):
    id: int  # referencia al usuario


class ClienteResponse(ClienteBase):
    id: int

    class Config:
        orm_mode = True