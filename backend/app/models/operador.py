from app.db.base_class import Base
from sqlalchemy import Column, BigInteger, String, DateTime, Enum, func
import enum
from datetime import datetime, timezone
from sqlalchemy.orm import relationship


class RolEnum(str, enum.Enum):
    admin = "admin"
    operador = "operador"


class Operador(Base):
    id = Column(BigInteger, primary_key=True, index=True)
    nombre = Column(String)
    rol = Column(Enum(RolEnum), nullable=False)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)

    movimientos = relationship("Movimientos", back_populates="operador")
