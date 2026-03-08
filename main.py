from fastapi import FastAPI
from endpoints import (
    sede_endpoint,
    usuario_endpoint,
    cliente_endpoint,
    veterinario_endpoint,
    mascota_endpoint,
    vacuna_endpoint,
    cita_vacunacion_endpoint
)
from database import Base, engine
from entities import *

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(sede_endpoint.router)
app.include_router(usuario_endpoint.router)
app.include_router(cliente_endpoint.router)
app.include_router(veterinario_endpoint.router)
app.include_router(mascota_endpoint.router)
app.include_router(vacuna_endpoint.router)
app.include_router(cita_vacunacion_endpoint.router)
import uvicorn
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from endpoints import (
    sede_endpoint,
    usuario_endpoint,
    cliente_endpoint,
    veterinario_endpoint,
    mascota_endpoint,
    vacuna_endpoint,
    cita_vacunacion_endpoint,
    autenticar_endpoint,
)
from database import Base, engine, create_tables
from entities import *


app = FastAPI(
    title="Sistema de Gestión de Veterinaria",
    description="API REST para la veterinaria (adaptada del proyecto de ejemplo)",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



def _init_db():
    """Initialize database tables on startup"""
    print("Creando/actualizando tablas de la base de datos...")
    create_tables()
    print("API lista - documentación disponible en http://localhost:8000/docs")

_init_db()


@app.get("/", tags=["raíz"])
async def root():
    return {
        "mensaje": "Bienvenido a la API de Veterinaria",
        "version": "1.0.0",
        "documentacion": "/docs",
        "redoc": "/redoc",
        "endpoints": {
            "Sedes": "/sedes",
            "Usuarios": "/usuarios",
            "Clientes": "/clientes",
            "Veterinarios": "/veterinarios",
            "Mascotas": "/mascotas",
            "Vacunas": "/vacunas",
            "Citas": "/citas_vacunacion",
        },
    }


app.include_router(sede_endpoint.router)
app.include_router(usuario_endpoint.router)
app.include_router(cliente_endpoint.router)
app.include_router(veterinario_endpoint.router)
app.include_router(mascota_endpoint.router)
app.include_router(vacuna_endpoint.router)
app.include_router(cita_vacunacion_endpoint.router)
app.include_router(autenticar_endpoint.router)


def main():
    print("Ejecutando servidor FastAPI...")
    uvicorn.run(
        "main:app",
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", 8000)),
        reload=True,
        log_level="info",
    )



if __name__ == "__main__":
    main()
    