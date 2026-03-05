from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# que herede basemodel le indica a python que tiene validacion de datos
# definimos los tipos de los atributos que contiene la clase
class CategoriaBase(BaseModel):
    nombre: str


# datos que nos retorna la api + los de categoriabase
class Categoria(CategoriaBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted: Optional[datetime] = None

    # transforma el objeto a json
    class Config:
        from_attributes: True


# datos que enviamos a la api, en este caso los de categoriabase
class CategoriaCreate(CategoriaBase):
    pass
