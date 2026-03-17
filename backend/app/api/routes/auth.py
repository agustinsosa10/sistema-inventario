from app.models.operador import Operador
from app.schemas.operador import OperadorAuth, OperadorLogin
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.dependencies import get_db
from app.crud import authentication as auth_crud
from app.crud import operador as operador_crud

router = APIRouter()


@router.post("/login", response_model=OperadorAuth)
def login(operador: OperadorLogin, db: Session = Depends(get_db)):
    db_operador = operador_crud.get_operador_by_email(db, operador_email=operador.email)

    if not db_operador:
        raise HTTPException(status_code=401, detail="Operador not found")
    else:
        return auth_crud.auth_user(db, operador=operador)
