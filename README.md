# Sistema de Gestión de Vacunación Veterinaria 🐾💉

## Descripción

Este proyecto es un sistema para la gestión de una clínica veterinaria especializada en **vacunación de mascotas**.

La aplicación permite registrar mascotas, propietarios y llevar control del historial de vacunas aplicadas, así como gestionar citas de vacunación.

El objetivo del sistema es facilitar el control del esquema de vacunación de cada mascota y mejorar la organización de la clínica.

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
├── alembic/                # Configuración de migraciones de base de datos
├── crud/                   # Funciones CRUD para interactuar con la base de datos
├── endpoints/              # Rutas o endpoints de la API
├── entities/               # Modelos de base de datos (tablas)
├── migrations/             # Archivos generados por las migraciones
├── schemas/                # Esquemas de validación con Pydantic
│
├── __init__.py             # Inicialización del paquete
├── database.py             # Configuración de conexión a la base de datos
├── main.py                 # Punto de entrada de la aplicación
├── cli_menu.py             # Interfaz de línea de comandos para interacción con el sistema
│
├── alembic.ini             # Configuración de Alembic
├── requirements.txt        # Dependencias del proyecto
├── test_connection.py      # Script para probar la conexión a la base de datos
├── .gitignore              # Archivos ignorados por Git
└── README.md               # Documentación del proyecto
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

## Autor

Juan

---

## Licencia

Este proyecto se distribuye bajo la licencia MIT.
