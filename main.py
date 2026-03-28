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

from core.handlers import register_exception_handlers

import uvicorn
import os

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

# ROOT
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
    main()
