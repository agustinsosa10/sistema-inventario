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
        db.query(Productos)
        .filter(
            Productos.nombre.ilike(f"%{producto_nombre}%"), Productos.deleted_at == None
        )
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
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(db: Session, product_to_update: Productos, producto: ProductoCreate):

    product_to_update.nombre = producto.nombre
    product_to_update.stock = producto.stock
    product_to_update.stock_minimo = producto.stock_minimo
    product_to_update.precio = producto.precio
    product_to_update.categoria_id = producto.categoria_id
    product_to_update.updated_at = datetime.now(timezone.utc)

    db.commit()
    db.refresh(product_to_update)
    return product_to_update


def delete_product(db: Session, product_to_delete: Productos):

    product_to_delete.deleted_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(product_to_delete)
    return product_to_delete
