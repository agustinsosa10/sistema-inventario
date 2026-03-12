from pydantic import BaseModel
from datetime import datetime


class VentaDetalleBase(BaseModel):
    venta_id: int
    producto_id: int
    cantidad: int
    precio_unitario: float


# los datos que recibimos
class Venta(VentaDetalleBase):
    id: int
    pass

    class Config:
        from_attributes = True


# los datos que enviamos
class VentaDetalleCreate(VentaDetalleBase):
    pass
