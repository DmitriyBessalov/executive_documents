from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship
from datetime import date


# Журнал верификации закупленной продукции
class JournalVerificationPurchasedProducts(SQLModel, table=False):
    id: Optional[int] = Field(primary_key=True)
    name_production: str = Field(description="Наименование продукции")
    delivery_date: date = Field(description="Дата поставки")
    transport_number: str = Field(description="Номер вагона (авто-машины)")
    provider__company_id: str = Field(description="Поставщик")
    certificate_id: int = Field(description="Сертификат качества (паспорт, сертификат и т.д)")
    type_packaging: str = Field(description="Вид упаковки")
    manufacture_date: date = Field(description="Дата изготовления")
    sampling_location: str = Field(description="Место отбора образца (выборки или пробы)")
    sampling_date: date = Field(description="Дата отбора образца (выборки или пробы)")
    quality_opinion_person: str = Field(description="Заключение лица о качестве")
    signature_id: int = Field(description="Подпись лица ответственного за верификацию")


# Журнал входного учета и контроля качества получаемых деталей, материалов, конструкций и деталей
class JournalInputAccountingAndQualityControlReceivedParts(SQLModel, table=False):
    id: Optional[int] = Field(primary_key=True)
    name_production: str = Field(description="Наименование продукции")
    delivery_date: date = Field(description="Дата доставки")
    quantity: str = Field(description="Количество")
    provider__company_id: str = Field(description="Поставщик")
    certificate_id: int = Field(description="Наименование и номер сопроводительного документа (сертификаты, декларации, паспорта качества))")
    control_type: str = Field(description="Вид контроля (визуальный, инструментальный, лабораторный)")
    control_result: str = Field(description="Результат контроля")
    signature_id: int = Field(description="Подпись лица осуществляющего контроль")


class JournalMaterialAll(JournalVerificationPurchasedProducts, JournalInputAccountingAndQualityControlReceivedParts, table=True):
    __tablename__ = "journal_material_all"

    certificate: List["Certificate"] = Relationship(back_populates="journal_material")
