from app.db.base_class import Base
from sqlalchemy import Column, BigInteger, String, Float, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone


class Productos(Base):
    id = Column(BigInteger, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    stock = Column(Integer, default=0)
    stock_minimo = Column(Integer, default=0)
    precio = Column(Float, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    deleted_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    categoria_id = Column(BigInteger, ForeignKey("categoria.id"), nullable=False)

    # relationship permite que las clases sepan que estan conectadas entre si
    categorias = relationship("Categoria", back_populates="productos")
    movimientos = relationship("Movimientos", back_populates="productos")
    suministros = relationship("Suministro", back_populates="productos")
