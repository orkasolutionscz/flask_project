"""Add newsletter modify db

Revision ID: f09cf814ab15
Revises: 43e620430aa1
Create Date: 2021-04-27 00:02:00.397736

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'f09cf814ab15'
down_revision = '43e620430aa1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "newsletter",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("email", sa.String, unique=True))


def downgrade():
    op.drop_table("newsletter")
