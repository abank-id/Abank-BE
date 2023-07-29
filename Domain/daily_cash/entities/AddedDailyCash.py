from Commons.exceptions import InvariantError
from datetime import date


class AddedDailyCash:
    def __init__(self, *args):
        self.id = args[0]
        self.user_id = args[1]
        self.day = args[2]
        self.spending = args[3]

        print(args)

        if (
            self.id is None
            or self.user_id is None
            or self.day is None
            or self.spending is None
        ):
            raise InvariantError("ADDED_DAILY_CASH.NOT_CONTAIN_NEEDED_PROPERTY")

        if (
            not isinstance(self.id, int)
            or not isinstance(self.user_id, int)
            or not isinstance(self.day, date)
            or not isinstance(self.spending, float)
        ):
            raise InvariantError("ADDED_DAILY_CASH.NOT_MEET_DATA_TYPE_SPECIFICATION")
