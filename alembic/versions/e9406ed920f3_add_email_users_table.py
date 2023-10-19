"""add email users table

Revision ID: e9406ed920f3
Revises: 6b724627a71b
Create Date: 2023-10-19 10:05:00.632881

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e9406ed920f3'
down_revision: Union[str, None] = '6b724627a71b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
