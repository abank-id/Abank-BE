from Commons.exceptions import InvariantError


class GetFamilyMember:
    def __init__(self, **kwargs):
        self.family_id = kwargs.get("family_id")

        if self.family_id is None:
            raise InvariantError("GET_FAMILY_MEMBER.NOT_CONTAIN_NEEDED_PROPERTY")

        if not isinstance(self.family_id, int):
            raise InvariantError("GET_FAMILY_MEMBER.NOT_MEET_DATA_TYPE_SPECIFICATION")
