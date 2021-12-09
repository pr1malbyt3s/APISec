"""empty message

Revision ID: 7d4d098294b3
Revises: e5ed83222d79
Create Date: 2021-12-09 16:04:40.562156

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d4d098294b3'
down_revision = 'e5ed83222d79'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=64), nullable=False),
    sa.Column('salt', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
