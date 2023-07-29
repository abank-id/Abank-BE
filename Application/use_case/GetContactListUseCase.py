from Domain.users.entities import ContactList
from Infrastructure.repository import UserRepository


class GetContactListUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self):
        result = self.user_repository.getContactList()
        contacts = ContactList(result)

        return contacts.contacts
