from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas import proveedor as proveedor_schema
from app.api.dependencies import get_db
from typing import List
from app.crud import proveedor as proveedor_crud

router = APIRouter()


@router.get("/", response_model=List[proveedor_schema.Proveedor])
def get_proveedores(db: Session = Depends(get_db)):
    return proveedor_crud.get_proveedores(db)


@router.get("/{proveedor_id}", response_model=proveedor_schema.Proveedor)
def get_proveedor_by_id(proveedor_id: int, db: Session = Depends(get_db)):
    proveedor = proveedor_crud.get_proveedor_by_id(db, proveedor_id=proveedor_id)

    if not proveedor or proveedor.deleted_at is not None:
        raise HTTPException(status_code=404, detail="Proveedor not found")
    else:
        return proveedor


@router.get("/name/{proveedor_name}", response_model=List[proveedor_schema.Proveedor])
def get_proveedor_by_name(proveedor_name: str, db: Session = Depends(get_db)):
    proveedor = proveedor_crud.get_proveedor_by_name(db, proveedor_name=proveedor_name)

    if not proveedor:
        raise HTTPException(status_code=404, detail="Proveedor Not Found")
    else:
        return proveedor


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=proveedor_schema.Proveedor
)
def create_proveedor(
    new_proveedor: proveedor_schema.ProveedorCreate, db: Session = Depends(get_db)
):
    return proveedor_crud.create_proveedor(db, new_proveedor=new_proveedor)


@router.put("/{proveedor_id}", response_model=proveedor_schema.Proveedor)
def update_proveedor(
    proveedor_id: int,
    updated_proveedor: proveedor_schema.ProveedorCreate,
    db: Session = Depends(get_db),
):
    proveedor_to_update = proveedor_crud.get_proveedor_by_id(
        db, proveedor_id=proveedor_id
    )

    if not proveedor_to_update or proveedor_to_update.deleted_at is not None:
        raise HTTPException(status_code=404, detail="Proveedor Not Found")
    else:
        return proveedor_crud.update_proveedor(
            db,
            proveedor_to_update=proveedor_to_update,
            updated_proveedor=updated_proveedor,
        )


@router.delete("/{proveedor_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_proveedor(proveedor_id: int, db: Session = Depends(get_db)):
    proveedor_to_delete = proveedor_crud.get_proveedor_by_id(
        db, proveedor_id=proveedor_id
    )

    if not proveedor_to_delete or proveedor_to_delete.deleted_at is not None:
        raise HTTPException(status_code=404, detail="Proveedor Not Found")
    else:
        return proveedor_crud.delete_product(
            db, proveedor_to_delete=proveedor_to_delete
        )
