"""migration_3

Revision ID: 2d9d9ae1feb9
Revises: 8c1b8e9da1e2
Create Date: 2023-08-14 19:48:55.582058

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2d9d9ae1feb9'
down_revision: Union[str, None] = '8c1b8e9da1e2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('temperature',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city_id', sa.Integer(), nullable=True),
    sa.Column('date_time', sa.DateTime(), nullable=False),
    sa.Column('temperature', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['city_id'], ['city.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_temperature_id'), 'temperature', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_temperature_id'), table_name='temperature')
    op.drop_table('temperature')
    # ### end Alembic commands ###