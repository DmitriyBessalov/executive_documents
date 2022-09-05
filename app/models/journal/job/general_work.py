from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship
from datetime import date


# # РАЗДЕЛ 1. Список инженерно-технического персонала лица, осуществляющего строительство, занятого при строительстве, реконструкции, капитальном ремонте объекта капитального строительства
# class ListEngineeringAndTechnicalPersonnelOverhaul:
#     id: int
#     company_builder: str = Field(description="Наименование лица, осуществляющего строительство")
#     person_engineering: str = Field(description="Фамилия, инициалы, должность лица, входящего в список инженерно-технического персонала")
#     date_begin: date = Field(description="Дата начала работ на объекте капитального строительства с указанием вида работ")
#     date_end: date = Field(description="Дата окончания работ на объекте капитального строительства")
#     person_builder: str = Field(description="Должность, фамилия, инициалы, подпись уполномоченного представителя лица, осуществляющего строительство")
#
#
# # РАЗДЕЛ 2. Перечень специальных журналов, в которых ведется учет выполнения работ, а также журналов авторского надзора лица, осуществляющего подготовку проектной документации
# class ListSpecialJournalsFulfillmentWork:
#     id: int
#     special_journal_name: str = Field(description="Наименование специального журнала (журнала авторского надзора) и дата его выдачи")
#     person_journal: str = Field(description="Наименование лица, осуществляющего строительство (лица, осуществляющего подготовку проектной документации), ведущих журнал, их уполномоченных представителей с указанием должности, фамилии, инициалов")
#     transfer_date_journal: date = Field(description="Дата передачи застройщику или заказчику журнала")
#     signature: str = Field(description="Подпись уполномоченного представителя застройщика или заказчика")
#
#
# # РАЗДЕЛ 3. Сведения о выполнении работ в процессе строительства, реконструкции, капитального ремонта объекта капитального строительства
# class IntelligenceFulfillmentWorkInProcessConstruction:
#     id: int
#     date_end: date = Field(description="Дата выполнения работ")
#     job_name: str = Field(description="Наименование работ, выполняемых в процессе строительства, реконструкции, капитального ремонта объекта капитального строительства")
#     position_signature: str = Field(description="Должность, фамилия, инициалы, подпись уполномоченного представителя лица, осуществляющего строительство")
#
#
# # РАЗДЕЛ 4. Сведения о строительном контроле застройщика или заказчика в процессе строительства, реконструкции, капитального ремонта объекта капитального строительства
# class IntelligenceConstructionControlDeveloperOrCustomer:
#     id: int
#     information_building_control: str = Field(description="Сведения о проведении строительного контроля при строительстве, реконструкции, капитальному ремонту объекта капитального строительства")
#     detect_limitations: str = Field(description="Выявленные недостатки")
#     detect_limitations_date_plan: date = Field(description="Срок устранения выявленных недостатков")
#     detect_limitations_date_fact: date = Field(description="Дата устранения недостатков")
#     position_signature: str = Field(description="Должность, фамилия, инициалы, подпись уполномоченного представителя застройщика или заказчика")
#
#
# # РАЗДЕЛ 5. Сведения о строительном контроле лица, осуществляющего строительство, в процессе строительстве реконструкции, капитального ремонта объекта капитального строительства
# class IntelligenceConstructionControlPersonControlBuilding(IntelligenceConstructionControlDeveloperOrCustomer):
#     information_building_control: str = Field(description="Сведения о проведении строительного контроля в процессе выполнения работ по строительству, реконструкции, капитальному ремонту объекта капитального строительства")
#
#
# # РАЗДЕЛ 6. Перечень исполнительной документации при строительстве, реконструкции, капитальном ремонте объекта капитального строительства
# class ListExecutiveDocumentationDuringConstruction:
#     id: int
#     name_domen.comdocumentation: str = Field(description="Наименование исполнительной документации (с указанием вида работ, места расположения конструкций, участков сетей инженерно - технического обеспечения и т.д.)")
#     data_signature_act: date = Field(description="Дата подписания акта, должности, фамилии, инициалы лиц, подписавших акты")
#
#
# # РАЗДЕЛ 7. Сведения о государственном строительном надзоре при строительстве, реконструкции, капитальном ремонте объекта капитального строительства
# class IntelligenceStateConstructionSupervisionDuringConstruction:
#     id: int
#     building_supervision_inspections: str = Field(description="Данные о проведенных органом государственного строительного надзора проверках, включая итоговую проверку")
#     detect_violations_date_plan: str = Field(description="Срок устранения выявленных нарушений")
#     detect_violations_date_fact: date = Field(description="Фактическая дата устранения выявленных нарушений")
#     position_signature: str = Field(description="Должность, фамилия, инициалы, подпись должностного лица")


# Приложение 02. Общий журнал работ
class JournalGeneralWork(SQLModel, table=True):
    __tablename__ = "journal_general_work"

    id: int = Field(primary_key=True, foreign_key="journal.id")
    journal: List["Journal"] = Relationship(back_populates="journal_general_work")

    short_name_project: str = Field(description="Краткое название проекта")

    developer__company_id: int = Field(description="Застройщик")

    customer__company_id: int = Field(description="Заказчик")

    building_permit__company_id: int = Field(description="Сведения о выданном разрешении на строительство")

    planner__company_id: int = Field(description="Лицо, осуществляющее подготовку проектной документации")

    expertise__document_id: int = Field(foreign_key="certificate.id", description="Сведения о государственной экспертизе проектной документации в случаях, предусмотренных статьей 49 Градостроительного кодекса Российской Федерации")
    certificate: List["Certificate"] = Relationship(back_populates="journal_general_work")

    developer_person__company_id: int = Field(description="Лицо, осуществляющее строительство")

    representative_builder__company_id: int = Field(description="Уполномоченный представитель лица, осуществляющего строительство")

    representative_builder_or_customer__company_id: int = Field(description="Уполномоченный представитель застройщика или заказчика по вопросам строительного контроля")

    representative_builder_control__company_id: int = Field(description="Уполномоченный представитель лица, осуществляющего строительство, по вопросам строительного контроля")

    representative_other__company_id: int = Field(description="Другие лица, осуществляющие строительство, их уполномоченные представители")

    building_supervision__company_id: int = Field(description="Сведения о государственном строительном надзоре")

    capital_construction_name: str = Field(description="Наименование объекта капитального строительства")
    capital_construction_short_characteristics: str = Field(description="Краткие проектные характеристики объекта капитального строительства")
    capital_construction_date_begin: date = Field(description="Дата начала строительства, реконструкции, капитального ремонта объекта капитального строительства")
    capital_construction_date_end: date = Field(description="Дата конца строительства, реконструкции, капитального ремонта объекта капитального строительства")

    # list_engineering_and_technical_personnel_overhaul: List[ListEngineeringAndTechnicalPersonnelOverhaulType] = Field(
    #     description="РАЗДЕЛ 1. Список инженерно-технического персонала лица, осуществляющего строительство, занятого при строительстве, реконструкции, капитальном ремонте объекта капитального строительства")

    # list_special_journals_fulfillment_work: List[ListSpecialJournalsFulfillmentWorkType] = Field(
    #     description="РАЗДЕЛ 2. Перечень специальных журналов, в которых ведется учет выполнения работ, а также журналов авторского надзора лица, осуществляющего подготовку проектной документации")

    # intelligence_fulfillment_work_in_process_construction: List[IntelligenceFulfillmentWorkInProcessConstructionType] = Field(
    #     description="РАЗДЕЛ 3. Сведения о выполнении работ в процессе строительства, реконструкции, капитального ремонта объекта капитального строительства")

    # intelligence_construction_control_developer_or_customer: List[IntelligenceConstructionControlDeveloperOrCustomerType] = Field(
    #     description="РАЗДЕЛ 4. Сведения о строительном контроле застройщика или заказчика в процессе строительства, реконструкции, капитального ремонта объекта капитального строительства")

    # intelligence_construction_control_person_control_building: List[IntelligenceConstructionControlPersonControlBuildingType] = Field(
    #     description="РАЗДЕЛ 5. Сведения о строительном контроле лица, осуществляющего строительство, в процессе строительстве реконструкции, капитального ремонта объекта капитального строительства")

    # list_domen.comdocumentation_during_construction: List[ListExecutiveDocumentationDuringConstructionType] = Field(
    #     description="РАЗДЕЛ 6. Перечень исполнительной документации при строительстве, реконструкции, капитальном ремонте объекта капитального строительства")

    # intelligence_state_construction_supervision_during_construction: List[IntelligenceStateConstructionSupervisionDuringConstructionType] = Field(
    #     description="РАЗДЕЛ 7. Сведения о государственном строительном надзоре при строительстве, реконструкции, капитальном ремонте объекта капитального строительства")

    # chapter__signature_id: int = Field(description="Подпись", foreign_key="signature.id")
