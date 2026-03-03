from pydantic import BaseModel, Optional
from datetime import datetime


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
    created_at: datetime
    updated_at: Optional[datetime.utcnow] = None
    deleted: Optional[datetime.utcnow] = None

    class Config:
        from_atributtes: True


# los datos que mandamos en este caso heredamos los datos de proveedorbase
class ProveedorCreate(ProveedorBase):
    pass
