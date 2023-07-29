from Commons.exceptions import InvariantError


class UpdateFamily:
    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.owner_id = kwargs.get("owner_id")
        self.co_owner_id = kwargs.get("co_owner_id")

        if self.id is None or self.owner_id is None:
            raise InvariantError("UPDATE_FAMILY.NOT_CONTAIN_NEEDED_PROPERTY")

        if (
            not isinstance(self.id, int)
            or not isinstance(self.owner_id, int)
            or not (isinstance(self.co_owner_id, int) or self.co_owner_id is None)
        ):
            raise InvariantError("UPDATE_FAMILY.NOT_MEET_DATA_TYPE_SPECIFICATION")
