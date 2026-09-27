"""Fix issues with declarative base

Revision ID: 6b724627a71b
Revises: 21cd497f85f0
Create Date: 2023-10-19 10:04:18.129521

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6b724627a71b'
down_revision: Union[str, None] = '21cd497f85f0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
