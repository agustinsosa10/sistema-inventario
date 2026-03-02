from app.db.base_class import Base
from sqlalchemy import Column, BigInteger, String, DateTime, Enum, Integer, ForeignKey
from datetime import datetime
import enum


class TipoEnum(str, enum.Enum):
    venta = "venta"
    restock = "restock"
    ajuste = "ajuste"


class Movimientos(Base):
    id = Column(BigInteger, primary_key=True, index=True)
    cantidad = Column(Integer, default=0)
    fecha = Column(DateTime, default=datetime.utcnow)
    tipo = Column(Enum(TipoEnum), nullable=False)
    producto_id = Column(BigInteger, ForeignKey("productos.id"), nullable=False)
    operador_id = Column(BigInteger, ForeignKey("operador.id"), nullable=False)
