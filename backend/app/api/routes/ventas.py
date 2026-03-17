from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas import venta as venta_schema
from app.api.dependencies import get_db, verificar_token
from typing import List
from app.crud import venta as venta_crud

router = APIRouter()


@router.get("/", response_model=List[venta_schema.Venta])
def get_ventas(db: Session = Depends(get_db), current_user=Depends(verificar_token)):
    return venta_crud.get_ventas(db)


@router.get("/{venta_id}", response_model=venta_schema.VentaConDetalles)
def get_venta_by_id(
    venta_id: int, db: Session = Depends(get_db), current_user=Depends(verificar_token)
):
    venta = venta_crud.get_venta_by_id(db, venta_id=venta_id)

    if not venta:
        raise HTTPException(status_code=404, detail="Venta not found")
    else:
        return venta


@router.get(
    "/operador/{operador_id}", response_model=List[venta_schema.VentaConDetalles]
)
def get_venta_by_operador_id(
    operador_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(verificar_token),
):
    operador = venta_crud.get_venta_by_operador_id(db, operador_id=operador_id)

    if not operador:
        raise HTTPException(status_code=404, detail="Ventas of this operador not found")
    else:
        return operador


@router.get(
    "/operador/name/{operador_nombre}",
    response_model=List[venta_schema.VentaByOperadorName],
)
def get_venta_by_operador_name(
    operador_nombre: str,
    db: Session = Depends(get_db),
    current_user=Depends(verificar_token),
):
    operador = venta_crud.get_venta_by_operador_name(
        db, operador_nombre=operador_nombre
    )

    if not operador:
        raise HTTPException(status_code=404, detail="Ventas of this operador not found")
    else:
        return operador


@router.get(
    "/producto/{producto_nombre}", response_model=List[venta_schema.VentaByProductoName]
)
def get_venta_by_product_name(
    producto_nombre: str,
    db: Session = Depends(get_db),
    current_user=Depends(verificar_token),
):
    db_product = venta_crud.get_venta_by_product_name(
        db, producto_nombre=producto_nombre
    )

    if not db_product:
        raise HTTPException(status_code=404, detail="Venta of this product not found")
    else:
        return db_product


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=venta_schema.VentaConDetalles,
)
def create_venta(
    new_venta: venta_schema.VentaCreate,
    db: Session = Depends(get_db),
    current_user=Depends(verificar_token),
):
    return venta_crud.create_venta(db, new_venta=new_venta)
