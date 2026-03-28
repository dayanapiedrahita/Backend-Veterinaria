from fastapi import FastAPI
 Feat--Pipeline

from endpoints import (
    sede_endpoint,
    usuario_endpoint,
    cliente_endpoint,
    veterinario_endpoint,
    mascota_endpoint,
    vacuna_endpoint,
    cita_vacunacion_endpoint,
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
 dev
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

 Feat--Pipeline
from core.handlers import register_exception_handlers

import uvicorn
import os


 dev
app = FastAPI(
    title="Sistema de Gestión de Veterinaria",
    description="API REST para la veterinaria",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# 🔥 REGISTRAR HANDLERS (IMPORTANTE)
register_exception_handlers(app)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

 Feat--Pipeline
# ROOT


def _init_db():
    """Initialize database tables on startup"""
    print("Creando/actualizando tablas de la base de datos...")
    create_tables()
    print("API lista - documentación disponible en http://localhost:8000/docs")


_init_db()


 dev
@app.get("/", tags=["raíz"])
async def root():
    return {
        "mensaje": "Bienvenido a la API de Veterinaria",
        "version": "1.0.0",
        "docs": "/docs",
    }

# ROUTERS
app.include_router(sede_endpoint.router)
app.include_router(usuario_endpoint.router)
app.include_router(cliente_endpoint.router)
app.include_router(veterinario_endpoint.router)
app.include_router(mascota_endpoint.router)
app.include_router(vacuna_endpoint.router)
app.include_router(cita_vacunacion_endpoint.router)
app.include_router(autenticar_endpoint.router)


def main():
    uvicorn.run(
        "main:app",
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", 8000)),
        reload=True,
    )


if __name__ == "__main__":
 Feat--Pipeline
    main()

    main()
 dev
