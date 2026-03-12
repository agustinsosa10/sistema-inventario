from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# que herede basemodel le indica a python que tiene validacion de datos
# definimos los tipos de los atributos que contiene la clase
class SuministroBase(BaseModel):
    producto_id: int
    proveedor_id: int
    precio_unitario: float


# aca definimos que queremos que nos retorne la api
class Suministro(SuministroBase):
    pass
    created_at: datetime
    deleted_at: Optional[datetime] = None

    # convierte los datos del objeto en json
    class Config:
        from_attributes = True


# que es lo que le vamos a mandar a la api
class SuministroCreate(SuministroBase):
    pass
