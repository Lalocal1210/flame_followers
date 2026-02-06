from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TicketSoporteBase(BaseModel):
    usuario_id: int
    asunto: Optional[str]
    mensaje: str
    estado: Optional[str] = "abierto"  # abierto, en progreso, cerrado
    respuesta: Optional[str]

class TicketSoporteCreate(TicketSoporteBase):
    pass

class TicketSoporteOut(TicketSoporteBase):
    id: int
    fecha_creado: datetime
    fecha_resuelto: Optional[datetime]

    class Config:
        orm_mode = True
