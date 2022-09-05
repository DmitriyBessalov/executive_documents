import strawberry

from models.base import Journal
from models.journal.merge import JournalGeneralWorkMerge


@strawberry.experimental.pydantic.type(model=Journal, all_fields=True, description="Основа Журнала")
class JournalType:
    # signature: Optional[SignatureType] = Field(description="Подпись")
    pass


@strawberry.experimental.pydantic.type(model=JournalGeneralWorkMerge, all_fields=True, description="Основа Журнала")
class JournalGeneralWorkType:
    # signature: Optional[SignatureType] = Field(description="Подпись")
    pass


