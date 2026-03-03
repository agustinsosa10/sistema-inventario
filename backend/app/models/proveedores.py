from sqlalchemy import Column, BigInteger, String, DateTime
from datetime import datetime, timezone
from app.db.base_class import Base
from sqlalchemy.orm import relationship


class Proveedores(Base):
    id = Column(BigInteger, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    telefono = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    localidad = Column(String, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    deleted_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    suministros = relationship("Suministro", back_populates="proveedores")
