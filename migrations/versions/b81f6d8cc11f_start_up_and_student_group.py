"""start up and student group

Revision ID: b81f6d8cc11f
Revises: 
Create Date: 2021-08-14 13:28:17.058369

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b81f6d8cc11f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('start_up',
    sa.Column('org_name', sa.String(length=70), nullable=True),
    sa.Column('org_purpose', sa.String(length=500), nullable=True),
    sa.Column('category', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('claimed', sa.Boolean(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_start_up_category'), 'start_up', ['category'], unique=False)
    op.create_index(op.f('ix_start_up_city'), 'start_up', ['city'], unique=False)
    op.create_index(op.f('ix_start_up_email'), 'start_up', ['email'], unique=True)
    op.create_index(op.f('ix_start_up_org_name'), 'start_up', ['org_name'], unique=True)
    op.create_table('student_group',
    sa.Column('org_name', sa.String(length=70), nullable=True),
    sa.Column('org_purpose', sa.String(length=500), nullable=True),
    sa.Column('category', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('claimed', sa.Boolean(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('school', sa.String(length=70), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_student_group_category'), 'student_group', ['category'], unique=False)
    op.create_index(op.f('ix_student_group_email'), 'student_group', ['email'], unique=True)
    op.create_index(op.f('ix_student_group_org_name'), 'student_group', ['org_name'], unique=True)
    op.create_index(op.f('ix_student_group_school'), 'student_group', ['school'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_student_group_school'), table_name='student_group')
    op.drop_index(op.f('ix_student_group_org_name'), table_name='student_group')
    op.drop_index(op.f('ix_student_group_email'), table_name='student_group')
    op.drop_index(op.f('ix_student_group_category'), table_name='student_group')
    op.drop_table('student_group')
    op.drop_index(op.f('ix_start_up_org_name'), table_name='start_up')
    op.drop_index(op.f('ix_start_up_email'), table_name='start_up')
    op.drop_index(op.f('ix_start_up_city'), table_name='start_up')
    op.drop_index(op.f('ix_start_up_category'), table_name='start_up')
    op.drop_table('start_up')
    # ### end Alembic commands ###
