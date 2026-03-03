from pydantic import BaseModel


# que herede basemodel le indica a python que tiene validacion de datos
# definimos los tipos de los atributos que contiene la clase
class SuministroBase(BaseModel):
    pass


# aca definimos que queremos que nos retorne la api
class Suministro(SuministroBase):
    producto_id: int
    proveedor_id: int

    # convierte los datos del objeto en json
    class Config:
        from_atributtes: True


# que es lo que le vamos a mandar a la api
class SuministroCreate(SuministroBase):
    producto_id: int
    proveedor_id: int
