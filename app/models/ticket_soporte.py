from sqlalchemy import Column, Integer, ForeignKey, String, Text, TIMESTAMP, func
from app.models.base import Base

class TicketSoporte(Base):
    __tablename__ = "tickets_soporte"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="SET NULL"))
    asunto = Column(String(150))
    mensaje = Column(Text, nullable=False)
    estado = Column(String(50), default="abierto")  # abierto, en progreso, cerrado
    respuesta = Column(Text)
    fecha_creado = Column(TIMESTAMP, server_default=func.now())
    fecha_resuelto = Column(TIMESTAMP)
