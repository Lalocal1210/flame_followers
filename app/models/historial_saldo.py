from sqlalchemy import Column, Integer, String, Text, Numeric, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base

class HistorialSaldo(Base):
    __tablename__ = "historial_saldo"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"))
    tipo = Column(String(50))  # recarga, consumo, ajuste
    monto = Column(Numeric(10, 2))
    descripcion = Column(Text)
    fecha = Column(TIMESTAMP)

    # Relación con Usuario
    usuario = relationship("Usuario", back_populates="historial_saldo")
