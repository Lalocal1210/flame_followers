from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.pedido import Pedido
from app.models.servicio import Servicio
from app.models.usuario import Usuario
from app.models.historial_saldo import HistorialSaldo
from app.schemas.pedido import PedidoCreate, PedidoOut
from app.routers.auth import get_current_user
from datetime import datetime

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])


@router.get("/", response_model=list[PedidoOut])
def listar_pedidos(db: Session = Depends(get_db), usuario: Usuario = Depends(get_current_user)):
    return db.query(Pedido).filter(Pedido.usuario_id == usuario.id).order_by(Pedido.fecha.desc()).all()


@router.post("/", response_model=PedidoOut)
def crear_pedido(pedido_data: PedidoCreate, db: Session = Depends(get_db), usuario: Usuario = Depends(get_current_user)):
    servicio = db.query(Servicio).filter(Servicio.id == pedido_data.servicio_id, Servicio.activo == True).first()

    if not servicio:
        raise HTTPException(status_code=404, detail="Servicio no disponible")

    costo_total = servicio.precio * (pedido_data.cantidad / 1000)

    if usuario.saldo < costo_total:
        raise HTTPException(status_code=400, detail="Saldo insuficiente")

    # Crear pedido
    pedido = Pedido(
        usuario_id=usuario.id,
        servicio_id=servicio.id,
        link=pedido_data.link,
        cantidad=pedido_data.cantidad,
        costo=costo_total,
        estado="pendiente",
        fecha=datetime.utcnow()
    )
    db.add(pedido)

    # Descontar saldo
    usuario.saldo -= costo_total
    db.add(usuario)

    # Registrar historial
    registro = HistorialSaldo(
        usuario_id=usuario.id,
        tipo="consumo",
        monto=costo_total,
        descripcion=f"Pedido de {servicio.nombre}",
        fecha=datetime.utcnow()
    )
    db.add(registro)

    db.commit()
    db.refresh(pedido)

    return pedido
