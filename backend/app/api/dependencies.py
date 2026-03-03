# archivo para levantar y bajar las sesiones, osea para conectarse y desconectarse de la base de datos

from typing import Generator
from app.db.session import SessionLocal


def get_db() -> Generator:
    # nos conectamos a la base de datos
    db = SessionLocal()

    try:
        # pausa la sesion hasta que termine de hacer la peticion
        yield db
    finally:
        # cuando termina, se cierra la sesion
        db.close()
