from Commons.exceptions import InvariantError
from Domain.users.entities.Contact import Contact


class ContactList:
    def __init__(self, contacts: list):
        self.contacts = []

        for c in contacts:
            _c = Contact(c).__dict__
            self.contacts.append(_c)
