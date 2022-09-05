import strawberry

from models.base import Certificate, PowerAttorney, Signature, Journal
from models.journal.job.general_work import JournalGeneralWork
from models.journal.merge import JournalGeneralWorkMerge
from service import crud

from shemas.base import CertificateInput, CertificateType, PowerAttorneyInput, PowerAttorneyType, SignatureInput, \
    SignatureType
from shemas.journal.base import JournalGeneralWorkType
from shemas.journal.job.general_work import JournalGeneralWorkInput


@strawberry.type
class Mutation:
    @strawberry.mutation(description="Свидетельство добавить")
    async def certificate_create(self, data: CertificateInput) -> CertificateType:
        return await crud.create(Certificate, data)

    @strawberry.mutation(description="Свидетельство обновить")
    async def certificate_update(self, data: CertificateInput) -> CertificateType:
        return await crud.update(Certificate, data)

    @strawberry.mutation(description="Свидетельство удалить")
    async def certificate_delete(self, id: int) -> bool:
        return await crud.delete(Certificate, id)

    @strawberry.mutation(description="Доверенность добавить")
    async def power_attorney_create(self, data: PowerAttorneyInput) -> PowerAttorneyType:
        return await crud.create(PowerAttorney, data)

    @strawberry.mutation(description="Доверенность обновить")
    async def power_attorney_update(self, data: PowerAttorneyInput) -> PowerAttorneyType:
        return await crud.update(PowerAttorney, data)

    @strawberry.mutation(description="Доверенность удалить")
    async def power_attorney_delete(self, id: int) -> bool:
        return await crud.delete(PowerAttorney, id)

    @strawberry.mutation(description="Подпись добавить")
    async def signature_create(self, data: SignatureInput) -> SignatureType:
        return await crud.create(Signature, data)

    @strawberry.mutation(description="Подпись удалить")
    async def signature_delete(self, id: int) -> bool:
        return await crud.delete(Signature, id)

    @strawberry.mutation(description="Общий журнал работ добавить")
    async def journal_general_work_create(self, data: JournalGeneralWorkInput) -> JournalGeneralWorkType:
        return await crud.journal_create(Journal, JournalGeneralWork, JournalGeneralWorkMerge, data)

    @strawberry.mutation(description="Общий журнал работ изменить")
    async def journal_general_work_update(self, data: JournalGeneralWorkInput) -> JournalGeneralWorkType:
        return await crud.journal_update(Journal, JournalGeneralWork, JournalGeneralWorkMerge, data)

    @strawberry.mutation(description="Журнал удалить")
    async def journal_delete(self, id: int) -> bool:
        return await crud.delete(Journal, id)

