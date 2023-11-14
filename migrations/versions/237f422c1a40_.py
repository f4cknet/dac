"""empty message

Revision ID: 237f422c1a40
Revises: a32a482a6686
Create Date: 2023-11-10 14:03:22.679361

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '237f422c1a40'
down_revision = 'a32a482a6686'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('result', schema=None) as batch_op:
        batch_op.add_column(sa.Column('result_detail', sa.String(length=256), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('result', schema=None) as batch_op:
        batch_op.drop_column('result_detail')

    # ### end Alembic commands ###
