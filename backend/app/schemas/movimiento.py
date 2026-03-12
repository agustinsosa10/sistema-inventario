from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class MovimientoTipo(str, Enum):
    venta = "venta"
    restock = "restock"
    ajuste = "ajuste"


# que herede basemodel le indica a python que tiene validacion de datos
# definimos los tipos de los atributos que contiene la clase
class MovimientoBase(BaseModel):
    cantidad: int
    tipo: MovimientoTipo
    producto_id: int
    operador_id: int


# los datos que queremos que nos devuelva la api, ademas de los de movimientobase
class Movimiento(MovimientoBase):
    id: int
    fecha: datetime.utcnow

    # convertir objeto en json
    class Config:
        from_attributes = True


# los datos que enviamos a la api, en este caso los de movimientobase
class MovimientoCreate(MovimientoBase):
    pass
