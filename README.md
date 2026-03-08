# Backend-Veterinaria

Sistema de información para una Veterinaria.

## Descripción

Este proyecto expone una API REST construida con FastAPI, inspirada en la estructura del proyecto de ejemplo "Veterinaria El Zancudo".

## Características principales

- Rutas CRUD para sedes, usuarios, clientes, veterinarios, mascotas, vacunas y citas de vacunación.
- Autenticación básica que devuelve un token simulado.
- Documentación automática en `/docs` y `/redoc`.
- Configuración de base de datos mediante variable de entorno `DATABASE_URL` (.env soportado).
- CORS habilitado para permitir peticiones desde cualquier origen en desarrollo.

## Instalación

1. Crear y activar un entorno virtual de Python.
2. Instalar dependencias:
   ```sh
   pip install -r requirements.txt
   ```
3. Crear un archivo `.env` en la raíz con la cadena de conexión a la base de datos:
   ```
   DATABASE_URL="postgresql+psycopg2://usuario:pass@host:port/dbname"
   ```
   (ya se incluye un `.env` de ejemplo en el repositorio). 

## Arrancar el servidor

    python main.py

El servidor arrancará en `http://localhost:8000` y mostrará los endpoints disponibles en la ruta raíz y en `/docs`.

## Ejemplo de uso

- `POST /autenticar/login` para iniciar sesión con el email de un usuario registrado.
- `GET /usuarios/total` para obtener el número de usuarios.
- CRUD en `/sedes`, `/clientes`, `/mascotas`, etc.

Puedes consultar los esquemas de datos en los archivos `schemas/*.py`.

