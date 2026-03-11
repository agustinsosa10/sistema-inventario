"""remove updated_at server_default

Revision ID: 08b040e13830
Revises: a3d0e612da58
Create Date: 2026-03-11 14:46:49.503506

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "08b040e13830"
down_revision: Union[str, Sequence[str], None] = "a3d0e612da58"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column("proveedores", "updated_at", server_default=None)


def downgrade() -> None:
    op.alter_column("proveedores", "updated_at", server_default=func.now())
