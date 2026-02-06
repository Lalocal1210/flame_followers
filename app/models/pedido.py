from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, TIMESTAMP
from sqlalchemy.orm import relationship
from app.models.base import Base

class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="SET NULL"))
    servicio_id = Column(Integer, ForeignKey("servicios.id"))
    link = Column(String, nullable=False)
    cantidad = Column(Integer, nullable=False)
    costo = Column(Numeric(10, 2), nullable=True)
    estado = Column(String, default="pendiente")
    fecha = Column(TIMESTAMP)

    usuario = relationship("Usuario", back_populates="pedidos", lazy="joined")
    servicio = relationship("Servicio", back_populates="pedidos", lazy="joined")
