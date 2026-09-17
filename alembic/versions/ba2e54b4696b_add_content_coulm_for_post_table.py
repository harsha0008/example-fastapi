"""Add content coulm for post table

Revision ID: ba2e54b4696b
Revises: ce8ee4aa1c35
Create Date: 2026-09-17 19:54:33.035362

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ba2e54b4696b'
down_revision: Union[str, Sequence[str], None] = 'ce8ee4aa1c35'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
