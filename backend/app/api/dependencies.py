# archivo para levantar y bajar las sesiones, osea para conectarse y desconectarse de la base de datos

from typing import Generator
from app.db.session import SessionLocal
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from app.core.config import settings
from app.models.operador import Operador
from sqlalchemy.orm import Session


def get_db() -> Generator:
    # nos conectamos a la base de datos
    db = SessionLocal()

    try:
        # pausa la sesion hasta que termine de hacer la peticion
        yield db
    finally:
        # cuando termina, se cierra la sesion
        db.close()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


# Depends quiere decir que antes de ejecutar el endpoint, lea el token del header y que lo pase como string
def verificar_token(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        # jwt.decode devuelve el payload es decir los datos del objeto, {"sub":mail, "rol": elrol, "exp":tiempoexpiracion}
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        # extrae el mail
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Token inválido")
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")

    # verificamos que el usuario exista y no haya sido eliminado despues de que se genero el token
    db_operador = (
        db.query(Operador)
        .filter(Operador.email == email, Operador.deleted_at == None)
        .first()
    )
    if db_operador is None:
        raise HTTPException(status_code=401, detail="Token inválido")

    return db_operador
