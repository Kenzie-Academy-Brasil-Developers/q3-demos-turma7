"""table invoice created

Revision ID: 08724f12e88f
Revises: a47a93847664
Create Date: 2022-02-15 09:22:42.403489

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08724f12e88f'
down_revision = 'a47a93847664'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('invoices',
    sa.Column('invoice_id', sa.Integer(), nullable=False),
    sa.Column('invoice_number', sa.String(length=63), nullable=True),
    sa.Column('release_time', sa.DateTime(), nullable=True),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ),
    sa.PrimaryKeyConstraint('invoice_id'),
    sa.UniqueConstraint('invoice_number'),
    sa.UniqueConstraint('order_id')
    )
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
    op.drop_table('invoices')
    # ### end Alembic commands ###
