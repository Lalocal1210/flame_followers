from fastapi import APIRouter, Depends
from app.dependencies.auth import get_current_user
from app.schemas.usuario import UsuarioOut
from app.models.usuario import Usuario

router = APIRouter(prefix="/perfil", tags=["Perfil"])

@router.get("/", response_model=UsuarioOut)
def ver_perfil(usuario: Usuario = Depends(get_current_user)):
    return usuario
