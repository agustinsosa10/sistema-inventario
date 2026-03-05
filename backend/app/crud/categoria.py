from sqlalchemy.orm import Session
from app.models.categoria import Categoria
from app.schemas.categoria import CategoriaCreate
from datetime import datetime, timezone


def get_categories(db: Session):
    return db.query(Categoria).all()


def get_category_by_id(db: Session, categoria_id: int):
    return db.query(Categoria).filter(Categoria.id == categoria_id).first()


def get_categoria_by_name(db: Session, categoria_name: str):
    return (
        db.query(Categoria).filter(Categoria.nombre.ilike(f"%{categoria_name}%")).all()
    )


def create_category(db: Session, categoria: CategoriaCreate):
    db_categoria_create = Categoria(nombre=categoria.nombre)
    db.add(db_categoria_create)
    db.commit()
    db.refresh(db_categoria_create)
    return db_categoria_create


def update_category(db: Session, categoria_id: int, categoria: CategoriaCreate):
    db_categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()

    db_categoria.nombre = categoria.nombre

    db.commit()
    db.refresh(db_categoria)
    return db_categoria


def delete_category(db: Session, categoria_id: int):
    db_categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()

    db_categoria.deleted_at = datetime.now(timezone.utc)
    db.commit()
    return db_categoria
