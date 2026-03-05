from app.db import base
from fastapi import FastAPI
from app.core.config import settings
from app.api.routes import productos


app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)


app.include_router(productos.router, prefix="/products", tags=["Etiquetas (productos)"])
