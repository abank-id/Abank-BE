from Commons.exceptions import InvariantError


class Contact:
    def __init__(self, contactRow: tuple):
        self.username = contactRow[0]
        self.phone_number = contactRow[1]

        if self.username is None or self.phone_number is None:
            raise InvariantError("CONTACT.NOT_CONTAIN_NEEDED_PROPERTY")

        if not isinstance(self.username, str) or not isinstance(self.phone_number, str):
            raise InvariantError("CONTACT.NOT_MEET_DATA_TYPE_SPECIFICATION")
