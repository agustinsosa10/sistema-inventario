from app.db.base_class import Base
from sqlalchemy import Column, BigInteger, String, ForeignKey, DateTime, func, Float
from sqlalchemy.orm import relationship


class Ventas(Base):
    id = Column(BigInteger, primary_key=True, index=True)
    operador_id = Column(BigInteger, ForeignKey("operador.id"), nullable=False)
    total = Column(Float, nullable=False, default=0)
    created_at = Column(DateTime, server_default=func.now())

    operador = relationship("Operador", back_populates="venta")
    detalles = relationship("VentasDetalle", back_populates="venta")
    movimientos = relationship("Movimientos", back_populates="venta")
