from flask import request, jsonify
from Application.use_case import AddFamilyMemberUseCase
from Infrastructure.repository import FamilyMemberRepository


class FamilyMemberHandler:
    def __init__(self, family_repository: FamilyMemberRepository):
        self.family_repository = family_repository

    def postFamilyMember(self, family_id):
        request_body = request.get_json()

        request_body["family_id"] = family_id
        print(request_body)

        response_data = AddFamilyMemberUseCase(self.family_repository).execute(
            request_body
        )
        print(response_data)

        response = {"status": "success", "data": response_data}

        return jsonify(response), 200
