from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# que herede basemodel le indica a python que tiene validacion de datos
# definimos los tipos de los atributos que contiene la clase
class ProveedorBase(BaseModel):
    nombre: str
    telefono: str
    email: str
    localidad: str


# los datos que queremos que se nos retorne, incluimos el id y las fechas
class Proveedor(ProveedorBase):
    id: int
    # created_at: datetime
    # updated_at: Optional[datetime] = None
    # deleted_at: Optional[datetime] = None

    class Config:
        from_atributtes: True


# los datos que mandamos, en este caso heredamos los datos de proveedorbase
class ProveedorCreate(ProveedorBase):
    pass


class ProveedorUpdate(BaseModel):
    nombre: str = None
    telefono: str = None
    email: str = None
    localidad: str = None
