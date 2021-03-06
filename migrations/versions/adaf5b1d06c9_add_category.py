"""add category

Revision ID: adaf5b1d06c9
Revises: ad55963cba61
Create Date: 2018-01-21 18:15:11.302916

"""

# revision identifiers, used by Alembic.
revision = 'adaf5b1d06c9'
down_revision = 'ad55963cba61'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('poem', sa.Column('category', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('poem', 'category')
    # ### end Alembic commands ###
