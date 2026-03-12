from pydantic import BaseModel
from datetime import datetime


class VentaBase(BaseModel):
    operador_id: int


# datos que nos retorna
class Venta(VentaBase):
    pass
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# datos que enviamos
class VentaCreate(VentaBase):
    pass
