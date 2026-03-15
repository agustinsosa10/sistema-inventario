from app.db.base_class import Base
from sqlalchemy import Column, BigInteger, Float, ForeignKey, DateTime, func, Integer
from sqlalchemy.orm import relationship


class VentasDetalle(Base):
    id = Column(BigInteger, primary_key=True, index=True)
    venta_id = Column(BigInteger, ForeignKey("ventas.id"), nullable=False)
    producto_id = Column(BigInteger, ForeignKey("productos.id"), nullable=False)
    cantidad = Column(Integer, nullable=False, default=0)
    precio_unitario = Column(Float, nullable=False, default=0)

    venta = relationship("Ventas", back_populates="detalles")
    productos = relationship("Productos", back_populates="ventas_detalle")
