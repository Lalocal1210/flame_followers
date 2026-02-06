from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.bitacora_sesion import BitacoraSesion
from app.dependencies.auth import get_current_user
from app.models.usuario import Usuario
from app.schemas.bitacora_sesion import BitacoraSesionOut
from typing import List
from datetime import datetime

router = APIRouter(prefix="/bitacora", tags=["Bitácora de sesiones"])

@router.get("/", response_model=List[BitacoraSesionOut])
def obtener_bitacora(usuario: Usuario = Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(BitacoraSesion)\
             .filter(BitacoraSesion.usuario_id == usuario.id)\
             .order_by(BitacoraSesion.fecha_inicio.desc())\
             .all()

@router.post("/registrar")
def registrar_inicio_sesion(request: Request, usuario: Usuario = Depends(get_current_user), db: Session = Depends(get_db)):
    ip = request.client.host
    user_agent = request.headers.get('user-agent', 'desconocido')
    entrada = BitacoraSesion(
        usuario_id=usuario.id,
        ip=ip,
        user_agent=user_agent,
        fecha_inicio=datetime.utcnow()
    )
    db.add(entrada)
    db.commit()
    return {"mensaje": "Sesión registrada en la bitácora"}
