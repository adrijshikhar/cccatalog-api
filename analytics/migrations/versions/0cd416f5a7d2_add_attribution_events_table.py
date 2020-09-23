"""Add attribution events table

Revision ID: 0cd416f5a7d2
Revises: 7695412f8a64
Create Date: 2020-09-11 15:43:24.507088

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0cd416f5a7d2'
down_revision = '7695412f8a64'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('attribution_referrer_event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('image_uuid', postgresql.UUID(), nullable=True),
    sa.Column('full_referer', sa.String(), nullable=True),
    sa.Column('referer_domain', sa.String(), nullable=True),
    sa.Column('resource', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_attribution_referrer_event_image_uuid'), 'attribution_referrer_event', ['image_uuid'], unique=False)
    op.create_index(op.f('ix_attribution_referrer_event_referer_domain'), 'attribution_referrer_event', ['referer_domain'], unique=False)
    op.create_index(op.f('ix_attribution_referrer_event_resource'), 'attribution_referrer_event', ['resource'], unique=False)
    op.create_index(op.f('ix_attribution_referrer_event_timestamp'), 'attribution_referrer_event', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_attribution_referrer_event_timestamp'), table_name='attribution_referrer_event')
    op.drop_index(op.f('ix_attribution_referrer_event_resource'), table_name='attribution_referrer_event')
    op.drop_index(op.f('ix_attribution_referrer_event_referer_domain'), table_name='attribution_referrer_event')
    op.drop_index(op.f('ix_attribution_referrer_event_image_uuid'), table_name='attribution_referrer_event')
    op.drop_table('attribution_referrer_event')
    # ### end Alembic commands ###