"""add note table

Revision ID: 4f5d1a393114
Revises: e9406ed920f3
Create Date: 2023-10-19 10:26:53.946755

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4f5d1a393114'
down_revision: Union[str, None] = 'e9406ed920f3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
