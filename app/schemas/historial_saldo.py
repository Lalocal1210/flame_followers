from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class HistorialSaldoBase(BaseModel):
    usuario_id: int
    tipo: str  # recarga, consumo, ajuste
    monto: float
    descripcion: Optional[str]

class HistorialSaldoCreate(HistorialSaldoBase):
    pass

class HistorialSaldoOut(HistorialSaldoBase):
    id: int
    fecha: datetime

    class Config:
        orm_mode = True
