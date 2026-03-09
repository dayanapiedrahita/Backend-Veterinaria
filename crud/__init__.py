from .usuario_crud import (
    get_usuarios,
    get_usuario_by_id,
    register_cliente,
    register_veterinario,
    login_usuario,
    create_usuario,
    update_usuario,
    delete_usuario,
)

from .cliente_crud import get_clientes, get_cliente, update_cliente, delete_cliente

from .veterinario_crud import (
    get_veterinarios,
    get_veterinario,
    update_veterinario,
    delete_veterinario,
)

from .sede_crud import get_sedes, get_sede, create_sede, update_sede, delete_sede

from .mascota_crud import (
    get_mascotas,
    get_mascota,
    create_mascota,
    update_mascota,
    delete_mascota,
)

from .vacuna_crud import (
    get_vacunas,
    get_vacuna,
    create_vacuna,
    update_vacuna,
    delete_vacuna,
)

from .cita_vacunacion_crud import (
    get_citas_vacunacion,
    get_cita_vacunacion,
    create_cita_vacunacion,
    update_cita_vacunacion,
    delete_cita_vacunacion,
)

__all__ = [
    "get_usuarios",
    "get_usuario_by_id",
    "register_cliente",
    "register_veterinario",
    "login_usuario",
    "create_usuario",
    "update_usuario",
    "delete_usuario",
    "get_clientes",
    "get_cliente",
    "update_cliente",
    "delete_cliente",
    "get_veterinarios",
    "get_veterinario",
    "update_veterinario",
    "delete_veterinario",
    "get_sedes",
    "get_sede",
    "create_sede",
    "update_sede",
    "delete_sede",
    "get_mascotas",
    "get_mascota",
    "create_mascota",
    "update_mascota",
    "delete_mascota",
    "get_vacunas",
    "get_vacuna",
    "create_vacuna",
    "update_vacuna",
    "delete_vacuna",
    "get_citas_vacunacion",
    "get_cita_vacunacion",
    "create_cita_vacunacion",
    "update_cita_vacunacion",
    "delete_cita_vacunacion",
]
