"""empty message

Revision ID: 5a7fc6df6e7c
Revises: 2a0b27b11fd1
Create Date: 2019-09-14 17:54:52.339653

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a7fc6df6e7c'
down_revision = '2a0b27b11fd1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'type', ['type'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'type', type_='unique')
    # ### end Alembic commands ###
