from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.admin_logs import AdminLog
from app.schemas.admin_logs import AdminLogCreate, AdminLogOut
from typing import List
from datetime import datetime

router = APIRouter(prefix="/admin-logs", tags=["Logs de administrador"])

@router.get("/", response_model=List[AdminLogOut])
def obtener_logs(db: Session = Depends(get_db)):
    return db.query(AdminLog).order_by(AdminLog.fecha.desc()).all()

@router.post("/", response_model=AdminLogOut)
def registrar_log(log: AdminLogCreate, db: Session = Depends(get_db)):
    nuevo = AdminLog(
        accion=log.accion,
        admin_nombre=log.admin_nombre,
        fecha=datetime.utcnow()
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo
