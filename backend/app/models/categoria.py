from app.db.base_class import Base
from sqlalchemy import Column, BigInteger, String, DateTime
from datetime import datetime


class Categoria(Base):
    id = Column(BigInteger, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    deleted_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
