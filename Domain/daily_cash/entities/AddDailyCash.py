from datetime import date
from Commons.exceptions import InvariantError


class AddDailyCash:
    def __init__(self, **kwargs):
        self.user_id = kwargs.get("user_id")
        self.day = kwargs.get("day")
        self.spending = kwargs.get("spending")

        if self.day is None:
            self.day = date.today().strftime("%Y-%m-%d %H:%M:%S")

        if self.user_id is None or self.spending is None:
            raise InvariantError("DAILY_CASH.NOT_CONTAIN_NEEDED_PROPERTY")

        if (
            not isinstance(self.user_id, int)
            or not isinstance(self.day, str)
            or not isinstance(self.spending, float)
        ):
            raise InvariantError("DAILY_CASH.NOT_MEET_DATA_TYPE_SPECIFICATION")
