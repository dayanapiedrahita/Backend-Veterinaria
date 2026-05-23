"""Agregar tabla servicio y columna servicio_id en cita_vacunacion

Revision ID: a1b2c3d4e5f6
Revises: 0bf9179c1928
Create Date: 2026-05-23 00:00:00.000000

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "a1b2c3d4e5f6"
down_revision: Union[str, None] = "0bf9179c1928"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "servicio",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("nombre", sa.String(), nullable=False),
        sa.Column("precio", sa.Float(), nullable=False),
        sa.Column("descripcion", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_servicio_id"), "servicio", ["id"], unique=False)
    op.add_column(
        "cita_vacunacion",
        sa.Column("servicio_id", sa.Integer(), nullable=True),
    )
    op.create_foreign_key(
        "fk_cita_vacunacion_servicio_id",
        "cita_vacunacion",
        "servicio",
        ["servicio_id"],
        ["id"],
    )


def downgrade() -> None:
    op.drop_constraint("fk_cita_vacunacion_servicio_id", "cita_vacunacion", type_="foreignkey")
    op.drop_column("cita_vacunacion", "servicio_id")
    op.drop_index(op.f("ix_servicio_id"), table_name="servicio")
    op.drop_table("servicio")
