from sqlalchemy import Column, Integer, String, Numeric, Text, TIMESTAMP, func
from sqlalchemy.orm import relationship
from .base import Base

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    email = Column(String(150), unique=True, nullable=False)
    password_hash = Column(Text, nullable=False)
    saldo = Column(Numeric(10, 2), default=0)
    fecha_registro = Column(TIMESTAMP, server_default=func.now())

    roles = relationship("UsuarioRol", back_populates="usuario")
pedidos = relationship("Pedido", back_populates="usuario")
