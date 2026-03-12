from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.schemas.suministro import SuministroCreate


# que herede basemodel le indica a python que tiene validacion de datos
# definimos los tipos de los atributos que contiene la clase
class ProductoBase(BaseModel):
    nombre: str
    stock: int
    stock_minimo: int
    precio: float
    categoria_id: int


# lo que queremos que nos retorne la api
class Producto(ProductoBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

    # que transforme el objeto en json
    class Config:
        from_attributes = True


# lo que mandamos a la api
class ProductoCreate(ProductoBase):
    proveedor_id: int
    precio_suministro: float
