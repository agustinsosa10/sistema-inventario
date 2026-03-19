# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

### Running the application

```bash
# Build and start the backend (Docker)
docker compose build
docker compose up

# API available at http://localhost:8000
# Interactive docs at http://localhost:8000/docs
```

### Database migrations (run inside the backend container or with venv active)

```bash
alembic current                                      # Check current revision
alembic revision --autogenerate -m "description"     # Generate migration
alembic upgrade head                                 # Apply all pending migrations
alembic downgrade -1                                 # Roll back one migration
```

### Environment setup

Requires a `.env` file at the project root with:

```
DATABASE_URL=postgresql+psycopg2://user:password@host:port/dbname
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=480
```

## Architecture

### Backend: FastAPI + SQLAlchemy + PostgreSQL

The backend lives in `backend/` and follows a layered pattern:

```
HTTP Request → main.py (router registration)
             → api/routes/<entity>.py  (FastAPI endpoints)
             → crud/<entity>.py        (database operations)
             → models/<entity>.py      (SQLAlchemy ORM models)
             → PostgreSQL
```

**`app/main.py`** — Entry point. Registers all routers with their URL prefixes.

**`app/core/`**
- `config.py` — Settings loaded from `.env` via pydantic-settings (DATABASE_URL, SECRET_KEY, ALGORITHM, token expiration)
- `security.py` — bcrypt password hashing (`get_password_hash`, `verify_password`) and JWT creation

**`app/db/`**
- `session.py` — SQLAlchemy engine and `SessionLocal` factory
- `base_class.py` — `Base` class all models inherit from
- `base.py` — Imports all models so Alembic can detect them for autogenerate

**`app/api/dependencies.py`** — Two key dependencies injected into routes:
- `get_db()` — Yields a DB session per request
- `verificar_token()` — Decodes JWT, returns the authenticated `Operador` object (raises 401 if invalid)

### Data models

All models include `created_at`, `updated_at`, and `deleted_at` (soft deletes).

| Model | Description |
|---|---|
| `Operador` | System users; roles: `admin` or `operador` |
| `Categoria` | Product categories |
| `Producto` | Inventory items with `stock` and `stock_minimo` |
| `Proveedor` | Suppliers |
| `Suministro` | Product↔Supplier link with `precio_unitario`; composite PK |
| `Movimiento` | Inventory movements; tipos: `venta`, `restock`, `ajuste` |
| `Venta` | Sale header with total |
| `VentaDetalle` | Sale line items (producto, cantidad, precio_unitario) |

### Authentication

- `POST /auth/login` accepts email + password, returns `{"token": ..., "rol": ..., "nombre": ...}`
- JWT payload: `{"sub": email, "rol": rol, "exp": expiration}`
- All CRUD endpoints use `current_user = Depends(verificar_token)` to enforce authentication

### Route structure

Routes are registered in `main.py` with these prefixes:
`/auth`, `/productos`, `/categorias`, `/operadores`, `/proveedores`, `/movimientos`, `/ventas`

Each entity follows the same CRUD pattern: `GET /`, `POST /`, `GET /{id}`, `PUT /{id}`, `DELETE /{id}` (soft delete).

### Schemas

Pydantic schemas in `app/schemas/` validate request bodies and shape responses. Each entity typically has `Base`, `Create`, `Update`, and `Read`/`InDB` variants.

## Pending work (as of March 2026)

- Integrate `verificar_token` into ventas routes so the authenticated operator is recorded on each sale
- Frontend (`frontend/`) not yet implemented
