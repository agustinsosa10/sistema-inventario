from app.models.operador import Operador
from app.schemas.operador import OperadorLogin
from app.crud import operador as operador_crud
from sqlalchemy.orm import Session
from app.core import security
from fastapi import HTTPException


def auth_user(db: Session, operador: OperadorLogin):

    db_operador = db.query(Operador).filter(Operador.email == operador.email).first()

    if not security.verify_password(operador.password, db_operador.password):
        raise HTTPException(status_code=401, detail="credenciales invalidas")

    token = security.create_access_token(
        {"sub": db_operador.email, "rol": db_operador.rol}
    )

    return {"token": token, "rol": db_operador.rol, "nombre": db_operador.nombre}
