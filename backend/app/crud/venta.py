from sqlalchemy.orm import Session, joinedload
from app.models.ventas import Ventas
from app.models.ventas_detalle import VentasDetalle
from app.models.productos import Productos
from app.schemas.venta import VentaCreate
from app.crud import producto as producto_crud
from app.schemas.movimiento import MovimientoCreate
from app.models.movimientos import TipoEnum
from app.crud import movimiento as movimiento_crud
from typing import Optional
from app.models.operador import Operador


def get_ventas(db: Session):
    return db.query(Ventas).all()


def get_venta_by_id(db: Session, venta_id: int):
    return (
        db.query(Ventas)
        .filter(Ventas.id == venta_id)
        .options(joinedload(Ventas.detalles))
        .options(joinedload(Ventas.operador))
        .first()
    )


def get_venta_by_operador_id(db: Session, operador_id: int):
    return (
        db.query(Ventas)
        .filter(Ventas.operador_id == operador_id)
        .options(joinedload(Ventas.detalles))
        .all()
    )


def get_venta_by_operador_name(db: Session, operador_nombre: str):
    return (
        db.query(Ventas)
        .join(Operador, Ventas.operador_id == Operador.id)
        .filter(Operador.nombre.ilike(f"%{operador_nombre}%"))
        .options(joinedload(Ventas.detalles))
        .all()
    )


def get_venta_by_product_name(db: Session, producto_nombre: str):
    return (
        db.query(Ventas)
        .join(VentasDetalle, Ventas.id == VentasDetalle.venta_id)
        .join(Productos, VentasDetalle.producto_id == Productos.id)
        .filter(Productos.nombre.ilike(f"%{producto_nombre}%"))
        .all()
    )


def create_venta(db: Session, new_venta: VentaCreate):

    db_ventadetalle = []
    total = 0

    for detalles in new_venta.detalles:
        producto = (
            db.query(Productos).filter(Productos.id == detalles.producto_id).first()
        )

        producto.stock -= detalles.cantidad

        movimiento_crud.create_movimiento(
            db,
            cantidad=detalles.cantidad,
            tipo=TipoEnum.venta,
            producto_id=detalles.producto_id,
            operador_id=new_venta.operador_id,
        )

        subtotal = detalles.cantidad * producto.precio
        total += subtotal

        db_ventadetalle.append(
            VentasDetalle(
                producto_id=detalles.producto_id,
                cantidad=detalles.cantidad,
                precio_unitario=producto.precio,
            )
        )

    db_new_venta = Ventas(
        operador_id=new_venta.operador_id, total=total, detalles=db_ventadetalle
    )

    db.add(db_new_venta)
    db.flush()
    db.commit()
    db.refresh(db_new_venta)
    return db_new_venta
