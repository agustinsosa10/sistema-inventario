from sqlalchemy.orm import Session
from app.models.operador import Operador
from app.schemas.operador import OperadorCreate
from datetime import datetime, timezone


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


def create_operador(db: Session, operador: OperadorCreate):
    new_operador = Operador(
        nombre=operador.nombre,
        rol=operador.rol,
        email=operador.email,
        password=operador.password,
    )

    db.add(new_operador)
    db.commit()
    db.refresh(new_operador)
    return new_operador


def update_operador(
    db: Session, operador_to_update: Operador, operador: OperadorCreate
):

    operador_to_update.nombre = operador.nombre
    operador_to_update.rol = operador.rol
    operador_to_update.email = operador.email
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
