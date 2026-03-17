from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas import movimiento as movimiento_schema
from app.api.dependencies import get_db, verificar_token
from typing import List
from app.crud import movimiento as movimiento_crud


router = APIRouter()


@router.get("/", response_model=List[movimiento_schema.Movimiento])
def get_movimientos(
    db: Session = Depends(get_db), current_user=Depends(verificar_token)
):
    return movimiento_crud.get_movimientos(db)


@router.get("/{movimiento_id}", response_model=movimiento_schema.Movimiento)
def get_movimiento_by_id(
    movimiento_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(verificar_token),
):
    db_movimiento = movimiento_crud.get_movimientos_by_id(
        db, movimiento_id=movimiento_id
    )

    if not db_movimiento:
        raise HTTPException(status_code=404, detail="Movimiento not found")
    else:
        return db_movimiento


@router.get(
    "/tipo/{movimiento_tipo}", response_model=List[movimiento_schema.Movimiento]
)
def get_movimiento_by_type(
    movimiento_tipo: str,
    db: Session = Depends(get_db),
    current_user=Depends(verificar_token),
):
    db_movimientos = movimiento_crud.get_movimientos_by_type(
        db, movimiento_tipo=movimiento_tipo
    )

    if not db_movimientos:
        raise HTTPException(
            status_code=404, detail="Movimientos of these type not founds"
        )
    else:
        return db_movimientos


@router.get(
    "/producto/{producto_name}", response_model=List[movimiento_schema.Movimiento]
)
def get_movimiento_by_product(
    producto_name: str,
    db: Session = Depends(get_db),
    current_user=Depends(verificar_token),
):
    db_movimiento_by_product = movimiento_crud.get_movimiento_by_producto(
        db, producto_name=producto_name
    )

    if not db_movimiento_by_product:
        raise HTTPException(
            status_code=404, detail="Movimientos of these producto not found"
        )
    else:
        return db_movimiento_by_product
