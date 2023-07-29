from Commons.exceptions import InvariantError


class FamilyMember:
    def __init__(self, owner_id, co_owner_id, row_member):
        self.user_id = row_member[0]
        self.username = row_member[1]
        self.spending = row_member[2]
        self.daily_limit = row_member[3]

        if self.username is None or self.spending is None or self.daily_limit is None:
            raise InvariantError("FAMILY_MEMBER.NOT_CONTAIN_NEEDED_PROPERTY")

        if (
            not isinstance(self.username, str)
            or not isinstance(self.spending, float)
            or not isinstance(self.daily_limit, float)
        ):
            raise InvariantError("FAMILY_MEMBER.NOT_MEET_DATA_TYPE_SPECIFICATION")

        if owner_id == self.user_id:
            self.role = "owner"
        elif co_owner_id == self.user_id:
            self.role = "co-owner"
        else:
            self.role = "member"
