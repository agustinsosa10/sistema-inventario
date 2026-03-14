from app.db.base_class import Base
from sqlalchemy import (
    Column,
    BigInteger,
    String,
    Float,
    DateTime,
    Integer,
    ForeignKey,
    func,
)
from sqlalchemy.orm import relationship
from datetime import datetime, timezone


class Productos(Base):
    id = Column(BigInteger, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    stock = Column(Integer, default=0)
    stock_minimo = Column(Integer, default=0)
    precio = Column(Float, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)
    categoria_id = Column(BigInteger, ForeignKey("categoria.id"), nullable=False)

    # relationship permite que las clases sepan que estan conectadas entre si
    categoria = relationship("Categoria", back_populates="productos")
    movimientos = relationship("Movimientos", back_populates="producto")
    suministros = relationship("Suministro", back_populates="productos")
    ventas_detalle = relationship("VentasDetalle", back_populates="productos")
