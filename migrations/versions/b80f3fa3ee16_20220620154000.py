"""20220620154000

Revision ID: b80f3fa3ee16
Revises: 7f901cab2cc4
Create Date: 2022-06-20 15:41:03.546868

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b80f3fa3ee16'
down_revision = '7f901cab2cc4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('job_bolted_mounting_connections',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('journal_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True, comment='Дата'),
    sa.Column('drawing_number_KMD', sa.String(), nullable=True, comment='Номер чертежа КМД и наименование узла (стыка) в соединении, ряд, ось, отметка'),
    sa.Column('numeric_upplied_bolts_in_connection', sa.Integer(), nullable=True, comment='Число поставленных болтов в соединении, шт.'),
    sa.Column('bolt_certificate_number', sa.String(), nullable=True, comment='Номер сертификата на болты'),
    sa.Column('method_processing_contact_surfaces', sa.String(), nullable=True, comment='Способ обработки контактных поверхностей'),
    sa.Column('estimated_torque', sa.String(), nullable=True, comment='Расчетный момент закручивания, кгсּм, угол поворота, град.'),
    sa.Column('quality_processing_of_contact_surfaces', sa.String(), nullable=True, comment='Качество обработки контактных поверхностей'),
    sa.Column('numeric_of_tested_bolts', sa.Integer(), nullable=True, comment='Число проверенных болтов, шт.'),
    sa.Column('torque_test_results', sa.String(), nullable=True, comment='Результаты проверки момента закручивания, кгсּм, угла поворота, град.'),
    sa.Column('stigma_foreman', sa.String(), nullable=True, comment='Номер клейма бригадира'),
    sa.Column('foreman__signature_id', sa.String(), nullable=True, comment='Подпись бригадира'),
    sa.Column('staging_bolts__signature_id', sa.String(), nullable=True, comment='Подпись лица, ответственного за постановку болтов'),
    sa.Column('customer__signature_id', sa.String(), nullable=True, comment='Подпись представителя заказчика'),
    sa.ForeignKeyConstraint(['journal_id'], ['journal_base.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('personal_on_mount_bolt',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('journal_id', sa.Integer(), nullable=True),
    sa.Column('responsible_id', sa.Integer(), nullable=True, comment='Фамилия, имя, отчество'),
    sa.Column('assigned_category', sa.Integer(), nullable=True, comment='Присвоенный разряд'),
    sa.Column('stigma', sa.String(), nullable=True, comment='Присвоенный номер или знак (клеймо)'),
    sa.Column('qualification_certificate__documentation_id', sa.Integer(), nullable=True, comment='Квалификационное удостоверение'),
    sa.Column('note', sa.String(), nullable=True, comment='Примечание'),
    sa.ForeignKeyConstraint(['journal_id'], ['journal_base.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('personal_on_mount_bolt')
    op.drop_table('job_bolted_mounting_connections')
    # ### end Alembic commands ###