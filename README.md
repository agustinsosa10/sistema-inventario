# Sistema de Inventario

## Descripción General

**Sistema de Inventario** es una aplicación web para gestionar inventarios, productos, movimientos de stock, ventas y proveedores. Implementa un backend robusto basado en FastAPI con autenticación segura y una arquitectura modular escalable.

---

## Estructura del Proyecto

### 📦 Backend (`/backend`)

#### **Archivos Raíz**

- **`main.py`**: Punto de entrada de la aplicación FastAPI. Configura la aplicación, importa todas las rutas de la API y las registra con sus prefijos.
- **`requirements.txt`**: Lista de dependencias del proyecto (FastAPI, SQLAlchemy, Alembic, PostgreSQL, etc.).
- **`Dockerfile`**: Configuración para construir la imagen Docker del backend.
- **`alembic.ini`**: Configuración de Alembic para manejar migraciones de base de datos.
- **`.dockerignore`**: Especifica qué archivos ignorar al construir la imagen Docker.

#### **📁 `alembic/` - Migraciones de Base de Datos**

Sistema de versionado y migraciones de esquemas de base de datos:

- **`env.py`**: Configuración del entorno para que Alembic se conecte a la base de datos.
- **`script.py.mako`**: Template de Mako para generar scripts de migración automáticamente.
- **`versions/`**: Contiene todos los scripts de migración versionados (ej: `b69f0721b80f_primera_migracion.py`). Cada archivo representa un cambio en el esquema.

#### **📁 `app/` - Código Principal de la Aplicación**

##### **`core/` - Configuración y Seguridad**

Gestiona la configuración global y funciones de seguridad:

- **`config.py`**: Define la clase `Settings` que carga variables de entorno como `DATABASE_URL`, `SECRET_KEY`, `ALGORITHM` y `ACCESS_TOKEN_EXPIRE_MINUTES`.
- **`security.py`**: Funciones de criptografía:
  - `get_password_hash()`: Genera hash de contraseñas usando bcrypt
  - `verify_password()`: Verifica contraseñas contra sus hashes
  - `create_access_token()`: Crea tokens JWT encriptados con expiración

##### **`db/` - Configuración de Base de Datos**

Gestiona la conexión y configuración de SQLAlchemy:

- **`base_class.py`**: Clase base que heredan todos los modelos ORM.
- **`base.py`**: Importa todos los modelos (registro para Alembic/SQLAlchemy). Facilita que Alembic detecte cambios en los modelos.
- **`session.py`**: Gestiona la sesión de base de datos y proporciona el generador de sesiones para las rutas.

##### **`models/` - Modelos de Base de Datos (ORM)**

Definen la estructura de las tablas y sus relaciones:

- **`operador.py`**: Representa usuarios/operadores del sistema que realiza operaciones.
- **`categoria.py`**: Categorías de productos (ej: Electrónica, Ropa, etc.).
- **`productos.py`**: Productos del inventario con campos: nombre, stock, precio, stock_minimo, fecha de creación/actualización.
- **`proveedores.py`**: Información de proveedores que suministran productos.
- **`suministro.py`**: Registra el suministro de productos por proveedores (relación entre proveedores y productos).
- **`movimientos.py`**: Registra cada movimiento de inventario con tipo (venta, restock, ajuste) y cantidad.
- **`ventas.py`**: Información de ventas realizadas.
- **`ventas_detalle.py`**: Detalles línea por línea de cada venta (qué productos se vendieron).

##### **`schemas/` - Esquemas de Validación (Pydantic)**

Define la estructura de datos para solicitudes/respuestas de la API:

- **`operador.py`**: Esquemas para autenticación (`OperadorAuth`, `OperadorLogin`).
- **`categoria.py`**: Esquemas de entrada y salida para categorías.
- **`producto.py`**: Esquemas para crear/actualizar/leer productos.
- **`proveedor.py`**: Esquemas para proveedores.
- **`suministro.py`**: Esquemas para relaciones proveedor-producto.
- **`movimiento.py`**: Esquemas para registro de movimientos de inventario.
- **`venta.py`**: Esquemas para ventas.
- **`venta_detalle.py`**: Esquemas para detalles de ventas.

Nota: Los esquemas validan los datos de entrada y documentan la API automáticamente en Swagger.

##### **`crud/` - Operaciones CRUD**

Contiene la lógica para interactuar con la base de datos:

- **`authentication.py`**: Autentica operadores (valida credenciales y retorna tokens).
- **`operador.py`**: Crear, leer, actualizar y eliminar operadores.
- **`categoria.py`**: CRUD de categorías.
- **`producto.py`**: CRUD de productos (crear productos, actualizar stock, etc.).
- **`proveedor.py`**: CRUD de proveedores.
- **`movimiento.py`**: Registrar movimientos de inventario.
- **`suministro.py`**: Gestionar relaciones proveedor-producto.
- **`venta.py`**: CRUD de ventas.

##### **`api/` - Rutas de la API**

Definen los endpoints REST:

- **`dependencies.py`**: Funciones inyectables compartidas (ej: `get_db()` para obtener sesión de BD).
- **`routes/`**: Contiene los routers de cada entidad:
  - **`auth.py`**: Endpoints de autenticación (`POST /auth/login`).
  - **`productos.py`**: Endpoints CRUD de productos.
  - **`categorias.py`**: Endpoints CRUD de categorías.
  - **`proveedores.py`**: Endpoints CRUD de proveedores.
  - **`operadores.py`**: Endpoints CRUD de operadores.
  - **`movimientos.py`**: Endpoints para registrar y consultar movimientos.
  - **`ventas.py`**: Endpoints CRUD de ventas.

##### **`services/` - Servicios de Negocio**

Carpeta actualmente vacía, disponible para lógica de negocio adicional (reportes, validaciones complejas, etc.).

---

### 🎨 Frontend (`/frontend`)

Carpeta vacía, lista para la implementación del cliente web.

---

## Tecnologías Utilizadas

| Tecnología            | Propósito                                 |
| --------------------- | ----------------------------------------- |
| **Python**            | Lenguaje principal                        |
| **FastAPI**           | Framework web moderno para APIs           |
| **SQLAlchemy**        | ORM para gestionar la base de datos       |
| **PostgreSQL**        | Base de datos relacional (vía `psycopg2`) |
| **Alembic**           | Versionado y migraciones de BD            |
| **JWT (python-jose)** | Autenticación con tokens                  |
| **bcrypt**            | Hash seguro de contraseñas                |
| **Pydantic**          | Validación de datos                       |
| **Docker**            | Contenedorización                         |
| **Uvicorn**           | Servidor ASGI para FastAPI                |

---

## Configuración y Ejecución

### 1. **Construcción de Contenedores**

```bash
docker compose build
```

### 2. **Ejecución de Contenedores**

```bash
docker compose up
```

### 3. **Migraciones de Base de Datos**

```bash
# Ver migraciones pendientes
alembic current

# Crear nueva migración automáticamente
alembic revision --autogenerate -m "Descripción del cambio"

# Aplicar migraciones
alembic upgrade head

# Revertir última migración
alembic downgrade -1
```

---

## Flujo de Datos

```
Cliente HTTP
    ↓
FastAPI (main.py)
    ↓
Rutas API (routes/)
    ↓
CRUD (operaciones BD)
    ↓
Models (ORM SQLAlchemy)
    ↓
PostgreSQL (BD)
```

---

## Endpoints Principales

| Método     | Ruta           | Descripción                     |
| ---------- | -------------- | ------------------------------- |
| `POST`     | `/auth/login`  | Autenticar operador             |
| `GET/POST` | `/productos`   | Listar/crear productos          |
| `GET/POST` | `/categorias`  | Listar/crear categorías         |
| `GET/POST` | `/proveedores` | Listar/crear proveedores        |
| `GET/POST` | `/operadores`  | Listar/crear operadores         |
| `GET/POST` | `/movimientos` | Registrar/consultar movimientos |
| `GET/POST` | `/ventas`      | Registrar/consultar ventas      |

---

## Variables de Entorno Requeridas

Crear archivo `.env` en la raíz del backend:

```env
DATABASE_URL=postgresql://usuario:contraseña@localhost/nombre_bd
SECRET_KEY=tu_clave_secreta_aqui
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
PROJECT_NAME=FastAPI-Inventario
PROJECT_VERSION=0.0.1
```

---

## Notas Importantes

- El proyecto utiliza una arquitectura **MVC modificada**: Modelos → CRUD → Rutas.
- Todos los modelos incluyen campos de auditoría: `created_at`, `updated_at`, `deleted_at` (soft delete).
- Las contraseñas se almacenan hasheadas con bcrypt, nunca en texto plano.
- Los tokens JWT expiran automáticamente según `ACCESS_TOKEN_EXPIRE_MINUTES`.
- La base de datos está versionada con Alembic, permitiendo rollback de cambios.

---

**Última actualización:** 16 de marzo de 2026
