from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class RecargaBase(BaseModel):
    usuario_id: Optional[int]
    monto: float
    metodo_pago: Optional[str]
    referencia: Optional[str]
    estado: Optional[str] = "pendiente"

class RecargaCreate(RecargaBase):
    pass

class RecargaOut(RecargaBase):
    id: int
    fecha: datetime

    class Config:
        orm_mode = True
