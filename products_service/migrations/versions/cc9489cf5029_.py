"""empty message

Revision ID: cc9489cf5029
Revises: ef44c4300345
Create Date: 2019-09-16 15:53:31.499079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc9489cf5029'
down_revision = 'ef44c4300345'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('type', sa.Column('photo', sa.LargeBinary(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('type', 'photo')
    # ### end Alembic commands ###
