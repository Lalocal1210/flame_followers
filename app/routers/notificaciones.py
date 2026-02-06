from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.notificacion import Notificacion
from app.schemas.notificacion import NotificacionCreate, NotificacionOut
from app.dependencies.auth import get_current_user
from app.models.usuario import Usuario
from typing import List
from datetime import datetime

router = APIRouter(prefix="/notificaciones", tags=["Notificaciones"])

@router.get("/", response_model=List[NotificacionOut])
def obtener_notificaciones(usuario: Usuario = Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(Notificacion).filter(Notificacion.usuario_id == usuario.id).order_by(Notificacion.fecha.desc()).all()

@router.post("/", response_model=NotificacionOut)
def crear_notificacion(noti: NotificacionCreate, db: Session = Depends(get_db), usuario: Usuario = Depends(get_current_user)):
    nueva = Notificacion(**noti.dict())
    nueva.usuario_id = usuario.id
    nueva.fecha = datetime.utcnow()
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

@router.put("/{noti_id}/leer", response_model=NotificacionOut)
def marcar_leida(noti_id: int, db: Session = Depends(get_db), usuario: Usuario = Depends(get_current_user)):
    noti = db.query(Notificacion).filter(Notificacion.id == noti_id, Notificacion.usuario_id == usuario.id).first()
    if noti:
        noti.leida = True
        db.commit()
        db.refresh(noti)
    return noti
