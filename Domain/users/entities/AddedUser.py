from Commons.exceptions import InvariantError


class AddedUser:
    def __init__(self, *args):
        self.id = args[0]
        self.user_id = args[1]
        self.ktpid = args[2]
        self.username = args[3]
        self.phone_number = args[4]
        self.email = args[5]

        if (
            self.id is None
            or self.user_id is None
            or self.ktpid is None
            or self.username is None
            or self.phone_number is None
            or self.email is None
        ):
            raise InvariantError("REGISTERED_USER.NOT_CONTAIN_NEEDED_PROPERTY")

        if (
            not isinstance(self.id, int)
            or not isinstance(self.user_id, int)
            or not isinstance(self.ktpid, str)
            or not isinstance(self.username, str)
            or not isinstance(self.phone_number, str)
            or not isinstance(self.email, str)
        ):
            raise InvariantError("REGISTERED_USER.NOT_MEET_DATA_TYPE_SPECIFICATION")
