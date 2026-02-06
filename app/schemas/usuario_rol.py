from pydantic import BaseModel

class UsuarioRolBase(BaseModel):
    usuario_id: int
    rol_id: int

class UsuarioRolCreate(UsuarioRolBase):
    pass

class UsuarioRolOut(UsuarioRolBase):
    id: int

    class Config:
        orm_mode = True
