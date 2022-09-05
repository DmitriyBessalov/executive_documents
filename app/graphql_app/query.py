import strawberry
from typing import List, Optional

from models.base import Journal, Certificate, PowerAttorney
from service import crud

from shemas.base import CertificateType, PowerAttorneyType
from shemas.journal.base import JournalType


@strawberry.type
class Query:
    @strawberry.field(description="Свидетельство получить")
    async def certificate_read(self, id: int) -> CertificateType:
        return await crud.read(Certificate, id)

    @strawberry.field(description="Доверенность получить")
    async def power_attorney_read(self, id: int) -> PowerAttorneyType:
        return await crud.read(PowerAttorney, id)

    @strawberry.field(description="Журналы получить все")
    async def journal_read_all(self) -> Optional[List[JournalType]]:
        return await crud.read_all(Journal)

