from Commons.exceptions import InvariantError


class AddedFamilyMember:
    def __init__(self, *args):
        self.id = args[0]
        self.family_id = args[1]
        self.user_id = args[2]
        self.daily_limit = args[3]

        if (
            self.id is None
            or self.family_id is None
            or self.user_id is None
            or self.daily_limit is None
        ):
            raise InvariantError("ADDED_FAMILY_MEMBER.NOT_CONTAIN_NEEDED_PROPERTY")

        if (
            not isinstance(self.id, int)
            or not isinstance(self.family_id, int)
            or not isinstance(self.user_id, int)
            or not isinstance(self.daily_limit, float)
        ):
            raise InvariantError("ADDED_FAMILY_MEMBER.NOT_MEET_DATA_TYPE_SPECIFICATION")
