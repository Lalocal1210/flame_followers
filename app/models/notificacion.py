from sqlalchemy import Column, Integer, ForeignKey, String, Text, Boolean, TIMESTAMP, func
from app.models.base import Base

class Notificacion(Base):
    __tablename__ = "notificaciones"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"))
    mensaje = Column(Text, nullable=False)
    leida = Column(Boolean, default=False)
    tipo = Column(String(50))  # info, alerta, sistema
    fecha = Column(TIMESTAMP, server_default=func.now())
