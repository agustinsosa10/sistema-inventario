from app.db.base_class import Base
from sqlalchemy import Column, BigInteger, String, Float, DateTime, Integer, ForeignKey
from datetime import datetime


class Productos(Base):
    id = Column(BigInteger, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    stock = Column(Integer, default=0)
    stock_minimo = Column(Integer, default=0)
    precio = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    deleted_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    categoria_id = Column(BigInteger, ForeignKey("categoria.id"), nullable=False)
