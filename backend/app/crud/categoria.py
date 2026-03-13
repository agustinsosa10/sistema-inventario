from sqlalchemy.orm import Session
from app.models.categoria import Categoria
from app.schemas.categoria import CategoriaCreate
from datetime import datetime, timezone


def get_categories(db: Session):
    return db.query(Categoria).filter(Categoria.deleted_at == None).all()


def get_category_by_id(db: Session, categoria_id: int):
    return db.query(Categoria).filter(Categoria.id == categoria_id).first()


def get_categoria_by_name(db: Session, categoria_name: str):
    return (
        db.query(Categoria)
        .filter(
            Categoria.nombre.ilike(f"%{categoria_name}%"), Categoria.deleted_at == None
        )
        .all()
    )


def create_category(db: Session, categoria: CategoriaCreate):
    db_categoria_create = Categoria(nombre=categoria.nombre)
    db.add(db_categoria_create)
    db.commit()
    db.refresh(db_categoria_create)
    return db_categoria_create


def update_category(
    db: Session, category_to_update: Categoria, new_data_categoria: CategoriaCreate
):

    category_to_update.nombre = new_data_categoria.nombre
    category_to_update.updated_at = datetime.now(timezone.utc)

    db.commit()
    db.refresh(category_to_update)
    return category_to_update


def delete_category(db: Session, category_to_delete: Categoria):

    category_to_delete.deleted_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(category_to_delete)
    return category_to_delete
