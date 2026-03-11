from app.db import base
from fastapi import FastAPI
from app.core.config import settings
from app.api.routes import productos
from app.api.routes import categorias
from app.api.routes import proveedores
from app.api.routes import operadores


app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)


app.include_router(productos.router, prefix="/products", tags=["Etiquetas (productos)"])
app.include_router(
    categorias.router, prefix="/categories", tags=["Etiquetas (categorias)"]
)
app.include_router(
    operadores.router, prefix="/operadores", tags=["Etiquetas (operadores)"]
)
app.include_router(
    proveedores.router, prefix="/proveedores", tags=["Etiquetas (proveedores)"]
)
