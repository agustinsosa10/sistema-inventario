from pydantic import BaseModel
from datetime import datetime
from typing import List
from app.schemas.venta_detalle import VentaDetalleCreate, VentaDetalle


class VentaBase(BaseModel):
    operador_id: int


# datos que nos retorna
class Venta(VentaBase):
    id: int
    total: float
    created_at: datetime
    detalles: List[VentaDetalle]

    class Config:
        from_attributes = True


# datos que enviamos
class VentaCreate(VentaBase):
    detalles: List[VentaDetalleCreate]
