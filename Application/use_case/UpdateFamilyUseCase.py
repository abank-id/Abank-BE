from Infrastructure.repository.FamilyRepository import FamilyRepository
from Domain.family.entities import UpdateFamily, AddedFamily


class UpdateFamilyUseCase:
    def __init__(self, family_repository: FamilyRepository):
        self.family_repository = family_repository

    def execute(self, request):
        update_family = UpdateFamily(**request)

        self.family_repository.getFamilyByOwnerId(update_family.owner_id)
        self.family_repository.updateCoOwner(update_family)
        added_family = self.family_repository.getFamilyByOwnerId(update_family.owner_id)
        result = AddedFamily(*added_family)

        return result.__dict__
