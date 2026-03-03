from pydantic import BaseModel, Optional
from enum import Enum
from datetime import datetime


class RolOperador(str, Enum):
    admin = "admin"
    operador = "operador"


# que herede basemodel le indica a python que tiene validacion de datos
# definimos los tipos de los atributos que contiene la clase
class OperadorBase(BaseModel):
    nombre: str
    rol: RolOperador
    email: str
    password: str


# los datos que queremos que nos retorne la api + los de operadorbase
class Operador(OperadorBase):
    id: int
    created_at: datetime.utcnow
    updated_at: Optional[datetime.utcnow] = None
    deleted: Optional[datetime.utcnow] = None

    class Config:
        from_atributtes: True


# los datos que vamos a enviar a la api, en este caso los de operadorbase
class OperadorCreate(OperadorBase):
    pass
