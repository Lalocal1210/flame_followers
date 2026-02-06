from pydantic import BaseModel
from typing import Optional

class ServicioBase(BaseModel):
    nombre: str
    descripcion: Optional[str]
    precio: float
    plataforma: Optional[str]
    tipo: Optional[str]
    activo: Optional[bool] = True

class ServicioCreate(ServicioBase):
    pass

class ServicioOut(ServicioBase):
    id: int

    class Config:
        orm_mode = True
