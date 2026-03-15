from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.schemas.suministro import SuministroCreate
from app.schemas import categoria


# que herede basemodel le indica a python que tiene validacion de datos
# definimos los tipos de los atributos que contiene la clase
class ProductoBase(BaseModel):
    nombre: str
    stock: int
    stock_minimo: int
    precio: float


# lo que queremos que nos retorne la api
class Producto(ProductoBase):
    id: int
    categoria: categoria.Categoria
    # comente las fechas por que no son tan relevantes para mostrarla al usuario
    # created_at: datetime
    # updated_at: Optional[datetime] = None
    # deleted_at: Optional[datetime] = None

    # que transforme el objeto en json
    class Config:
        from_attributes = True


class ProductoVenta(BaseModel):
    id: int
    nombre: str
    categoria: categoria.Categoria

    class Config:
        from_attributes = True


# lo que mandamos a la api
class ProductoCreate(ProductoBase):
    categoria_id: int
    proveedor_id: int
    precio_suministro: float


# hereda de BaseModel y no de ProductoBase por que en ProductoBase los campos son obligatorios y aca necesitamos campos opcionales
class ProductoUpdate(BaseModel):
    nombre: str = None
    stock_minimo: int = None
    precio: float = None
    categoria_id: int = None
    proveedor_id: int = None
    precio_suministro: float = None
    cantidad: Optional[int] = None
