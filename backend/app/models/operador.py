from app.db.base_class import Base
from sqlalchemy import Column, BigInteger, String, DateTime, Enum
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
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    deleted_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    movimientos = relationship("Movimientos", back_populates="operador")
