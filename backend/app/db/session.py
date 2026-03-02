# aca se crea la sesion de conexion a la base de datos
from sqlalchemy import create_engine
from sqlachemy.orm import sessionmaker
from sqlachemy.orm.session import engine
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
