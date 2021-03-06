"""table order rename to orders

Revision ID: a47a93847664
Revises: 3638f1058177
Create Date: 2022-02-15 09:04:19.083905

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a47a93847664'
down_revision = '3638f1058177'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_date', sa.DateTime(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('order')
    op.alter_column('users', 'account_balance',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=2),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'account_balance',
               existing_type=sa.Float(precision=2),
               type_=sa.REAL(),
               existing_nullable=True)
    op.create_table('order',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('order_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('customer_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['users.user_id'], name='order_customer_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='order_pkey')
    )
    op.drop_table('orders')
    # ### end Alembic commands ###
