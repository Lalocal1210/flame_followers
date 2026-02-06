from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BitacoraSesionBase(BaseModel):
    usuario_id: int
    ip: Optional[str]
    user_agent: Optional[str]

class BitacoraSesionCreate(BitacoraSesionBase):
    pass

class BitacoraSesionOut(BitacoraSesionBase):
    id: int
    fecha_inicio: datetime

    class Config:
        orm_mode = True
