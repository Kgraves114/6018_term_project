"""empty message

Revision ID: 04182783932c
Revises: a4bf599ab08b
Create Date: 2017-12-18 22:27:33.111066

"""

# revision identifiers, used by Alembic.
revision = '04182783932c'
down_revision = 'a4bf599ab08b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('study',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('studyname', sa.String(length=64), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('confirmed', sa.Boolean(), nullable=True),
    sa.Column('investigator', sa.String(length=64), nullable=True),
    sa.Column('location', sa.String(length=64), nullable=True),
    sa.Column('background', sa.Text(), nullable=True),
    sa.Column('study_procedure', sa.Text(), nullable=True),
    sa.Column('risksbenefits', sa.Text(), nullable=True),
    sa.Column('PHI', sa.Text(), nullable=True),
    sa.Column('member_since', sa.DateTime(), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.Column('avatar_hash', sa.String(length=32), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_study_email'), 'study', ['email'], unique=True)
    op.create_index(op.f('ix_study_studyname'), 'study', ['studyname'], unique=True)
    op.drop_table('users')
    op.drop_table('consents')
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.create_foreign_key(None, 'posts', 'study', ['author_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.create_foreign_key(None, 'posts', 'users', ['author_id'], ['id'])
    op.create_table('consents',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('institution', sa.VARCHAR(length=64), nullable=True),
    sa.Column('study_name', sa.VARCHAR(length=255), nullable=True),
    sa.Column('study_objective', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=64), nullable=True),
    sa.Column('role_id', sa.INTEGER(), nullable=True),
    sa.Column('email', sa.VARCHAR(length=64), nullable=True),
    sa.Column('password_hash', sa.VARCHAR(length=128), nullable=True),
    sa.Column('confirmed', sa.BOOLEAN(), nullable=True),
    sa.Column('about_me', sa.TEXT(), nullable=True),
    sa.Column('last_seen', sa.DATETIME(), nullable=True),
    sa.Column('location', sa.VARCHAR(length=64), nullable=True),
    sa.Column('member_since', sa.DATETIME(), nullable=True),
    sa.Column('name', sa.VARCHAR(length=64), nullable=True),
    sa.Column('avatar_hash', sa.VARCHAR(length=32), nullable=True),
    sa.Column('institution', sa.VARCHAR(length=64), nullable=True),
    sa.Column('study_name', sa.VARCHAR(length=255), nullable=True),
    sa.Column('study_objective', sa.TEXT(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index(op.f('ix_study_studyname'), table_name='study')
    op.drop_index(op.f('ix_study_email'), table_name='study')
    op.drop_table('study')
    # ### end Alembic commands ###
