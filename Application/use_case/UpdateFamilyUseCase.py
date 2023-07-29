from Infrastructure.repository.FamilyRepository import FamilyRepository
from Domain.family.entities import UpdateFamily, AddedFamily


class UpdateFamilyUseCase:
    def __init__(self, family_repository: FamilyRepository):
        self.family_repository = family_repository

    def execute(self, request):
        update_family = UpdateFamily(**request)

        self.family_repository.getFamilyById(update_family.id)
        self.family_repository.updateCoOwner(
            update_family.id, update_family.owner_id, update_family.co_owner_id
        )
        added_family = self.family_repository.getFamilyById(update_family.id)
        result = AddedFamily(*added_family)

        return result.__dict__
