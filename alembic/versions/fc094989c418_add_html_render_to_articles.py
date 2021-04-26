"""add html_render to articles

Revision ID: fc094989c418
Revises: 97d536af2327
Create Date: 2021-04-26 23:16:44.690222

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc094989c418'
down_revision = '97d536af2327'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("article",
                  sa.Column("html_render", sa.String, server_default=""))


def downgrade():
    op.drop_column("article", "html_render")
