# Backend-Veterinaria

## Descripción del Proyecto

Este es un backend completo para un sistema de gestión de una veterinaria, desarrollado con **FastAPI** y **SQLAlchemy**. El proyecto permite gestionar sedes, usuarios, clientes, veterinarios, mascotas, vacunas y citas de vacunación a través de una API RESTful. Está diseñado para ser escalable, modular y fácil de mantener.

El sistema incluye autenticación básica, operaciones CRUD completas para todas las entidades, y documentación automática generada por FastAPI. Está inspirado en el proyecto de ejemplo "Veterinaria El Zancudo", pero adaptado y expandido para cubrir todas las funcionalidades necesarias en una veterinaria moderna.

## Tecnologías Utilizadas

- **FastAPI**: Framework web moderno y rápido para construir APIs con Python.
- **SQLAlchemy**: ORM para interactuar con la base de datos de manera eficiente.
- **PostgreSQL**: Base de datos relacional utilizada para almacenar los datos.
- **Pydantic**: Para validación de datos y serialización.
- **Alembic**: Para migraciones de base de datos.
- **Uvicorn**: Servidor ASGI para ejecutar la aplicación.
- **Python 3.8+**: Versión de Python requerida.

## Arquitectura del Proyecto

El proyecto sigue una arquitectura limpia y modular, separando responsabilidades en diferentes capas:

- **Capa de Presentación (Endpoints)**: Routers de FastAPI que manejan las rutas HTTP.
- **Capa de Servicio (CRUD)**: Lógica de negocio para operaciones de base de datos.
- **Capa de Datos (Entities/Schemas)**: Modelos de base de datos y esquemas de validación.
- **Capa de Infraestructura**: Configuración de base de datos, migraciones, etc.

## Estructura de Archivos

```
Backend-Veterinaria/
├── main.py                 # Punto de entrada de la aplicación
├── database.py             # Configuración de la base de datos
├── cli_menu.py             # Menú de línea de comandos (opcional)
├── test_connection.py      # Script para probar conexión a DB
├── requirements.txt        # Dependencias del proyecto
├── alembic/                # Migraciones de base de datos
│   ├── env.py
│   ├── script.py.mako
│   └── versions/           # Archivos de migración
├── entities/               # Modelos de SQLAlchemy
│   ├── __init__.py
│   ├── sede.py
│   ├── usuario.py
│   ├── cliente.py
│   ├── veterinario.py
│   ├── mascota.py
│   ├── vacuna.py
│   └── cita_vacunacion.py
├── schemas/                # Esquemas de Pydantic
│   ├── __init__.py
│   ├── sede_schema.py
│   ├── usuario_schema.py
│   ├── cliente_schema.py
│   ├── veterinario_schema.py
│   ├── mascota_schema.py
│   ├── vacuna_schema.py
│   └── cita_vacunacion_schema.py
├── crud/                   # Operaciones CRUD
│   ├── __init__.py
│   ├── sede_crud.py
│   ├── usuario_crud.py
│   ├── cliente_crud.py
│   ├── veterinario_crud.py
│   ├── mascota_crud.py
│   ├── vacuna_crud.py
│   └── cita_vacunacion_crud.py
├── endpoints/              # Routers de FastAPI
│   ├── __init__.py
│   ├── sede_endpoint.py
│   ├── usuario_endpoint.py
│   ├── cliente_endpoint.py
│   ├── veterinario_endpoint.py
│   ├── mascota_endpoint.py
│   ├── vacuna_endpoint.py
│   ├── cita_vacunacion_endpoint.py
│   └── autenticar_endpoint.py
└── README.md               # Este archivo
```

## Instalación y Configuración

### Prerrequisitos

- Python 3.8 o superior
- PostgreSQL instalado y ejecutándose
- Una base de datos PostgreSQL creada

### Pasos de Instalación

1. **Clona el repositorio** (si aplica) o navega al directorio del proyecto.

2. **Crea un entorno virtual**:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # En Windows
   # source venv/bin/activate  # En Linux/Mac
   ```

3. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura la base de datos**:
   - Crea un archivo `.env` en la raíz del proyecto con la siguiente variable:
     ```
     DATABASE_URL=postgresql+psycopg2://usuario:password@localhost:5432/nombre_db
     ```
   - Reemplaza `usuario`, `password`, `localhost`, `5432` y `nombre_db` con tus credenciales reales.

5. **Ejecuta las migraciones** para crear las tablas:
   ```bash
   alembic upgrade head
   ```

## Ejecución del Proyecto

Para iniciar el servidor de desarrollo:

```bash
python main.py
```

El servidor se ejecutará en `http://localhost:8000` por defecto. Puedes cambiar el host y puerto mediante variables de entorno `HOST` y `PORT`.

### Documentación de la API

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`
- **Raíz**: `http://localhost:8000/` (muestra información general)

## Video Demostración

En este video se evidencia la ejecución del pipeline CI/CD y la creación de tablas/campos en la base de datos:

**[Enlace al video - Agregar aquí]**

En el video se muestra:
- ✅ Ejecución del pipeline en GitHub Actions (rama dev)
- ✅ Ejecución de migraciones con Alembic (`alembic upgrade head`)
- ✅ Ejecución del seeder idempotente (`python scripts/seed.py`)
- ✅ Tablas y datos creados en PostgreSQL

## Endpoints Principales

### Protección de Endpoints

**Endpoints Públicos (GET)** - No requieren autenticación:
- `GET /sedes`, `GET /sedes/{id}`
- `GET /usuarios/{id}`
- `GET /clientes`, `GET /clientes/{id}`
- `GET /veterinarios`, `GET /veterinarios/{id}`
- `GET /mascotas`, `GET /mascotas/{id}`
- `GET /vacunas`, `GET /vacunas/{id}`
- `GET /citas_vacunacion`, `GET /citas_vacunacion/{id}`

**Endpoints Protegidos (POST/PUT/DELETE)** - Requieren JWT token en header `Authorization: Bearer <token>`:
- Crear/Actualizar/Eliminar: sedes, clientes, veterinarios, mascotas, vacunas, citas
- Registrar: `/usuarios/registro/cliente`, `/usuarios/registro/veterinario`

### Autenticación (JWT)
- `POST /autenticar/login`: Iniciar sesión con email y obtener JWT token
  - Request: `{"email": "usuario@email.com"}`
  - Response: `{"token": "eyJ0eXAiOiJKV1QiLCJhbGc...", "usuario": {...}}`
  - Token válido por 30 minutos

### Configuración JWT:
- **Algoritmo**: HS256
- **Expiración**: 30 minutos
- **Header requerido**: `Authorization: Bearer <token>`
- **Buena práctica**: SECRET_KEY se configura en variables de entorno

### Flujo de autenticación:
1. Cliente envía POST a `/autenticar/login` con su email
2. Servidor valida email y genera JWT token válido por 30 minutos
3. Cliente incluye el token en header para operaciones protegidas
4. Servidor valida token en endpoints POST/PUT/DELETE; rechaza con 401 si es inválido o expirado

### Ejemplo de login:
```bash
curl -X POST "http://localhost:8000/autenticar/login" \
  -H "Content-Type: application/json" \
  -d '{"email": "juan.garcia@email.com"}'
```

### Usando el token en operaciones protegidas:
```bash
curl -X POST "http://localhost:8000/sedes" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc..." \
  -d '{"nombre": "Sede Este", "direccion": "Calle 50", "telefono": "3001111111"}'
```

### Sedes
- `GET /sedes`: Listar todas las sedes
- `POST /sedes`: Crear nueva sede (⭐ Protegido)
- `GET /sedes/{id}`: Obtener sede por ID
- `PUT /sedes/{id}`: Actualizar sede (⭐ Protegido)
- `DELETE /sedes/{id}`: Eliminar sede (⭐ Protegido)

### Usuarios
- `GET /usuarios/{id}`: Obtener usuario por ID
- `POST /usuarios/registro/cliente`: Registrar nuevo cliente (⭐ Protegido)
- `POST /usuarios/registro/veterinario`: Registrar nuevo veterinario (⭐ Protegido)

### Clientes
- `GET /clientes`: Listar clientes
- `GET /clientes/{id}`: Obtener cliente
- `PUT /clientes/{id}`: Actualizar cliente (⭐ Protegido)
- `DELETE /clientes/{id}`: Eliminar cliente (⭐ Protegido)

### Veterinarios
- `GET /veterinarios`: Listar veterinarios
- `GET /veterinarios/{id}`: Obtener veterinario
- `PUT /veterinarios/{id}`: Actualizar veterinario (⭐ Protegido)
- `DELETE /veterinarios/{id}`: Eliminar veterinario (⭐ Protegido)

### Mascotas
- `GET /mascotas`: Listar mascotas
- `GET /mascotas/{id}`: Obtener mascota
- `POST /mascotas`: Crear mascota (⭐ Protegido)
- `PUT /mascotas/{id}`: Actualizar mascota (⭐ Protegido)
- `DELETE /mascotas/{id}`: Eliminar mascota (⭐ Protegido)

### Vacunas
- `GET /vacunas`: Listar vacunas
- `GET /vacunas/{id}`: Obtener vacuna
- `POST /vacunas`: Crear vacuna (⭐ Protegido)
- `PUT /vacunas/{id}`: Actualizar vacuna (⭐ Protegido)
- `DELETE /vacunas/{id}`: Eliminar vacuna (⭐ Protegido)

### Citas de Vacunación
- `GET /citas_vacunacion`: Listar citas
- `GET /citas_vacunacion/{id}`: Obtener cita
- `POST /citas_vacunacion`: Crear cita (⭐ Protegido)
- `PUT /citas_vacunacion/{id}`: Actualizar cita (⭐ Protegido)
- `DELETE /citas_vacunacion/{id}`: Eliminar cita (⭐ Protegido)

## CORS (Cross-Origin Resource Sharing)

La API está configurada con CORS para permitir el consumo desde aplicaciones frontend en diferentes orígenes. Esta es una configuración crítica de seguridad que debe adaptarse según el entorno.

### Política CORS Actual (Desarrollo)

**⚠️ IMPORTANTE**: El backend está actualmente configurado con CORS abierto a cualquier origen:
```python
allow_origins=["*"]  # ⚠️ Permite cualquier origen (SOLO DESARROLLO)
allow_methods=["*"]  # Permite cualquier método HTTP
allow_headers=["*"]  # Permite cualquier header
```

Esta configuración se encuentra en [main.py](main.py#L35-L40) y es **INSEGURA para producción**.

### Configuración mediante Variables de Entorno

Para controlar los orígenes permitidos, se recomienda usar una variable de entorno `ALLOWED_ORIGINS`.

#### 1. Añade a tu archivo `.env`:

**Para desarrollo** (permite localhost):
```
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:4200,http://localhost:8080
```

**Para producción** (dominios específicos):
```
ALLOWED_ORIGINS=https://midominio.com,https://www.midominio.com,https://app.midominio.com
```

#### 2. Uso en `main.py`:

```python
import os
from fastapi.middleware.cors import CORSMiddleware

# Leer orígenes permitidos desde variable de entorno
allowed_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)
```

### Orígenes Recomendados por Entorno

**Desarrollo**:
```
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:4200,http://localhost:8080,http://127.0.0.1:3000
```

**Staging/Testing**:
```
ALLOWED_ORIGINS=https://staging.midominio.com,https://testing.midominio.com
```

**Producción**:
```
ALLOWED_ORIGINS=https://midominio.com,https://www.midominio.com
```

### Métodos HTTP Permitidos

La API permite los siguientes métodos HTTP necesarios para operaciones CRUD:
- `GET`: Obtener datos
- `POST`: Crear datos
- `PUT`: Actualizar datos
- `DELETE`: Eliminar datos
- `OPTIONS`: Preflight de navegador

### Headers CORS Requeridos

Los siguientes headers son permitidos para todas las peticiones:
- `Content-Type`: Especifica el tipo de contenido (application/json)
- `Authorization`: Para enviar el JWT token en formato `Bearer <token>`

### Verificación de CORS

Para verificar que CORS está correctamente configurado, prueba una petición desde tu frontend:

```javascript
// JavaScript/Fetch
const response = await fetch('http://localhost:8000/sedes', {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
    }
});
```

Si CORS está correctamente configurado, la petición será exitosa. Si no, verás un error en la consola del navegador:
```
Access to XMLHttpRequest at 'http://localhost:8000/sedes' 
from origin 'http://localhost:3000' has been blocked by CORS policy
```

## Carpeta Core y Manejo de Errores

La carpeta `core/` centraliza funcionalidades transversales de la aplicación:

### Estructura:
- **`exceptions.py`**: Excepciones personalizadas (NotFoundException, BadRequestException, ConflictException)
- **`handlers.py`**: Manejadores globales de excepciones en FastAPI
- **`security.py`**: Utilidades de seguridad (JWT, hashing de contraseñas)
- **`dependencies.py`**: Dependencias reutilizables (validación de JWT)

### Respuestas de error homogéneas:
Todos los errores retornan formato consistente:
```json
{
  "error": "Descripción del error"
}
```

Códigos HTTP utilizados:
- `404 Not Found`: Recurso no encontrado
- `400 Bad Request`: Solicitud inválida
- `409 Conflict`: Conflicto en los datos
- `401 Unauthorized`: Token inválido o expirado

## Seeder de Base de Datos

El proyecto incluye un script seeder idempotente que crea datos iniciales de demostración.

### Ejecutar seeder manualmente:
```bash
python scripts/seed.py
```

### Datos que crea:
- 3 sedes de veterinaria
- 5 vacunas disponibles
- 3 veterinarios registrados
- 4 clientes de prueba
- 4 mascotas de ejemplo

**Nota**: El seeder solo ejecuta si la BD está vacía (seguro contra ejecuciones repetidas).

## Base de Datos

### Modelo de Datos

El sistema utiliza PostgreSQL con las siguientes tablas principales:

- **usuario**: Información de usuarios (clientes y veterinarios)
- **cliente**: Datos específicos de clientes
- **veterinario**: Datos específicos de veterinarios
- **sede**: Ubicaciones de la veterinaria
- **mascota**: Información de las mascotas
- **vacuna**: Tipos de vacunas disponibles
- **cita_vacunacion**: Registro de citas para vacunación

### Migraciones

Las migraciones se manejan con Alembic. Para crear una nueva migración después de cambios en los modelos:

```bash
alembic revision --autogenerate -m "Descripción del cambio"
alembic upgrade head
```

## Pruebas

Para probar la conexión a la base de datos:

```bash
python test_connection.py
```

## Notas Adicionales

- ✅ **Autenticación JWT real** implementada con tokens seguros, expiración y validación en endpoints protegidos
- ✅ **Manejo centralizado de errores** mediante carpeta `core/` con excepciones personalizadas y handlers globales
- ✅ **CORS configurado** para desarrollo (abierto); requiere restricción en producción
- ✅ **Seeder idempotente** que evita duplicados en ejecuciones repetidas
- ✅ **Migraciones con Alembic** para versionado de esquema
- ✅ **Pipeline CI/CD**: Configurado en `.github/workflows/ci.yml` con integración a BD, linting, tests y seeder
- Los esquemas de Pydantic validan automáticamente los datos de entrada y salida
- El proyecto está diseñado para ser extensible; puedes agregar nuevos endpoints o entidades siguiendo la estructura existente

## Contribución

1. Crea una rama para tu feature: `git checkout -b feature/nueva-funcionalidad`
2. Realiza tus cambios y commits.
3. Envía un Pull Request con descripción detallada.

## Licencia

Este proyecto es de uso educativo y puede ser modificado según necesidades.

