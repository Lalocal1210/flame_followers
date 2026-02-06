from pydantic import BaseModel
from datetime import datetime

class AdminLogCreate(BaseModel):
    accion: str
    admin_nombre: str

class AdminLogOut(AdminLogCreate):
    id: int
    fecha: datetime

    class Config:
        from_attributes = True  # ← Pydantic v2 compatible
