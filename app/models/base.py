from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship
from datetime import date
#from models import JournalGeneralWork


# Представитель организации
class Representative(SQLModel, table=False):
    id: Optional[int] = Field(primary_key=True)
    full_name: str = Field(description="ФИО")
    position: str = Field(description="Должность")


# Организация
class Company(SQLModel, table=False):
    id: Optional[int] = Field(primary_key=True)
    name: str = Field(description="Название")
    number: str = Field(description="номер выдачи свидетельства о государственной регистрации")
    date_extradition: date = Field(description="дата выдачи свидетельства о государственной регистрации")
    ogrn: str = Field(description="ОГРН")
    inn: int = Field(description="ИНН")
    address: int = Field(description="Почтовый адрес")
    phone_or_fax: Optional[str] = Field(description="Телефон/факс")
    representative_id: Optional[int] = Field(description="Представитель")


# Свидетельство (сертификат качества)
class Certificate(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    number: str = Field(description="номер")
    date_extradition: date = Field(description="дата заключения")
    government: str = Field(description="наименование органа исполнительной власти, выдавшего заключение")
    files: Optional[str] = Field(description="Скан документа")

    journal_general_work: List["JournalGeneralWork"] = Relationship(back_populates="certificate", sa_relationship_kwargs={"cascade": "all, delete"})


# Доверенность
class PowerAttorney(SQLModel, table=True):
    __tablename__ = "power_attorney"

    id: Optional[int] = Field(primary_key=True)
    number: str = Field(description="Номер документа, подтверждающего полномочия")
    power_attorney: str = Field(description="Наименование документа, подтверждающего полномочия")
    date_extradition: date = Field(description="Дата начала")
    date_end: date = Field(description="Дата конца")
    files: Optional[str] = Field(description="Скан доверенности")

    signature_id: int = Field(description="Подпись", foreign_key="power_attorney.id")
    signature: List["Signature"] = Relationship(back_populates="power_attorney", sa_relationship_kwargs={"cascade": "all, delete"})


# Подпись
class Signature(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    date_signature: date = Field(description="Дата подписи")

    power_attorney_id: Optional[int] = Field(description="Текущая доверенность", foreign_key="power_attorney.id")
    power_attorney: List["PowerAttorney"] = Relationship(back_populates="signature")
    journal: List["Journal"] = Relationship(back_populates="signature")


# Основа Журнала
class Journal(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    number: str = Field(description="Номер журнала")
    type_work: str = Field(description="Вид работ")

    project_name: str = Field(description="Наименование проекта")

    company: str = Field(description="Организация, выполняющая работы")
    date_begin: date = Field(description="Дата начала работ")
    date_end: date = Field(description="Дата конца работ")

    signature_id: Optional[int] = Field(description="Подпись", foreign_key="signature.id", nullable=True)
    signature: List["Signature"] = Relationship(back_populates="journal")

    journal_general_work: List["JournalGeneralWork"] = Relationship(back_populates="journal")
