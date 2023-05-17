"""empty message

Revision ID: da2ab7a9d377
Revises: 60de663073b0
Create Date: 2023-05-17 14:46:02.057285

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da2ab7a9d377'
down_revision = '60de663073b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('chat', schema=None) as batch_op:
        batch_op.alter_column('fecha',
               existing_type=sa.DATE(),
               nullable=False)

    with op.batch_alter_table('mensaje', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id_chat', sa.String(length=36), nullable=True))
        batch_op.add_column(sa.Column('id_mensajePadre', sa.String(length=36), nullable=True))
        batch_op.drop_constraint('mensaje_id_mensaje2_fkey', type_='foreignkey')
        batch_op.drop_constraint('mensaje_id_usuariodestinatario_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'chat', ['id_chat'], ['id_chat'])
        batch_op.create_foreign_key(None, 'mensaje', ['id_mensajePadre'], ['id_mensaje'])
        batch_op.drop_column('id_mensaje2')
        batch_op.drop_column('id_usuariodestinatario')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mensaje', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id_usuariodestinatario', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('id_mensaje2', sa.VARCHAR(length=36), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('mensaje_id_usuariodestinatario_fkey', 'usuario', ['id_usuariodestinatario'], ['id_usuario'])
        batch_op.create_foreign_key('mensaje_id_mensaje2_fkey', 'mensaje', ['id_mensaje2'], ['id_mensaje'])
        batch_op.drop_column('id_mensajePadre')
        batch_op.drop_column('id_chat')

    with op.batch_alter_table('chat', schema=None) as batch_op:
        batch_op.alter_column('fecha',
               existing_type=sa.DATE(),
               nullable=True)

    # ### end Alembic commands ###
