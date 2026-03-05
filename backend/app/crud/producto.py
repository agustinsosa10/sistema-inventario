from sqlalchemy.orm import Session
from app.models.productos import Productos
from app.schemas.producto import ProductoCreate
from datetime import datetime, timezone


# obtener todos los productos
def get_products(db: Session):
    return db.query(Productos).all()


# obtener producto por id
def get_product_by_id(db: Session, producto_id: int):
    return db.query(Productos).filter(Productos.id == producto_id).first()


def get_product_by_name(db: Session, producto_nombre: str):
    return (
        db.query(Productos).filter(Productos.nombre.ilike(f"%{producto_nombre}%")).all()
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
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(db: Session, producto_id: int, producto: ProductoCreate):
    db_product_updated = db.query(Productos).filter(Productos.id == producto_id).first()

    db_product_updated.nombre = producto.nombre
    db_product_updated.stock = producto.stock
    db_product_updated.stock_minimo = producto.stock_minimo
    db_product_updated.precio = producto.precio
    db_product_updated.categoria_id = producto.categoria_id

    db.commit()
    db.refresh(db_product_updated)
    return db_product_updated


def delete_product(db: Session, producto_id: int):
    db_product_deleted = db.query(Productos).filter(Productos.id == producto_id).first()

    db_product_deleted.deleted_at = datetime.now(timezone.utc)
    db.commit()
    return db_product_deleted
