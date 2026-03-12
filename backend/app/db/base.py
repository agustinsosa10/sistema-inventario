# este archivo lo que hace es agrupar todas las entidades
# es el archivo que dice cuales son las entidades de la base de datos
# Este archivo cumple un rol de registro de modelos para Alembic/SQLAlchemy
from app.db.base_class import Base
from app.models.operador import Operador
from app.models.categoria import Categoria
from app.models.productos import Productos
from app.models.proveedores import Proveedores
from app.models.movimientos import Movimientos
from app.models.suministro import Suministro
from app.models.ventas import Ventas
from app.models.ventas_detalle import VentasDetalle
