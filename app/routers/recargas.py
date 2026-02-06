from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.recarga import Recarga
from app.models.usuario import Usuario
from app.models.historial_saldo import HistorialSaldo
from app.schemas.recarga import RecargaCreate, RecargaOut
from app.dependencies.auth import get_current_user
from typing import List

router = APIRouter(prefix="/recargas", tags=["Recargas"])

@router.get("/", response_model=List[RecargaOut])
def obtener_recargas(usuario: Usuario = Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(Recarga).filter(Recarga.usuario_id == usuario.id).order_by(Recarga.fecha.desc()).all()

@router.post("/", response_model=RecargaOut)
def crear_recarga(recarga: RecargaCreate, db: Session = Depends(get_db), usuario: Usuario = Depends(get_current_user)):
    nueva = Recarga(
        usuario_id=usuario.id,
        monto=recarga.monto,
        metodo_pago=recarga.metodo_pago,
        referencia=recarga.referencia,
        estado="confirmada"  # en real, podría ser "pendiente"
    )
    db.add(nueva)

    # Aumentar saldo
    usuario.saldo += recarga.monto

    # Registrar en historial de saldo
    movimiento = HistorialSaldo(
        usuario_id=usuario.id,
        tipo="recarga",
        monto=recarga.monto,
        descripcion=f"Recarga de saldo por {recarga.metodo_pago}"
    )
    db.add(movimiento)

    db.commit()
    db.refresh(nueva)
    return nueva
