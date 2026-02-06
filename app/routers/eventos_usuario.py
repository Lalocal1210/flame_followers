from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.evento_usuario import EventoUsuario
from app.schemas.evento_usuario import EventoUsuarioCreate, EventoUsuarioOut
from app.dependencies.auth import get_current_user
from app.models.usuario import Usuario
from typing import List
from datetime import datetime

router = APIRouter(prefix="/eventos", tags=["Eventos del usuario"])

@router.get("/", response_model=List[EventoUsuarioOut])
def listar_eventos_usuario(usuario: Usuario = Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(EventoUsuario)\
        .filter(EventoUsuario.usuario_id == usuario.id)\
        .order_by(EventoUsuario.fecha.desc()).all()

@router.post("/", response_model=EventoUsuarioOut)
def registrar_evento(evento: EventoUsuarioCreate, usuario: Usuario = Depends(get_current_user), db: Session = Depends(get_db)):
    nuevo = EventoUsuario(
        usuario_id=usuario.id,
        evento=evento.evento,
        descripcion=evento.descripcion,
        ip_origen=evento.ip_origen,
        user_agent=evento.user_agent,
        fecha=datetime.utcnow()
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo
