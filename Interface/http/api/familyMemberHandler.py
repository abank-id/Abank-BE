from flask import request, jsonify
from Application.use_case import AddFamilyMemberUseCase, GetFamilyMemberUseCase
from Infrastructure.repository import FamilyMemberRepository, FamilyRepository


class FamilyMemberHandler:
    def __init__(
        self,
        family_member_repository: FamilyMemberRepository,
        family_repository: FamilyRepository,
    ):
        self.family_repository = family_repository
        self.family_member_repository = family_member_repository

    def postFamilyMember(self, family_id):
        request_body = request.get_json()
        request_body["family_id"] = family_id

        print(request_body)

        response_data = AddFamilyMemberUseCase(self.family_member_repository).execute(
            request_body
        )
        print(response_data)

        response = {"status": "success", "data": response_data}

        return jsonify(response), 200

    def getFamilyMember(self, family_id):
        print(family_id, type(family_id))
        response_data = GetFamilyMemberUseCase(
            self.family_member_repository, self.family_repository
        ).execute(request={"family_id": family_id})

        response = {"status": "success", "data": response_data}

        return jsonify(response), 200
