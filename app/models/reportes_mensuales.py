from sqlalchemy import Column, Integer, Numeric, TIMESTAMP
from app.models.base import Base

class ReporteMensual(Base):
    __tablename__ = "reportes_mensuales"

    id = Column(Integer, primary_key=True, index=True)
    mes = Column(Integer, nullable=False)
    anio = Column(Integer, nullable=False)
    total_usuarios = Column(Integer, nullable=False)
    total_pedidos = Column(Integer, nullable=False)
    total_recargas = Column(Numeric(10, 2), nullable=False)
    ingresos_estimados = Column(Numeric(10, 2), nullable=False)
    fecha_generado = Column(TIMESTAMP, nullable=False)
