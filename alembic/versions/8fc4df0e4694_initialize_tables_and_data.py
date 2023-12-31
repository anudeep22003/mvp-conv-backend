"""initialize tables and data

Revision ID: 8fc4df0e4694
Revises: 
Create Date: 2023-06-27 17:28:55.688436

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fc4df0e4694'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('message',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('conv_id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('sender', sa.String(), nullable=False),
    sa.Column('receiver', sa.String(), nullable=False),
    sa.Column('sources', sa.String(), nullable=True),
    sa.Column('ts_created', sa.DateTime(timezone=True), server_default=sa.text("(STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW'))"), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('message')
    # ### end Alembic commands ###
