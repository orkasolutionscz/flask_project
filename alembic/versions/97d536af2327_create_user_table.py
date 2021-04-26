"""Create User table

Revision ID: 97d536af2327
Revises: 
Create Date: 2021-04-26 06:23:32.419065

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97d536af2327'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "user",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("username", sa.String, unique=True),
        sa.Column("password", sa.String)
    )


def downgrade():
    op.drop_table("user")
