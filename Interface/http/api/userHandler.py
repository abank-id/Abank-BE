from flask import request, jsonify
from Application.use_case import AddUserUseCase, GetContactListUseCase
from Infrastructure.repository import UserRepository


class UserHandler:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def postUser(self):
        request_body = request.get_json()
        response_data = AddUserUseCase(self.user_repository).execute(request_body)
        print(response_data)

        response = {"status": "success", "data": response_data}

        return jsonify(response), 200

    def getContactList(self):
        response_data = GetContactListUseCase(self.user_repository).execute()

        response = {"status": "success", "data": response_data}

        return jsonify(response), 200
