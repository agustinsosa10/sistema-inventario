from pydantic import BaseModel
from datetime import datetime
from typing import List
from app.schemas.venta_detalle import (
    VentaDetalleCreate,
    VentaDetalle,
    VentaDetalleProducto,
)
from app.schemas import operador


# datos que nos retorna
class Venta(BaseModel):
    id: int
    total: float
    created_at: datetime

    class Config:
        from_attributes = True


class VentaConDetalles(BaseModel):
    id: int
    total: float
    created_at: datetime
    detalles: List[VentaDetalle] = []
    operador: operador.OperadorBase

    class Config:
        from_attributes = True


class VentaByOperadorName(BaseModel):
    id: int
    total: float
    created_at: datetime
    detalles: List[VentaDetalle] = []
    operador: operador.Operador

    class Config:
        from_attributes = True


class VentaByProductoName(BaseModel):
    id: int
    total: float
    created_at: datetime
    detalles: List[VentaDetalleProducto] = []
    operador: operador.Operador


# datos que enviamos
class VentaCreate(BaseModel):
    detalles: List[VentaDetalleCreate]
