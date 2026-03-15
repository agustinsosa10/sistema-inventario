from pydantic import BaseModel
from datetime import datetime
from app.schemas import producto


class VentaDetalleBase(BaseModel):
    producto_id: int
    cantidad: int


# los datos que recibimos
class VentaDetalle(VentaDetalleBase):
    precio_unitario: float

    class Config:
        from_attributes = True


class VentaDetalleProducto(BaseModel):
    productos: producto.ProductoVenta
    cantidad: int

    class Config:
        from_attributes = True


# los datos que enviamos
class VentaDetalleCreate(VentaDetalleBase):
    pass
