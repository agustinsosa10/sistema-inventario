from app.db.base_class import Base
from sqlalchemy import Column, BigInteger, String, DateTime
from datetime import datetime, timezone
from sqlalchemy.orm import relationship


class Categoria(Base):
    id = Column(BigInteger, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    deleted_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    # relationship permite que las clases sepan que estan conectadas entre si
    productos = relationship("Productos", back_populates="categorias")
