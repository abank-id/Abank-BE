from Infrastructure.repository import UserRepository
from Domain.users.entities import AddUser, AddedUser


class AddUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, request):
        print(request, type(request))
        add_user = AddUser(**request)

        self.user_repository.verifyAvailableId(add_user.user_id)
        self.user_repository.addUser(add_user)
        added_user = self.user_repository.getLastAddedUser()
        result = AddedUser(*added_user)

        return result.__dict__
