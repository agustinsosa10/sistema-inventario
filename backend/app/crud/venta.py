from sqlalchemy.orm import Session, joinedload
from app.models.ventas import Ventas
from app.schemas.venta import VentaCreate
from app.schemas.movimiento import MovimientoCreate
from app.models.movimientos import TipoEnum
from datetime import datetime, timezone
from app.crud import movimiento as movimiento_crud
from typing import Optional
from app.models.operador import Operador


def get_ventas(db: Session):
    return (
        db.query(Ventas)
        .options(joinedload(Ventas.ventas_detalle))
        .options(joinedload(Ventas.operador))
        .all()
    )


def get_venta_by_id(db: Session, venta_id: int):
    return db.query(Ventas).filter(Ventas.id == venta_id).first()


def get_venta_by_operador_id(db: Session, operador_id: int):
    return db.query(Ventas).filter(Ventas.operador_id == operador_id).first()


def get_venta_by_operador_name(db: Session, operador_nombre: str):
    return (
        db.query(Ventas)
        .join(Operador, Ventas.operador_id == Operador.id)
        .filter(Operador.nombre.ilike(f"%{operador_nombre}%"))
        .options(joinedload(Ventas.ventas_detalle))
        .all()
    )
