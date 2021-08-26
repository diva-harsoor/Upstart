"""categories table update

Revision ID: 4f2ebf8ad1c2
Revises: e491e38007fc
Create Date: 2021-08-25 21:50:10.647371

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f2ebf8ad1c2'
down_revision = 'e491e38007fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=70), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_category_name'), 'category', ['name'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('org_name', sa.String(length=70), nullable=True),
    sa.Column('org_purpose', sa.String(length=500), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('is_start_up', sa.Boolean(), nullable=True),
    sa.Column('location', sa.String(length=70), nullable=True),
    sa.Column('claimed', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_is_start_up'), 'user', ['is_start_up'], unique=False)
    op.create_index(op.f('ix_user_location'), 'user', ['location'], unique=False)
    op.create_index(op.f('ix_user_org_name'), 'user', ['org_name'], unique=True)
    op.create_table('categories',
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('category_id', 'user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('categories')
    op.drop_index(op.f('ix_user_org_name'), table_name='user')
    op.drop_index(op.f('ix_user_location'), table_name='user')
    op.drop_index(op.f('ix_user_is_start_up'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_category_name'), table_name='category')
    op.drop_table('category')
    # ### end Alembic commands ###