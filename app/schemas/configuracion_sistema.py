from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ConfiguracionSistemaBase(BaseModel):
    clave: str
    valor: Optional[str]
    descripcion: Optional[str]

class ConfiguracionSistemaCreate(ConfiguracionSistemaBase):
    pass

class ConfiguracionSistemaOut(ConfiguracionSistemaBase):
    id: int
    actualizacion: datetime

    class Config:
        orm_mode = True
