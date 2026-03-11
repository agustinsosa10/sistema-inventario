from pydantic import BaseModel
from enum import Enum
from datetime import datetime
from typing import Optional


class RolOperador(str, Enum):
    admin = "admin"
    operador = "operador"


# que herede basemodel le indica a python que tiene validacion de datos
# definimos los tipos de los atributos que contiene la clase
class OperadorBase(BaseModel):
    nombre: str
    rol: RolOperador
    email: str


# los datos que queremos que nos retorne la api + los de operadorbase
class Operador(OperadorBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes: True


# los datos que vamos a enviar a la api, en este caso los de operadorbase y la contraseña
class OperadorCreate(OperadorBase):
    password: str
