"""foreingkey

Revision ID: 8287c1d67267
Revises: 0fb6f5f252a2
Create Date: 2022-08-30 11:51:28.895123

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8287c1d67267'
down_revision = '0fb6f5f252a2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'posts', 'users', ['owner_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.drop_column('posts', 'owner_id')
    # ### end Alembic commands ###
