from sqlalchemy import (
    BigInteger,
    ForeignKey,
    Column,
    Float,
    PrimaryKeyConstraint,
    DateTime,
    func,
)
from app.db.base_class import Base
from sqlalchemy.orm import relationship


class Suministro(Base):
    producto_id = Column(BigInteger, ForeignKey("productos.id"), nullable=False)
    proveedor_id = Column(BigInteger, ForeignKey("proveedores.id"), nullable=False)
    precio_unitario = Column(Float)
    created_at = Column(DateTime, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True)

    __table_args__ = (PrimaryKeyConstraint("producto_id", "proveedor_id"),)

    productos = relationship("Productos", back_populates="suministros")
    proveedores = relationship("Proveedores", back_populates="suministros")
