from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, func
from app.models.base import Base

class ConfiguracionSistema(Base):
    __tablename__ = "configuraciones_sistema"

    id = Column(Integer, primary_key=True, index=True)
    clave = Column(String(100), unique=True, nullable=False)
    valor = Column(Text)
    descripcion = Column(Text)
    actualizacion = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
