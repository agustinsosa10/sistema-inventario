from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas import venta as venta_schema
from app.api.dependencies import get_db
from typing import List
from app.crud import venta as venta_crud

router = APIRouter()


@router.get("/", response_model=List[venta_schema.Venta])
def get_ventas(db: Session = Depends(get_db)):
    return venta_crud.get_ventas(db)


@router.get("/{venta_id}", response_model=venta_schema.Venta)
def get_venta_by_id(venta_id: int, db: Session = Depends(get_db)):
    venta = venta_crud.get_venta_by_id(db, venta_id=venta_id)

    if not venta:
        raise HTTPException(status_code=404, detail="Venta not found")
    else:
        return venta


@router.get("/operador/{operador_id}", response_model=venta_schema.Venta)
def get_venta_by_operador_id(operador_id: int, db: Session = Depends(get_db)):
    operador = venta_crud.get_venta_by_operador_id(db, operador_id=operador_id)

    if not operador:
        raise HTTPException(status_code=404, detail="Ventas of this operador not found")
    else:
        return operador


@router.get("/operador/name/{operador_nombre}", response_model=List[venta_schema.Venta])
def get_venta_by_operador_name(operador_nombre: str, db: Session = Depends(get_db)):
    operador = venta_crud.get_venta_by_operador_name(
        db, operador_nombre=operador_nombre
    )

    if not operador:
        raise HTTPException(status_code=404, detail="Ventas of this operador not found")
    else:
        return operador
