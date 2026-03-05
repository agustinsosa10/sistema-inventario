from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import categoria as categoria_schema
from app.api.dependencies import get_db
from typing import List
from app.crud import categoria as categoria_crud

router = APIRouter()


@router.get("/", response_model=List[categoria_schema.Categoria])
def read_categories(db: Session = Depends(get_db)):
    return categoria_crud.get_categories(db)


@router.get("/{categoria_id}", response_model=categoria_schema.Categoria)
def read_category_by_id(categoria_id: int, db: Session = Depends(get_db)):
    db_categoria_by_id = categoria_crud.get_category_by_id(
        db, categoria_id=categoria_id
    )

    if db_categoria_by_id is None:
        raise HTTPException(status_code=404, detail="Categoria Not Found")
    else:
        return db_categoria_by_id


@router.get("/nombre/{categoria_name}", response_model=List[categoria_schema.Categoria])
def read_category_by_name(categoria_name: str, db: Session = Depends(get_db)):
    db_categorie_by_name = categoria_crud.get_categoria_by_name(
        db, categoria_name=categoria_name
    )

    if db_categorie_by_name is None:
        raise HTTPException(status_code=404, detail="Categoria Not Found")
    else:
        return db_categorie_by_name


@router.post("/", response_model=categoria_schema.Categoria)
def create_category(
    categoria: categoria_schema.CategoriaCreate, db: Session = Depends(get_db)
):
    return categoria_crud.create_category(db, categoria=categoria)


@router.put("/{categoria_id}", response_model=categoria_schema.Categoria)
def update_category(
    categoria_id: int,
    new_data_categoria: categoria_schema.CategoriaCreate,
    db: Session = Depends(get_db),
):
    category_to_update = categoria_crud.get_category_by_id(
        db, categoria_id=categoria_id
    )

    if category_to_update is None:
        raise HTTPException(status_code=404, detail="Categoria Not Found")
    else:
        return categoria_crud.update_category(
            db,
            category_to_update=category_to_update,
            new_data_categoria=new_data_categoria,
        )


@router.delete("/{categoria_id}", response_model=categoria_schema.Categoria)
def delete_category(categoria_id: int, db: Session = Depends(get_db)):

    category_to_delete = categoria_crud.get_category_by_id(
        db, categoria_id=categoria_id
    )

    if category_to_delete is None:
        raise HTTPException(status_code=404, detail="Categoria Not Found")
    else:
        return categoria_crud.delete_category(db, category_to_delete=category_to_delete)
