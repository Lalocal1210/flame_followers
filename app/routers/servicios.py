from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.servicio import Servicio
from app.schemas.servicio import ServicioCreate, ServicioOut
from typing import List
from app.dependencies.auth import get_current_user

router = APIRouter(prefix="/servicios", tags=["Servicios"])

# Mostrar todos los servicios activos (público)
@router.get("/", response_model=List[ServicioOut])
def obtener_servicios(db: Session = Depends(get_db)):
    return db.query(Servicio).filter(Servicio.activo == True).all()

# Crear servicio (solo admin en el futuro)
@router.post("/", response_model=ServicioOut)
def crear_servicio(servicio: ServicioCreate, db: Session = Depends(get_db), usuario = Depends(get_current_user)):
    nuevo = Servicio(**servicio.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo
