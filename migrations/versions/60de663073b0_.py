"""empty message

Revision ID: 60de663073b0
Revises: d4dc20757dd4
Create Date: 2023-05-16 23:47:15.489294

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60de663073b0'
down_revision = 'd4dc20757dd4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chat',
    sa.Column('id_chat', sa.String(length=36), nullable=False),
    sa.Column('id_usuario', sa.String(length=160), nullable=True),
    sa.Column('id_usuario2', sa.String(length=160), nullable=True),
    sa.Column('id_mensaje', sa.String(length=160), nullable=True),
    sa.Column('fecha', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['id_mensaje'], ['mensaje.id_mensaje'], ),
    sa.ForeignKeyConstraint(['id_usuario'], ['usuario.id_usuario'], ),
    sa.ForeignKeyConstraint(['id_usuario2'], ['usuario.id_usuario'], ),
    sa.PrimaryKeyConstraint('id_chat')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('chat')
    # ### end Alembic commands ###
