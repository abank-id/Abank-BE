from Commons.exceptions import InvariantError
from Infrastructure.repository import FamilyMemberRepository, FamilyRepository
from Domain.family.entities import AddedFamily
from Domain.family_member.entities import (
    GetFamilyMember,
    FamilyMembers,
)


class GetFamilyMemberUseCase:
    def __init__(
        self,
        family_member_repository: FamilyMemberRepository,
        family_repository: FamilyRepository,
    ):
        self.family_member_repository = family_member_repository
        self.family_repository = family_repository

    def execute(self, request):
        family_member = GetFamilyMember(**request)

        row_family = self.family_repository.getFamilyById(family_member.family_id)

        added_family = AddedFamily(*row_family)

        row_family_members = self.family_member_repository.getFamilyMember(
            added_family.id
        )

        result = FamilyMembers(
            row_family_members, added_family.owner_id, added_family.co_owner_id
        ).members

        return result
