validacion de datos de las tablas de datos

BaseModel -> le dice a python que esa clase sirve para validacion

class xBase(BaseModel ) -> x es un validador de datos
atributo1: int
atributo2: str

class x (xBase) -> esta clase es lo que queremos que nos retorne la api
id:int
#como estamos heredando xBase nos va a retornar los datos de xBase + id

class xCreate(xBase) -> aca definimos los datos que queremos mandar
pass -> con esto decimos que no hay otros atributos mas que los de xBase
