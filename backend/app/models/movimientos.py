from app.db.base_class import Base
from sqlalchemy import (
    Column,
    BigInteger,
    String,
    DateTime,
    Enum,
    Integer,
    ForeignKey,
    func,
)
from datetime import datetime, timezone
import enum
from sqlalchemy.orm import relationship


class TipoEnum(str, enum.Enum):
    venta = "venta"
    restock = "restock"
    ajuste = "ajuste"


class Movimientos(Base):
    id = Column(BigInteger, primary_key=True, index=True)
    cantidad = Column(Integer, default=0)
    fecha = Column(DateTime, server_default=func.now())
    tipo = Column(Enum(TipoEnum), nullable=False)
    producto_id = Column(BigInteger, ForeignKey("productos.id"), nullable=False)
    operador_id = Column(BigInteger, ForeignKey("operador.id"), nullable=False)

    # relationship permite que las clases sepan que estan conectadas entre si
    producto = relationship("Productos", back_populates="movimientos")
    operador = relationship("Operador", back_populates="movimientos")
