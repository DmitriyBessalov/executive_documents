from typing import List
import strawberry
from strawberry import field as Field
from models.base import PowerAttorney, Representative, Signature, Certificate, Company


@strawberry.experimental.pydantic.type(model=PowerAttorney, all_fields=True, description="Доверенность")
class PowerAttorneyType:
    pass


@strawberry.input
class PowerAttorneyInput(PowerAttorneyType):
    pass


@strawberry.experimental.pydantic.type(model=Representative, all_fields=True, description="Представитель организации")
class RepresentativeType:
    power_attorney: List[PowerAttorneyType] = Field(description="Доверенности")


@strawberry.experimental.pydantic.type(model=Signature, all_fields=True, description="Подпись")
class SignatureType:
    # power_attorney: PowerAttorneyType = Field(description="Текущая доверенность")
    pass


@strawberry.input
class SignatureInput(SignatureType):
    pass


@strawberry.experimental.pydantic.type(model=Company, all_fields=True, description="Организация")
class CompanyType:
    pass


@strawberry.experimental.pydantic.type(model=Company, fields=["id", "address", "phone_or_fax"], description="Орган власти")
class CompanyGovType:
    name: str = Field(description="Наименование органа государственного строительного надзора")
    representative_id: List[RepresentativeType] = Field(description="Представитель")


@strawberry.experimental.pydantic.type(model=Company, fields=["id", "name", "number", "date_extradition", "ogrn", "inn", "address", "phone_or_fax"], description="Компания без представителя")
class CompanyWithoutRepresentativeType:
    pass


@strawberry.experimental.pydantic.type(model=Certificate, all_fields=True, description="Документ")
class CertificateType:
    # files: List[Upload] = Field(description="Скан")
    pass


@strawberry.input
class CertificateInput(CertificateType):
    pass

