# Base es una clase constructora, que sirve para que las clases que tenga se conviertan en tablas de la base de datos. Ejemplo class Producto(Base) <- hereda Base por ende se convierte en una tabla de la base de datos
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    @declared_attr
    # aca lo que hacemos es decirle a la base de datos que el nombre de la tabla va a ser el de la clase pero en minuscula ejemplo class Producto -> en la db "producto"
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
