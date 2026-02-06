from pydantic import BaseModel
from datetime import datetime

class PedidoCreate(BaseModel):
    servicio_id: int
    link: str
    cantidad: int

class PedidoOut(BaseModel):
    id: int
    usuario_id: int
    servicio_id: int
    link: str
    cantidad: int
    costo: float
    estado: str
    fecha: datetime

    class Config:
        orm_mode = True
