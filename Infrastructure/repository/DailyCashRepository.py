from Commons.exceptions import InvariantError
from Infrastructure.database.DatabaseService import Database
from Domain.daily_cash.entities import AddDailyCash


class DailyCashRepository:
    def __init__(self, database: Database):
        self.db = database

    def verifyDailyCashAvailability(self, user_id, day):
        result = self.db.execute(
            "SELECT * FROM daily_cash WHERE user_id = %s AND day = %s", (user_id, day)
        )

        if len(result) > 0:
            raise InvariantError("daily cash already exist")

    def createDailyCash(self, add_daily_cash: AddDailyCash):
        self.db.execute(
            "INSERT INTO daily_cash (user_id, day, spending) VALUES (%s, %s, %s)",
            (add_daily_cash.user_id, add_daily_cash.day, add_daily_cash.spending),
        )

        return add_daily_cash.user_id

    def getDailyCash(self, user_id, day):
        result = self.db.execute(
            "SELECT * FROM daily_cash WHERE user_id = %s AND day = %s", (user_id, day)
        )

        return result[0]

    def updateDailyCash(self, add_daily_cash: AddDailyCash):
        self.db.execute(
            "UPDATE daily_cash SET daily_spending = %s WHERE user_id = %s AND day = %s",
            (add_daily_cash.spending, add_daily_cash.user_id, add_daily_cash.day),
        )

        return add_daily_cash.user_id
