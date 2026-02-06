from sqlalchemy import Column, Integer, String, Text, Numeric, Boolean
from app.models.base import Base
from sqlalchemy.orm import relationship
class Servicio(Base):
    __tablename__ = "servicios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text)
    precio = Column(Numeric(10, 2), nullable=False)
    plataforma = Column(String(50))     # Ej: Instagram, TikTok
    tipo = Column(String(50))           # Ej: seguidores, likes
    activo = Column(Boolean, default=True)
 
pedidos = relationship("Pedido", back_populates="servicio")