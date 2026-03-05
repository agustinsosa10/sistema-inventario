from app.db.base_class import Base
from sqlalchemy import Column, BigInteger, String, DateTime, func
from datetime import datetime, timezone
from sqlalchemy.orm import relationship


class Categoria(Base):
    id = Column(BigInteger, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # relationship permite que las clases sepan que estan conectadas entre si
    productos = relationship("Productos", back_populates="categorias")
