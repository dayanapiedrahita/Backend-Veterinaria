from pydantic import BaseModel

class SedeBase(BaseModel):
    nombre: str
    direccion: str
    telefono: str

class SedeCreate(SedeBase):
    pass

class SedeUpdate(SedeBase):
    pass

class SedeResponse(SedeBase):
    id: int

    class Config:
        from_attributes = True