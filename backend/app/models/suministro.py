from sqlalchemy import BigInteger, ForeignKey, Column, PrimaryKeyConstraint
from app.db.base_class import Base
from sqlalchemy.orm import relationship


class Suministro(Base):
    producto_id = Column(BigInteger, ForeignKey("productos.id"), nullable=False)
    proveedor_id = Column(BigInteger, ForeignKey("proveedores.id"), nullable=False)

    __table_args__ = (PrimaryKeyConstraint("producto_id", "proveedor_id"),)

    productos = relationship("Productos", back_populates="suministros")
    proveedores = relationship("Proveedores", back_populates="suministros")
