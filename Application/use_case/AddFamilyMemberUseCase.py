from Commons.exceptions import InvariantError
from Infrastructure.repository import FamilyMemberRepository
from Domain.family.entities import AddFamilyMember, AddedFamilyMember


class AddFamilyMemberUseCase:
    def __init__(self, family_member_repository: FamilyMemberRepository):
        self.family_member_repository = family_member_repository

    def execute(self, request):
        add_family_member = AddFamilyMember(**request)

        self.family_member_repository.verifyUserInFamily(add_family_member.user_id)
        self.family_member_repository.addFamilyMember(add_family_member)
        added_family_member = self.family_member_repository.getLastAddedFamilyMember()

        result = AddedFamilyMember(*added_family_member)

        return result.__dict__
