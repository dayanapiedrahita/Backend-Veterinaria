# USUARIO
from .usuario_crud import (
    get_usuarios,
    get_usuario_by_id,
    get_usuario_by_email,
    register_cliente,
    register_veterinario,
    login_usuario,
    create_usuario,
    update_usuario,
    delete_usuario,
)

# CLIENTE
from .cliente_crud import (
    get_clientes,
    get_cliente,
    update_cliente,
    delete_cliente
)

# VETERINARIO
from .veterinario_crud import (
    get_veterinarios,
    get_veterinario,
    update_veterinario,
    delete_veterinario,
)

# SEDE
from .sede_crud import (
    get_sedes,
    get_sede,
    create_sede,
    update_sede,
    delete_sede
)

# MASCOTA
from .mascota_crud import (
    get_mascotas,
    get_mascota,
    create_mascota,
    update_mascota,
    delete_mascota
)

# VACUNA
from .vacuna_crud import (
    get_vacunas,
    get_vacuna,
    create_vacuna,
    update_vacuna,
    delete_vacuna
)

# CITA VACUNACIÓN
from .cita_vacunacion_crud import (
    get_citas_vacunacion,
    get_cita_vacunacion,
    create_cita_vacunacion,
    update_cita_vacunacion,
    delete_cita_vacunacion,
)

__all__ = [
    # USUARIO
    "get_usuarios",
    "get_usuario_by_id",
    "get_usuario_by_email",
    "register_cliente",
    "register_veterinario",
    "login_usuario",
    "create_usuario",
    "update_usuario",
    "delete_usuario",

    # CLIENTE
    "get_clientes",
    "get_cliente",
    "update_cliente",
    "delete_cliente",

    # VETERINARIO
    "get_veterinarios",
    "get_veterinario",
    "update_veterinario",
    "delete_veterinario",

    # SEDE
    "get_sedes",
    "get_sede",
    "create_sede",
    "update_sede",
    "delete_sede",

    # MASCOTA
    "get_mascotas",
    "get_mascota",
    "create_mascota",
    "update_mascota",
    "delete_mascota",

    # VACUNA
    "get_vacunas",
    "get_vacuna",
    "create_vacuna",
    "update_vacuna",
    "delete_vacuna",

    # CITA VACUNACIÓN
    "get_citas_vacunacion",
    "get_cita_vacunacion",
    "create_cita_vacunacion",
    "update_cita_vacunacion",
    "delete_cita_vacunacion",
]

