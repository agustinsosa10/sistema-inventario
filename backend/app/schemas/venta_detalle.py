from pydantic import BaseModel
from datetime import datetime


class VentaDetalleBase(BaseModel):
    producto_id: int
    cantidad: int
    precio_unitario: float


# los datos que recibimos
class VentaDetalle(VentaDetalleBase):
    id: int
    venta_id: int

    class Config:
        from_attributes = True


# los datos que enviamos
class VentaDetalleCreate(VentaDetalleBase):
    pass
