from sqlalchemy.orm import Session
from app.models.movimientos import Movimientos
from app.schemas.movimiento import MovimientoCreate
from datetime import datetime, timezone


def get_movimientos(db: Session):
    return db.query(Movimientos).all()
