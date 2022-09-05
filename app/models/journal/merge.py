from models.base import Journal
from models.journal.job.general_work import JournalGeneralWork
from models.journal.material.material_all import JournalMaterialAll


class JournalGeneralWorkMerge(Journal, JournalGeneralWork):
    pass


class JournalMaterialMerge(Journal, JournalMaterialAll):
    pass
