from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class NotificacionBase(BaseModel):
    usuario_id: int
    mensaje: str
    leida: Optional[bool] = False
    tipo: Optional[str] = "info"  # info, alerta, sistema

class NotificacionCreate(NotificacionBase):
    pass

class NotificacionOut(NotificacionBase):
    id: int
    fecha: datetime

    class Config:
        orm_mode = True
