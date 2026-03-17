from sqlalchemy.orm import Session
from app.models.operador import Operador
from app.schemas.operador import OperadorCreate, OperadorUpdate
from datetime import datetime, timezone
from app.core import security


def get_operadores(db: Session):
    return db.query(Operador).filter(Operador.deleted_at == None).all()


def get_operador_by_id(db: Session, operador_id: int):
    return db.query(Operador).filter(Operador.id == operador_id).first()


def get_operador_by_name(db: Session, operador_name: str):
    return (
        db.query(Operador)
        .filter(
            Operador.nombre.ilike(f"%{operador_name}%"), Operador.deleted_at == None
        )
        .all()
    )


def get_operador_by_email(db: Session, operador_email: str):
    return db.query(Operador).filter(Operador.email == operador_email).first()


def create_operador(db: Session, operador: OperadorCreate):

    hashed_pw = security.get_password_hash(operador.password)

    new_operador = Operador(
        nombre=operador.nombre,
        rol=operador.rol,
        email=operador.email,
        password=hashed_pw,
    )

    db.add(new_operador)
    db.commit()
    db.refresh(new_operador)
    return new_operador


def update_operador(
    db: Session, operador_to_update: Operador, operador: OperadorUpdate
):
    if operador.nombre is not None:
        operador_to_update.nombre = operador.nombre
    if operador.rol is not None:
        operador_to_update.rol = operador.rol
    if operador.email is not None:
        operador_to_update.email = operador.email
    if operador.password is not None:
        operador_to_update.password = operador.password

    operador_to_update.updated_at = datetime.now(timezone.utc)

    db.commit()
    db.refresh(operador_to_update)
    return operador_to_update


def delete_operador(db: Session, operador_to_delete: Operador):

    operador_to_delete.deleted_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(operador_to_delete)
    return operador_to_delete
