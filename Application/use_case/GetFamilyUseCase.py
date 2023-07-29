from Infrastructure.repository.FamilyRepository import FamilyRepository
from Domain.family.entities import AddFamily, AddedFamily


class GetFamilyUseCase:
    def __init__(self, family_repository: FamilyRepository):
        self.family_repository = family_repository

    def execute(self, request):
        add_family = AddFamily(**request)

        added_family = self.family_repository.getFamilyByOwnerId(add_family.owner_id)
        result = AddedFamily(*added_family)

        return result.__dict__
