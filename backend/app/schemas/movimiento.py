from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from app.schemas import producto, operador


class MovimientoTipo(str, Enum):
    venta = "venta"
    restock = "restock"
    ajuste = "ajuste"


# que herede basemodel le indica a python que tiene validacion de datos
# definimos los tipos de los atributos que contiene la clase
class MovimientoBase(BaseModel):
    cantidad: int
    tipo: MovimientoTipo


# los datos que queremos que nos devuelva la api, ademas de los de movimientobase
class Movimiento(MovimientoBase):
    id: int
    fecha: datetime
    productos: producto.Producto
    operador: operador.Operador

    # convertir objeto en json
    class Config:
        from_attributes = True


# los datos que enviamos a la api, en este caso los de movimientobase
class MovimientoCreate(MovimientoBase):
    pass
