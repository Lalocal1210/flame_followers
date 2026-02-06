from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TokenRecuperacionBase(BaseModel):
    usuario_id: int
    token: str
    usado: Optional[bool] = False
    fecha_expira: Optional[datetime]

class TokenRecuperacionCreate(TokenRecuperacionBase):
    pass

class TokenRecuperacionOut(TokenRecuperacionBase):
    id: int
    fecha_generado: datetime

    class Config:
        orm_mode = True
