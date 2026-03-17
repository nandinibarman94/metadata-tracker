"""insert default source system

Revision ID: 40f463d0dd64
Revises: efb5de449e26
Create Date: 2026-03-17 20:10:07.770628

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '40f463d0dd64'
down_revision: Union[str, Sequence[str], None] = 'efb5de449e26'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
     op.execute(
        sa.text("""
            INSERT INTO sourcesystems 
            (id, name, "owningApplication", "createdOn", "createdBy", "updatedOn", "updatedBy")
            VALUES 
            (1, 'OrderDB', 'data-team', CURRENT_TIMESTAMP, 'admin', CURRENT_TIMESTAMP, 'admin')
        """)
    )


def downgrade() -> None:
    op.execute(
        sa.text("""
            DELETE FROM sourcesystems 
            WHERE id = 1
        """)
    )
