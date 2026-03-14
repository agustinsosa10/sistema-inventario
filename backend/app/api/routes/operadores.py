from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.crud import operador as operador_crud
from app.schemas import operador as operador_schema
from app.api.dependencies import get_db

router = APIRouter()


@router.get("/", response_model=List[operador_schema.Operador])
def read_operadores(db: Session = Depends(get_db)):
    return operador_crud.get_operadores(db)


@router.get("/{operador_id}", response_model=operador_schema.Operador)
def read_operador_by_id(operador_id: int, db: Session = Depends(get_db)):
    operador_by_id = operador_crud.get_operador_by_id(db, operador_id=operador_id)

    if not operador_by_id or operador_by_id.deleted_at is not None:
        raise HTTPException(status_code=404, detail="Operador Not Found")
    else:
        return operador_by_id


@router.get("/name/{operador_nombre}", response_model=List[operador_schema.Operador])
def read_operador_by_name(operador_nombre: str, db: Session = Depends(get_db)):
    operador_by_name = operador_crud.get_operador_by_name(
        db, operador_name=operador_nombre
    )

    if not operador_by_name:
        raise HTTPException(status_code=404, detail="Operador Not Found")
    else:
        return operador_by_name


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=operador_schema.Operador
)
def create_operador(
    operador: operador_schema.OperadorCreate, db: Session = Depends(get_db)
):
    return operador_crud.create_operador(db, operador=operador)


@router.put("/{operador_id}", response_model=operador_schema.Operador)
def update_operador(
    operador_id: int,
    operador: operador_schema.OperadorUpdate,
    db: Session = Depends(get_db),
):
    operador_to_update = operador_crud.get_operador_by_id(db, operador_id=operador_id)

    if not operador_to_update or operador_to_update.deleted_at is not None:
        raise HTTPException(status_code=404, detail="Operador Not Found")
    else:
        return operador_crud.update_operador(
            db, operador_to_update=operador_to_update, operador=operador
        )


@router.delete("/{operador_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_operador(operador_id: int, db: Session = Depends(get_db)):
    operador_to_delete = operador_crud.get_operador_by_id(db, operador_id=operador_id)
    if not operador_to_delete or operador_to_delete.deleted_at is not None:
        raise HTTPException(status_code=404, detail="Operador Not Found")
    else:
        return operador_crud.delete_operador(db, operador_to_delete=operador_to_delete)
