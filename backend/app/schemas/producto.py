from pydantic import BaseModel, Optional
from datetime import datetime


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
    created_at: datetime.utcnow
    updated_at: Optional[datetime.utcnow] = None
    deleted: Optional[datetime.utcnow] = None

    # que transforme el objeto en json
    class Config:
        from_atributtes: True


# lo que mandamos a la api
class ProductoCreate(ProductoBase):
    pass
