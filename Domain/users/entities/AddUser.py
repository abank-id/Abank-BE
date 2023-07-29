from Commons.exceptions import InvariantError


class AddUser:
    def __init__(self, **kwargs):
        self.user_id = kwargs.get("user_id")
        self.ktpid = kwargs.get("ktpid")
        self.username = kwargs.get("username")
        self.phone_number = kwargs.get("phone_number")
        self.email = kwargs.get("email")

        if (
            self.user_id is None
            or self.ktpid is None
            or self.username is None
            or self.phone_number is None
            or self.email is None
        ):
            raise InvariantError("REGISTER_USER.NOT_CONTAIN_NEEDED_PROPERTY")

        if (
            not isinstance(self.user_id, int)
            or not isinstance(self.ktpid, str)
            or not isinstance(self.username, str)
            or not isinstance(self.phone_number, str)
            or not isinstance(self.email, str)
        ):
            raise InvariantError("REGISTER_USER.NOT_MEET_DATA_TYPE_SPECIFICATION")

        if len(self.ktpid) != 16:
            raise InvariantError("REGISTER_USER.KTPID_LENGTH_NOT_16")
