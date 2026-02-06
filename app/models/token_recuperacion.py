from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, TIMESTAMP, func
from app.models.base import Base

class TokenRecuperacion(Base):
    __tablename__ = "tokens_recuperacion"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"))
    token = Column(String(255), nullable=False)
    usado = Column(Boolean, default=False)
    fecha_generado = Column(TIMESTAMP, server_default=func.now())
    fecha_expira = Column(TIMESTAMP)
