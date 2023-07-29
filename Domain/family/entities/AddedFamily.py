from Commons.exceptions import InvariantError


class AddedFamily:
    def __init__(self, *args):
        self.id = args[0]
        self.owner_id = args[1]
        self.co_owner_id = args[2]

        print(self.id, self.owner_id, self.co_owner_id)
        print(type(self.id), type(self.owner_id), type(self.co_owner_id))

        if self.id is None or self.owner_id is None:
            raise InvariantError("ADDED_FAMILY.NOT_CONTAIN_NEEDED_PROPERTY")

        if (
            not isinstance(self.id, int)
            or not isinstance(self.owner_id, int)
            or not (isinstance(self.co_owner_id, int) or self.co_owner_id is None)
        ):
            raise InvariantError("ADDED_FAMILY.NOT_MEET_DATA_TYPE_SPECIFICATION")
