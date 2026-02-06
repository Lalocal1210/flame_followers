from sqlalchemy import Column, Integer, ForeignKey, Numeric, String, Text, TIMESTAMP, func
from app.models.base import Base

class Recarga(Base):
    __tablename__ = "recargas"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="SET NULL"))
    monto = Column(Numeric(10, 2), nullable=False)
    metodo_pago = Column(String(50))  # Stripe, PayPal, SPEI, etc.
    referencia = Column(Text)         # puede ser ID de transacción o folio
    estado = Column(String(50), default="pendiente")  # pendiente, confirmada
    fecha = Column(TIMESTAMP, server_default=func.now())
