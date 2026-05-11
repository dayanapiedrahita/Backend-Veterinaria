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
    servicio_endpoint,
    factura_endpoint,
    raza_animal_endpoint,
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

# Leer orígenes permitidos desde variable de entorno (por defecto * para desarrollo)
allowed_origins = os.getenv("ALLOWED_ORIGINS", "*").split(",")

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
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
app.include_router(sede_endpoint.router, prefix="/sedes", tags=["sedes"])
app.include_router(usuario_endpoint.router, prefix="/usuarios", tags=["usuarios"])
app.include_router(cliente_endpoint.router, prefix="/clientes", tags=["clientes"])
app.include_router(veterinario_endpoint.router, prefix="/veterinarios", tags=["veterinarios"])
app.include_router(mascota_endpoint.router, prefix="/mascotas", tags=["mascotas"])
app.include_router(vacuna_endpoint.router, prefix="/vacunas", tags=["vacunas"])
app.include_router(cita_vacunacion_endpoint.router, prefix="/citas", tags=["citas"])
app.include_router(autenticar_endpoint.router, prefix="/autenticar", tags=["autenticación"])
app.include_router(servicio_endpoint.router, prefix="/servicios", tags=["servicios"])
app.include_router(factura_endpoint.router, prefix="/facturas", tags=["facturas"])
app.include_router(raza_animal_endpoint.router, prefix="/razas-animal", tags=["razas-animal"])


def main():
    uvicorn.run(
        "main:app",
        host=os.getenv("HOST", "127.0.0.1"),
        port=int(os.getenv("PORT", 8000)),
        reload=True,
    )


if __name__ == "__main__":
    main()
