#LINK DEL FRONTEND: https://github.com/lincoln20900/frontend-aplicaciones-y-servicios.git

# Sistema de Gestión de Vacunación Veterinaria 

## Descripción

Este proyecto es un sistema para la gestión de una clínica veterinaria especializada en **vacunación de mascotas**.

La aplicación permite registrar mascotas, propietarios y llevar control del historial de vacunas aplicadas, así como gestionar citas de vacunación.

El objetivo del sistema es facilitar el control del esquema de vacunación de cada mascota y mejorar la organización de la clínica.

En cuanto a los pipelines, el proyecto está preparado para integrarse con flujos de integración continua y despliegue continuo (CI/CD). Gracias a la configuración de GitHub Actions (.github/workflows/ci.yml), cada cambio en el código dispara automáticamente un pipeline que:

Instala las dependencias definidas en requirements.txt.
Ejecuta linting con flake8 para asegurar que el código cumple con los estándares de estilo y calidad.
Corre todos los tests unitarios e integrales con pytest para verificar que las funcionalidades principales del sistema no se rompan.
Puede auditar dependencias con pip-audit para detectar vulnerabilidades antes de desplegar.

En conjunto, estos pipelines permiten mantener la estabilidad del proyecto, detectar errores rápidamente y preparar el entorno para despliegues seguros y consistentes, minimizando riesgos al integrar nuevos cambios.

---

## Tecnologías utilizadas

* Python
* FastAPI
* SQLAlchemy
* Alembic (migraciones de base de datos)
* Base de datos relacional
* Git y GitHub

---

## Estructura del proyecto

```bash
project/
│
Backend-Veterinaria/
├── .github/
│   └── workflows/
│       └── ci.yml
├── .venv/
├── alembic/
├── core/
├── crud/
├── endpoints/
├── entities/
├── migrations/
├── schemas/
├── scripts/
├── tests/
├── venv/
├── __init__.py
├── .env
├── .gitignore
├── alembic.ini
├── cli_menu.py
├── database.py
├── Dockerfile
├── main.py
├── README.md
├── requirements.txt
└── test_connection.py
```

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/usuario/proyecto-veterinaria.git
cd proyecto-veterinaria
```

### 2. Crear entorno virtual

```bash
python -m venv venv
```

### 3. Activar entorno virtual

Windows:

```bash
venv\Scripts\activate
```

Linux o Mac:

```bash
source venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Configuración de la base de datos

Para ejecutar las migraciones con Alembic:

```bash
alembic upgrade head
```

Para crear una nueva migración:

```bash
alembic revision --autogenerate -m "descripcion_del_cambio"
```

---

## Ejecutar la aplicación

Para iniciar el servidor:

```bash
uvicorn main:app --reload
```

Luego abrir en el navegador:

```
http://127.0.0.1:8000
```

Documentación automática de la API:

```
http://127.0.0.1:8000/docs
```

---

## Funcionalidades del sistema

* Registro de propietarios de mascotas
* Registro de mascotas
* Registro de vacunas aplicadas
* Gestión de citas de vacunación
* Consulta del historial de vacunación

---

## Autores

Juan Felipe Ospina Agudelo

Lincon Andres Palacios

video de la segunda entrega :
https://youtu.be/4biNLPlJvhY

## Licencia

Este proyecto se distribuye bajo la licencia MIT.
