from dotenv import load_dotenv
import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# 🔥 Cargar variables de entorno
load_dotenv()

config = context.config

# 🔥 Sobrescribir DATABASE_URL
database_url = os.getenv("DATABASE_URL")
if database_url:
    config.set_main_option("sqlalchemy.url", database_url)

# 🔥 Logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 🔥 Importar Base y ENTIDADES
from database import Base
from entities import *  # 👈 MUCHO MEJOR que importar uno por uno

target_metadata = Base.metadata


# =========================
# OFFLINE
# =========================
def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,  # 🔥 detecta cambios de tipos
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


# =========================
# ONLINE
# =========================
def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,  # 🔥 IMPORTANTE
        )

        with context.begin_transaction():
            context.run_migrations()


# =========================
# EJECUCIÓN
# =========================
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
