from pydantic import BaseModel, field_validator
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

    # no colocamos la pass aca por que no queremos devolverla en una respuesta de la api


# los datos que queremos que nos retorne la api + los de operadorbase, no devolvemos la contrasñea por que no esta en el modelo base
class Operador(OperadorBase):
    id: int
    email: str
    # created_at: datetime
    # updated_at: Optional[datetime] = None
    # deleted_at: Optional[datetime] = None

    class Config:
        from_attributes: True


# los datos que vamos a enviar a la api, en este caso los de operadorbase y la contraseña
class OperadorCreate(OperadorBase):
    password: str
    rol: RolOperador
    email: str

    @field_validator("password")
    @classmethod
    def password_min_length(cls, v):
        if len(v) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres")
        return v


class OperadorLogin(BaseModel):
    email: str
    password: str


class OperadorAuth(OperadorBase):
    rol: RolOperador
    token: str

    class Config:
        from_attributes: True


class OperadorUpdate(BaseModel):
    nombre: str = None
    rol: RolOperador = None
    email: str = None
    password: str = None
