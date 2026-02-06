from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.ticket_soporte import TicketSoporte
from app.schemas.ticket_soporte import TicketSoporteCreate, TicketSoporteOut
from app.dependencies.auth import get_current_user
from app.models.usuario import Usuario
from typing import List
from datetime import datetime

router = APIRouter(prefix="/soporte", tags=["Soporte"])

@router.post("/", response_model=TicketSoporteOut)
def crear_ticket(ticket: TicketSoporteCreate, db: Session = Depends(get_db), usuario: Usuario = Depends(get_current_user)):
    nuevo = TicketSoporte(
        usuario_id=usuario.id,
        asunto=ticket.asunto,
        mensaje=ticket.mensaje,
        estado="abierto"
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.get("/", response_model=List[TicketSoporteOut])
def listar_tickets(usuario: Usuario = Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(TicketSoporte).filter(TicketSoporte.usuario_id == usuario.id).order_by(TicketSoporte.fecha_creado.desc()).all()

@router.put("/{ticket_id}/responder", response_model=TicketSoporteOut)
def responder_ticket(ticket_id: int, respuesta: str, db: Session = Depends(get_db), usuario: Usuario = Depends(get_current_user)):
    ticket = db.query(TicketSoporte).filter(TicketSoporte.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket no encontrado")

    ticket.respuesta = respuesta
    ticket.estado = "cerrado"
    ticket.fecha_resuelto = datetime.utcnow()
    db.commit()
    db.refresh(ticket)
    return ticket
