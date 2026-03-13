from sqlalchemy.orm import Session
from app.models.proveedores import Proveedores
from app.schemas.proveedor import ProveedorCreate
from datetime import datetime, timezone


def get_proveedores(db: Session):
    return db.query(Proveedores).filter(Proveedores.deleted_at == None).all()


def get_proveedor_by_id(db: Session, proveedor_id: int):
    return db.query(Proveedores).filter(Proveedores.id == proveedor_id).first()


def get_proveedor_by_name(db: Session, proveedor_name: str):
    return (
        db.query(Proveedores)
        .filter(
            Proveedores.nombre.ilike(f"%{proveedor_name}%"),
            Proveedores.deleted_at == None,
        )
        .all()
    )


def create_proveedor(db: Session, new_proveedor: ProveedorCreate):

    db_proveedor = Proveedores(
        nombre=new_proveedor.nombre,
        telefono=new_proveedor.telefono,
        email=new_proveedor.email,
        localidad=new_proveedor.localidad,
    )

    db.add(db_proveedor)
    db.commit()
    db.refresh(db_proveedor)
    return db_proveedor


def update_proveedor(
    db: Session, proveedor_to_update: Proveedores, updated_proveedor: ProveedorCreate
):
    proveedor_to_update.nombre = updated_proveedor.nombre
    proveedor_to_update.telefono = updated_proveedor.telefono
    proveedor_to_update.email = updated_proveedor.email
    proveedor_to_update.localidad = updated_proveedor.localidad
    proveedor_to_update.updated_at = datetime.now(timezone.utc)

    db.commit()
    db.refresh(proveedor_to_update)
    return proveedor_to_update


def delete_product(db: Session, proveedor_to_delete: Proveedores):
    proveedor_to_delete.deleted_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(proveedor_to_delete)
    return proveedor_to_delete
