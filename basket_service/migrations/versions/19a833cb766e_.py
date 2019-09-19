"""empty message

Revision ID: 19a833cb766e
Revises: f4a6d94877d1
Create Date: 2019-09-15 14:16:38.764563

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19a833cb766e'
down_revision = 'f4a6d94877d1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('date', sa.Date(), nullable=True))
    op.add_column('order', sa.Column('payment', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('order', 'payment')
    op.drop_column('order', 'date')
    # ### end Alembic commands ###