from pydantic import BaseModel
from datetime import datetime

class ReporteMensualBase(BaseModel):
    mes: int
    anio: int
    total_usuarios: int
    total_pedidos: int
    total_recargas: float
    ingresos_estimados: float

class ReporteMensualCreate(ReporteMensualBase):
    pass

class ReporteMensualOut(ReporteMensualBase):
    id: int
    fecha_generado: datetime

    class Config:
        orm_mode = True
