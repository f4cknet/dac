"""empty message

Revision ID: ab4c55cf2231
Revises: 237f422c1a40
Create Date: 2023-11-10 16:51:37.306334

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab4c55cf2231'
down_revision = '237f422c1a40'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('result', schema=None) as batch_op:
        batch_op.add_column(sa.Column('old_traceid', sa.String(length=64), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('result', schema=None) as batch_op:
        batch_op.drop_column('old_traceid')

    # ### end Alembic commands ###