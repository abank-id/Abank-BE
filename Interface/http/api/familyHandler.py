from flask import request, jsonify
from Application.use_case import AddFamilyUseCase, GetFamilyUseCase, UpdateFamilyUseCase
from Infrastructure.repository import FamilyRepository


class FamilyHandler:
    def __init__(self, family_repository: FamilyRepository):
        self.family_repository = family_repository

    def postFamily(self):
        request_body = request.get_json()
        response_data = AddFamilyUseCase(self.family_repository).execute(request_body)
        print(response_data)

        response = {"status": "success", "data": response_data}

        return jsonify(response), 200

    def putFamily(self):
        request_body = request.get_json()
        response_data = UpdateFamilyUseCase(self.family_repository).execute(
            request_body
        )
        print(response_data)

        response = {"status": "success", "data": response_data}

        return jsonify(response), 200

    def getFamilyByOwnerId(self):
        request_body = request.get_json()
        response_data = GetFamilyUseCase(self.family_repository).execute(request_body)
        print(response_data)

        response = {"status": "success", "data": response_data}

        return jsonify(response), 200
