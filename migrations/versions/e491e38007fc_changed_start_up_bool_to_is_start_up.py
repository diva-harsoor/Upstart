"""changed start_up bool to is_start_up

Revision ID: e491e38007fc
Revises: 472711fce0ac
Create Date: 2021-08-14 14:19:27.515964

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e491e38007fc'
down_revision = '472711fce0ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_start_up', sa.Boolean(), nullable=True))
    op.drop_index('ix_user_start_up', table_name='user')
    op.create_index(op.f('ix_user_is_start_up'), 'user', ['is_start_up'], unique=False)
    op.drop_column('user', 'start_up')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('start_up', sa.BOOLEAN(), nullable=True))
    op.drop_index(op.f('ix_user_is_start_up'), table_name='user')
    op.create_index('ix_user_start_up', 'user', ['start_up'], unique=False)
    op.drop_column('user', 'is_start_up')
    # ### end Alembic commands ###