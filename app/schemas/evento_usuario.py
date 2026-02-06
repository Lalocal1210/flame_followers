from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class EventoUsuarioBase(BaseModel):
    usuario_id: int
    evento: str  # Ej: 'login', 'pedido_creado'
    descripcion: Optional[str]
    ip_origen: Optional[str]
    user_agent: Optional[str]

class EventoUsuarioCreate(EventoUsuarioBase):
    pass

class EventoUsuarioOut(EventoUsuarioBase):
    id: int
    fecha: datetime

    class Config:
        orm_mode = True
