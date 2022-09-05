from typing import List
import strawberry
from strawberry import field as Field
from strawberry.file_uploads import Upload
from datetime import date
from models.base import Certificate
from models.journal.merge import JournalGeneralWorkMerge



@strawberry.experimental.pydantic.type(model=Certificate, fields=["id", "number"], description="Сведения о выданном разрешении на строительство")
class BuildingPermitType:
    files: List[Upload] = Field(description="Скан")
    date_extradition: date = Field(description="Дата выдачи разрешения")
    government: str = Field(description="Наименование органа исполнительной власти или органа местного самоуправления")


# @strawberry.type(description="РАЗДЕЛ 1. Список инженерно-технического персонала лица, осуществляющего строительство, занятого при строительстве, реконструкции, капитальном ремонте объекта капитального строительства")
# class ListEngineeringAndTechnicalPersonnelOverhaulType:
#     id: int
#     company_builder: str = Field(description="Наименование лица, осуществляющего строительство")
#     person_engineering: str = Field(description="Фамилия, инициалы, должность лица, входящего в список инженерно-технического персонала")
#     date_begin: date = Field(description="Дата начала работ на объекте капитального строительства с указанием вида работ")
#     date_end: date = Field(description="Дата окончания работ на объекте капитального строительства")
#     person_builder: str = Field(description="Должность, фамилия, инициалы, подпись уполномоченного представителя лица, осуществляющего строительство")
#
#
# @strawberry.type(description="РАЗДЕЛ 2. Перечень специальных журналов, в которых ведется учет выполнения работ, а также журналов авторского надзора лица, осуществляющего подготовку проектной документации")
# class ListSpecialJournalsFulfillmentWorkType:
#     id: int
#     special_journal_name: str = Field(description="Наименование специального журнала (журнала авторского надзора) и дата его выдачи")
#     person_journal: str = Field(description="Наименование лица, осуществляющего строительство (лица, осуществляющего подготовку проектной документации), ведущих журнал, их уполномоченных представителей с указанием должности, фамилии, инициалов")
#     transfer_date_journal: date = Field(description="Дата передачи застройщику или заказчику журнала")
#     signature: str = Field(description="Подпись уполномоченного представителя застройщика или заказчика")
#
#
# @strawberry.type(description="РАЗДЕЛ 3. Сведения о выполнении работ в процессе строительства, реконструкции, капитального ремонта объекта капитального строительства")
# class IntelligenceFulfillmentWorkInProcessConstructionType:
#     id: int
#     date_end: date = Field(description="Дата выполнения работ")
#     job_name: str = Field(description="Наименование работ, выполняемых в процессе строительства, реконструкции, капитального ремонта объекта капитального строительства")
#     position_signature: str = Field(description="Должность, фамилия, инициалы, подпись уполномоченного представителя лица, осуществляющего строительство")
#
#
# @strawberry.type(description="РАЗДЕЛ 4. Сведения о строительном контроле застройщика или заказчика в процессе строительства, реконструкции, капитального ремонта объекта капитального строительства")
# class IntelligenceConstructionControlDeveloperOrCustomerType:
#     id: int
#     information_building_control: str = Field(description="Сведения о проведении строительного контроля при строительстве, реконструкции, капитальному ремонту объекта капитального строительства")
#     detect_limitations: str = Field(description="Выявленные недостатки")
#     detect_limitations_date_plan: date = Field(description="Срок устранения выявленных недостатков")
#     detect_limitations_date_fact: date = Field(description="Дата устранения недостатков")
#     position_signature: str = Field(description="Должность, фамилия, инициалы, подпись уполномоченного представителя застройщика или заказчика")
#
#
# @strawberry.type(description="РАЗДЕЛ 5. Сведения о строительном контроле лица, осуществляющего строительство, в процессе строительстве реконструкции, капитального ремонта объекта капитального строительства")
# class IntelligenceConstructionControlPersonControlBuildingType(IntelligenceConstructionControlDeveloperOrCustomerType):
#     information_building_control: str = Field(description="Сведения о проведении строительного контроля в процессе выполнения работ по строительству, реконструкции, капитальному ремонту объекта капитального строительства")
#
#
# @strawberry.type(description="РАЗДЕЛ 6. Перечень исполнительной документации при строительстве, реконструкции, капитальном ремонте объекта капитального строительства")
# class ListExecutiveDocumentationDuringConstructionType:
#     id: int
#     name_domen.comdocumentation: str = Field(description="Наименование исполнительной документации (с указанием вида работ, места расположения конструкций, участков сетей инженерно - технического обеспечения и т.д.)")
#     data_signature_act: date = Field(description="Дата подписания акта, должности, фамилии, инициалы лиц, подписавших акты")
#
#
# @strawberry.type(description="РАЗДЕЛ 7. Сведения о государственном строительном надзоре при строительстве, реконструкции, капитальном ремонте объекта капитального строительства")
# class IntelligenceStateConstructionSupervisionDuringConstructionType:
#     id: int
#     building_supervision_inspections: str = Field(description="Данные о проведенных органом государственного строительного надзора проверках, включая итоговую проверку")
#     detect_violations_date_plan: str = Field(description="Срок устранения выявленных нарушений")
#     detect_violations_date_fact: date = Field(description="Фактическая дата устранения выявленных нарушений")
#     position_signature: str = Field(description="Должность, фамилия, инициалы, подпись должностного лица")


# @strawberry.type(description="Разделы")
# class JournalGeneralWorkSectionType:
#     list_engineering_and_technical_personnel_overhaul: List[ListEngineeringAndTechnicalPersonnelOverhaulType] = Field(
#         description="РАЗДЕЛ 1. Список инженерно-технического персонала лица, осуществляющего строительство, занятого при строительстве, реконструкции, капитальном ремонте объекта капитального строительства")
#     list_special_journals_fulfillment_work: List[ListSpecialJournalsFulfillmentWorkType] = Field(
#         description="РАЗДЕЛ 2. Перечень специальных журналов, в которых ведется учет выполнения работ, а также журналов авторского надзора лица, осуществляющего подготовку проектной документации")
#     intelligence_fulfillment_work_in_process_construction: List[IntelligenceFulfillmentWorkInProcessConstructionType] = Field(
#         description="РАЗДЕЛ 3. Сведения о выполнении работ в процессе строительства, реконструкции, капитального ремонта объекта капитального строительства")
#     intelligence_construction_control_developer_or_customer: List[IntelligenceConstructionControlDeveloperOrCustomerType] = Field(
#         description="РАЗДЕЛ 4. Сведения о строительном контроле застройщика или заказчика в процессе строительства, реконструкции, капитального ремонта объекта капитального строительства")
#     intelligence_construction_control_person_control_building: List[IntelligenceConstructionControlPersonControlBuildingType] = Field(
#         description="РАЗДЕЛ 5. Сведения о строительном контроле лица, осуществляющего строительство, в процессе строительстве реконструкции, капитального ремонта объекта капитального строительства")
#     list_domen.comdocumentation_during_construction: List[ListExecutiveDocumentationDuringConstructionType] = Field(
#         description="РАЗДЕЛ 6. Перечень исполнительной документации при строительстве, реконструкции, капитальном ремонте объекта капитального строительства")
#     intelligence_state_construction_supervision_during_construction: List[IntelligenceStateConstructionSupervisionDuringConstructionType] = Field(
#         description="РАЗДЕЛ 7. Сведения о государственном строительном надзоре при строительстве, реконструкции, капитальном ремонте объекта капитального строительства")
#
#     # Подпись
#     signature_chapter: SignatureType = Field(description="Подпись")


# @strawberry.type(description="Приложение 02. Общий журнал работ")
@strawberry.experimental.pydantic.type(model=JournalGeneralWorkMerge, all_fields=True, description="Общий журнал работ")
class JournalGeneralWorkType:
    pass
    # short_name_project: str = Field(description="Краткое название проекта")
    #
    # developer: CompanyType = Field(description="Застройщик")
    #
    # customer: CompanyType = Field(description="Заказчик")
    #
    # building_permit: BuildingPermitType = Field(description="Сведения о выданном разрешении на строительство")
    #
    # planner: List[CompanyType] = Field(description="Лицо, осуществляющее подготовку проектной документации")
    #
    # expertise: CertificateType = Field(description="Сведения о государственной экспертизе проектной документации в случаях, предусмотренных статьей 49 Градостроительного кодекса Российской Федерации")
    #
    # developer_person: List[CompanyWithoutRepresentativeType] = Field(description="Лицо, осуществляющее строительство")
    #
    # representative_builder_id: List[CompanyType] = Field(description="Уполномоченный представитель лица, осуществляющего строительство")
    # representative_builder_or_customer_control_id: List[CompanyType] = Field(description="Уполномоченный представитель застройщика или заказчика по вопросам строительного контроля")
    # representative_builder_control_id: List[CompanyType] = Field(description="Уполномоченный представитель лица, осуществляющего строительство, по вопросам строительного контроля")
    # representative_other_id: List[CompanyType] = Field(description="Другие лица, осуществляющие строительство, их уполномоченные представители")
    #
    # building_supervision: CompanyGovType = Field(description="Сведения о государственном строительном надзоре")
    #
    # # Общие сведения об объекте капитального строительства
    # capital_construction_name: str = Field(description="наименование объекта капитального строительства")
    # capital_construction_short_characteristics: str = Field(description="Краткие проектные характеристики объекта капитального строительства")
    # capital_construction_date_begin: str = Field(description="Дата начала строительства, реконструкции, капитального ремонта объекта капитального строительства")
    # capital_construction_date_end: str = Field(description="Дата конца строительства, реконструкции, капитального ремонта объекта капитального строительства")
    #
    # # section: JournalGeneralWorkSectionType = Field(description="Разделы")


@strawberry.input
class JournalGeneralWorkInput(JournalGeneralWorkType):
    pass
