"""server_default todas las tablas

Revision ID: 1212d5fa5914
Revises: 51277d4c3a4f
Create Date: 2026-03-05 04:27:41.265394

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1212d5fa5914"
down_revision: Union[str, Sequence[str], None] = "51277d4c3a4f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "categoria",
        "created_at",
        existing_type=sa.DateTime(),
        server_default=sa.func.now(),
    )
    op.alter_column(
        "categoria",
        "updated_at",
        existing_type=sa.DateTime(),
        server_default=sa.func.now(),
    )
    op.alter_column(
        "operador",
        "created_at",
        existing_type=sa.DateTime(),
        server_default=sa.func.now(),
    )
    op.alter_column(
        "operador",
        "updated_at",
        existing_type=sa.DateTime(),
        server_default=sa.func.now(),
    )
    op.alter_column(
        "proveedores",
        "created_at",
        existing_type=sa.DateTime(),
        server_default=sa.func.now(),
    )
    op.alter_column(
        "proveedores",
        "updated_at",
        existing_type=sa.DateTime(),
        server_default=sa.func.now(),
    )
    op.alter_column(
        "movimientos",
        "fecha",
        existing_type=sa.DateTime(),
        server_default=sa.func.now(),
    )


def downgrade() -> None:
    """Downgrade schema."""
    pass
