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

## Endpoints Principales

### Autenticación (JWT)
- `POST /autenticar/login`: Iniciar sesión con email y obtener JWT token
  - Request: `{"email": "usuario@email.com"}`
  - Response: `{"token": "eyJ0eXAiOiJKV1QiLCJhbGc...", "usuario": {...}}`
  - Token válido por 30 minutos

### Sedes
- `GET /sedes`: Listar todas las sedes
- `POST /sedes`: Crear nueva sede
- `GET /sedes/{id}`: Obtener sede por ID
- `PUT /sedes/{id}`: Actualizar sede
- `DELETE /sedes/{id}`: Eliminar sede

### Usuarios
- `GET /usuarios/total`: Obtener número total de usuarios
- `GET /usuarios/email/{email}`: Obtener usuario por email
- `GET /usuarios/{id}`: Obtener usuario por ID
- `POST /usuarios/registro/cliente`: Registrar nuevo cliente
- `POST /usuarios/registro/veterinario`: Registrar nuevo veterinario

### Clientes
- `GET /clientes`: Listar clientes
- `POST /clientes`: Crear cliente
- `GET /clientes/{id}`: Obtener cliente
- `PUT /clientes/{id}`: Actualizar cliente
- `DELETE /clientes/{id}`: Eliminar cliente

### Veterinarios
- `GET /veterinarios`: Listar veterinarios
- `POST /veterinarios`: Crear veterinario
- `GET /veterinarios/{id}`: Obtener veterinario
- `PUT /veterinarios/{id}`: Actualizar veterinario
- `DELETE /veterinarios/{id}`: Eliminar veterinario

### Mascotas
- `GET /mascotas`: Listar mascotas
- `POST /mascotas`: Crear mascota
- `GET /mascotas/{id}`: Obtener mascota
- `PUT /mascotas/{id}`: Actualizar mascota
- `DELETE /mascotas/{id}`: Eliminar mascota

### Vacunas
- `GET /vacunas`: Listar vacunas
- `POST /vacunas`: Crear vacuna
- `GET /vacunas/{id}`: Obtener vacuna
- `PUT /vacunas/{id}`: Actualizar vacuna
- `DELETE /vacunas/{id}`: Eliminar vacuna

### Citas de Vacunación
- `GET /citas_vacunacion`: Listar citas
- `POST /citas_vacunacion`: Crear cita
- `GET /citas_vacunacion/{id}`: Obtener cita
- `PUT /citas_vacunacion/{id}`: Actualizar cita
- `DELETE /citas_vacunacion/{id}`: Eliminar cita

## Autenticación JWT

La API utiliza **JSON Web Tokens (JWT)** para autenticación segura.

### Flujo de autenticación:
1. Cliente envía POST a `/autenticar/login` con su email
2. Servidor valida y genera un JWT token válido por 30 minutos
3. Cliente incluye el token en header `Authorization: Bearer <token>`
4. Servidor valida token en cada solicitud protegida

### Ejemplo de login:
```bash
curl -X POST "http://localhost:8000/autenticar/login" \
  -H "Content-Type: application/json" \
  -d '{"email": "juan.garcia@email.com"}'
```

### Usando el token:
```bash
curl -X GET "http://localhost:8000/usuarios/total" \
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc..."
```

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

- El sistema incluye CORS habilitado para desarrollo.
- La autenticación actual es básica y simula tokens; en producción, implementa JWT o similar.
- Los esquemas de Pydantic validan automáticamente los datos de entrada y salida.
- El proyecto está diseñado para ser extensible; puedes agregar nuevos endpoints o entidades siguiendo la estructura existente.

## Contribución

1. Crea una rama para tu feature: `git checkout -b feature/nueva-funcionalidad`
2. Realiza tus cambios y commits.
3. Envía un Pull Request con descripción detallada.

## Licencia

Este proyecto es de uso educativo y puede ser modificado según necesidades.

