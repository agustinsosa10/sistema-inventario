from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import producto as producto_schema
from app.api.dependencies import get_db
from typing import List
from app.crud import producto as producto_crud

router = APIRouter()


@router.get("/", response_model=List[producto_schema.Producto])
def read_products(db: Session = Depends(get_db)):
    return producto_crud.get_products(db)


@router.get("/{producto_id}", response_model=producto_schema.Producto)
def read_product_by_id(producto_id: int, db: Session = Depends(get_db)):
    db_product = producto_crud.get_product_by_id(db, producto_id=producto_id)

    if db_product is None:
        raise HTTPException(status_code=404, detail="Producto not found")
    else:
        return db_product


@router.get("/name/{producto_nombre}", response_model=List[producto_schema.Producto])
def read_product_by_name(producto_nombre: str, db: Session = Depends(get_db)):
    db_product = producto_crud.get_product_by_name(db, producto_nombre=producto_nombre)

    if db_product is None:
        raise HTTPException(status_code=404, detail="Producto not found")
    else:
        return db_product


@router.post("/", response_model=producto_schema.Producto)
def create_product(
    producto: producto_schema.ProductoCreate, db: Session = Depends(get_db)
):
    # lo que hace esto es mandarle los datos a la funcion del crud para que los inserte en la db
    return producto_crud.create_product(db, producto=producto)


@router.put("/{producto_id}", response_model=producto_schema.Producto)
def update_product(
    producto_id: int,
    producto: producto_schema.ProductoCreate,
    db: Session = Depends(get_db),
):
    db_product_update = producto_crud.get_product_by_id(db, producto_id=producto_id)

    if db_product_update is None:
        raise HTTPException(status_code=404, detail="Producto not found")
    else:
        return producto_crud.update_product(
            db, producto_id=producto_id, producto=producto
        )


@router.delete("/{producto_id}", response_model=producto_schema.Producto)
def delete_product(producto_id: int, db: Session = Depends(get_db)):
    db_product_delete = producto_crud.get_product_by_id(db, producto_id=producto_id)

    if db_product_delete is None:
        raise HTTPException(status_code=404, detail="Producto not found")
    else:
        return producto_crud.delete_product(db, producto_id=producto_id)
