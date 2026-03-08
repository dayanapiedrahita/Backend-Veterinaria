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

# Ruta principal
@app.get("/")
def root():
    return {
        "mensaje": "API Veterinaria funcionando",
        "documentacion": "/docs"
    }

app.include_router(sede_endpoint.router)
app.include_router(usuario_endpoint.router)
app.include_router(cliente_endpoint.router)
app.include_router(veterinario_endpoint.router)
app.include_router(mascota_endpoint.router)
app.include_router(vacuna_endpoint.router)
app.include_router(cita_vacunacion_endpoint.router)