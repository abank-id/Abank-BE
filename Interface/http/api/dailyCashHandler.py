from flask import request, jsonify
from Application.use_case import AddDailyCashUseCase
from Infrastructure.repository import DailyCashRepository


class DailyCashHandler:
    def __init__(self, daily_cash_repository: DailyCashRepository):
        self.daily_cash_repository = daily_cash_repository

    def postDailyCash(self, user_id):
        request_body = request.get_json()
        response_data = AddDailyCashUseCase(self.daily_cash_repository).execute(
            request_body
        )
        print(response_data)

        response = {"status": "success", "data": response_data}

        return jsonify(response), 200
