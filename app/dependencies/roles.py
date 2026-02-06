from fastapi import Depends, HTTPException, status
from app.dependencies.auth import get_current_user

from app.models.usuario import Usuario

def verificar_admin(usuario: Usuario = Depends(get_current_user)):
    if "admin" not in [rol.nombre for rol in usuario.roles]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acceso restringido solo para administradores"
        )
    return usuario
