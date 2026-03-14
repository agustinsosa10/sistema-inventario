from sqlalchemy.orm import Session, joinedload
from app.models.productos import Productos
from app.schemas.producto import ProductoCreate, ProductoUpdate
from app.schemas.movimiento import MovimientoCreate
from app.models.movimientos import TipoEnum
from datetime import datetime, timezone
from app.models.suministro import Suministro
from app.crud import movimiento as movimiento_crud
from typing import Optional


# obtener todos los productos
def get_products(db: Session):
    return (
        db.query(Productos)
        .filter(Productos.deleted_at == None)
        .options(joinedload(Productos.categoria))
        .all()
    )


# obtener producto por id
def get_product_by_id(db: Session, producto_id: int):
    return db.query(Productos).filter(Productos.id == producto_id).first()


def get_product_by_name(db: Session, producto_nombre: str):
    return (
        db.query(Productos)
        .filter(
            Productos.nombre.ilike(f"%{producto_nombre}%"), Productos.deleted_at == None
        )
        .all()
    )


def get_products_by_categorie(db: Session, categorie_id: int):
    return (
        db.query(Productos)
        .filter(Productos.categoria_id == categorie_id, Productos.deleted_at == None)
        .all()
    )


def create_product(db: Session, producto: ProductoCreate):
    db_product = Productos(
        nombre=producto.nombre,
        stock=producto.stock,
        stock_minimo=producto.stock_minimo,
        precio=producto.precio,
        categoria_id=producto.categoria_id,
    )

    db.add(db_product)
    db.flush()

    db_suministro = Suministro(
        producto_id=db_product.id,
        proveedor_id=producto.proveedor_id,
        precio_unitario=producto.precio_suministro,
    )

    db.add(db_suministro)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(
    db: Session,
    product_to_update: Productos,
    producto: ProductoUpdate,
):

    if producto.nombre is not None:
        product_to_update.nombre = producto.nombre
    if producto.stock_minimo is not None:
        product_to_update.stock_minimo = producto.stock_minimo
    if producto.precio is not None:
        product_to_update.precio = producto.precio
    if producto.categoria_id is not None:
        product_to_update.categoria_id = producto.categoria_id

    if producto.cantidad is not None:
        product_to_update.stock += producto.cantidad

        movimiento_crud.create_movimiento(
            db,
            cantidad=producto.cantidad,
            tipo=TipoEnum.restock,
            producto_id=product_to_update.id,
            operador_id=1,
        )

    product_to_update.updated_at = datetime.now(timezone.utc)

    db.commit()
    db.refresh(product_to_update)
    return product_to_update


def delete_product(db: Session, product_to_delete: Productos):

    product_to_delete.deleted_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(product_to_delete)
    return product_to_delete
