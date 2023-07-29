from Commons.exceptions import InvariantError


class AddFamilyMember:
    def __init__(self, **kwargs):
        self.family_id = kwargs.get("family_id")
        self.user_id = kwargs.get("user_id")
        self.daily_limit = kwargs.get("daily_limit")

        if self.family_id is None or self.user_id is None or self.daily_limit is None:
            raise InvariantError("ADD_FAMILY.NOT_CONTAIN_NEEDED_PROPERTY")

        if (
            not isinstance(self.family_id, int)
            or not isinstance(self.user_id, int)
            or not isinstance(self.daily_limit, float)
        ):
            raise InvariantError("ADD_FAMILY.NOT_MEET_DATA_TYPE_SPECIFICATION")
