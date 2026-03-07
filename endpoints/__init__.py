from .sede_endpoint import router as sede_router
from .usuario_endpoint import router as usuario_router
from .cliente_endpoint import router as cliente_router
from .veterinario_endpoint import router as veterinario_router
from .mascota_endpoint import router as mascota_router
from .vacuna_endpoint import router as vacuna_router
from .cita_vacunacion_endpoint import router as cita_vacunacion_router

__all__ = [
    "sede_router",
    "usuario_router",
    "cliente_router",
    "veterinario_router",
    "mascota_router",
    "vacuna_router",
    "cita_vacunacion_router"
]