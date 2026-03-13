from sqlalchemy.orm import Session, joinedload
from app.models.movimientos import Movimientos
from app.schemas.movimiento import MovimientoCreate
from datetime import datetime, timezone
from app.models.productos import Productos


def get_movimientos(db: Session):
    return (
        db.query(Movimientos)
        .options(joinedload(Movimientos.productos))
        .options(joinedload(Movimientos.operador))
        .all()
    )


def get_movimientos_by_id(db: Session, movimiento_id: int):
    return db.query(Movimientos).filter(Movimientos.id == movimiento_id).first()


def get_movimientos_by_type(db: Session, movimiento_tipo: str):
    return db.query(Movimientos).filter(Movimientos.tipo == movimiento_tipo).all()


def get_movimiento_by_producto(db: Session, producto_name: str):
    return (
        db.query(Movimientos)
        .join(Productos)
        .filter(
            Productos.nombre.ilike(f"%{producto_name}%"), Productos.deleted_at == None
        )
        .options(joinedload(Movimientos.productos))
        .options(joinedload(Movimientos.operador))
        .all()
    )
