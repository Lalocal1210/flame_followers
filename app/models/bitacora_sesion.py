from sqlalchemy import Column, Integer, ForeignKey, String, Text, TIMESTAMP, func
from app.models.base import Base

class BitacoraSesion(Base):
    __tablename__ = "bitacora_sesion"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"))
    ip = Column(String(50))
    user_agent = Column(Text)
    fecha_inicio = Column(TIMESTAMP, server_default=func.now())
