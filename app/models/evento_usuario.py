from sqlalchemy import Column, Integer, ForeignKey, String, Text, TIMESTAMP, func
from app.models.base import Base

class EventoUsuario(Base):
    __tablename__ = "eventos_usuario"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"))
    evento = Column(String(100))         # Ej: 'login', 'pedido_creado'
    descripcion = Column(Text)
    ip_origen = Column(String(50))
    user_agent = Column(Text)
    fecha = Column(TIMESTAMP, server_default=func.now())
