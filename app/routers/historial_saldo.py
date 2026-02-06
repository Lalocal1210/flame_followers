from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.historial_saldo import HistorialSaldo
from app.schemas.historial_saldo import HistorialSaldoOut
from app.dependencies.auth import get_current_user
from app.models.usuario import Usuario
from typing import List

router = APIRouter(prefix="/historial", tags=["Historial de saldo"])

@router.get("/", response_model=List[HistorialSaldoOut])
def obtener_historial(usuario: Usuario = Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(HistorialSaldo)\
             .filter(HistorialSaldo.usuario_id == usuario.id)\
             .order_by(HistorialSaldo.fecha.desc()).all()
