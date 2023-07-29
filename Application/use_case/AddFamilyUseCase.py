from Infrastructure.repository.FamilyRepository import FamilyRepository
from Domain.family.entities import AddFamily, AddedFamily


class AddFamilyUseCase:
    def __init__(self, family_repository: FamilyRepository):
        self.family_repository = family_repository

    def execute(self, request):
        add_family = AddFamily(**request)

        self.family_repository.verifyFamilyAvailability(add_family.owner_id)
        self.family_repository.addFamily(add_family)
        added_family = self.family_repository.getLastAddedFamily()
        result = AddedFamily(*added_family)

        return result.__dict__
