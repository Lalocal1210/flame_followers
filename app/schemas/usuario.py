from pydantic import BaseModel, EmailStr, constr
from typing import Optional

class UsuarioBase(BaseModel):
    nombre: Optional[str]
    email: EmailStr

class UsuarioCreate(UsuarioBase):
    password: constr(min_length=6)

class UsuarioOut(UsuarioBase):
    id: int
    saldo: float

    class Config:
        orm_mode = True
