from Infrastructure.repository import DailyCashRepository
from Domain.daily_cash.entities import AddDailyCash, AddedDailyCash


class AddDailyCashUseCase:
    def __init__(self, daily_cash_repository: DailyCashRepository):
        self.daily_cash_repository = daily_cash_repository

    def execute(self, request):
        add_daily_cash = AddDailyCash(**request)

        self.daily_cash_repository.verifyDailyCashAvailability(
            add_daily_cash.user_id, add_daily_cash.day
        )
        self.daily_cash_repository.createDailyCash(add_daily_cash)
        added_daily_cash = self.daily_cash_repository.getDailyCash(
            add_daily_cash.user_id, add_daily_cash.day
        )

        result = AddedDailyCash(*added_daily_cash)

        return result.__dict__
