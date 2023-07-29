from Domain.users.entities import AddUser
from nanoid import generate
from Commons.exceptions import InvariantError
from Infrastructure.database.DatabaseService import Database


class UserRepository:
    def __init__(self, database: Database):
        self.db = database

    # hanya id yang diverfikiasi karena sudah diverifikasi di API yang disediakan
    def verifyAvailableId(self, id):
        result = self.db.execute("SELECT * FROM users WHERE user_id = %s", (id,))

        if len(result) > 0:
            raise InvariantError("id not available")

    def addUser(self, add_user: AddUser):
        self.db.execute(
            "INSERT INTO users (user_id, ktpid, username, phone_number, email) VALUES (%s, %s, %s, %s, %s)",
            (
                add_user.user_id,
                add_user.ktpid,
                add_user.username,
                add_user.phone_number,
                add_user.email,
            ),
        )

        return add_user.user_id

    def getLastAddedUser(self):
        result = self.db.execute("SELECT * FROM users WHERE id = last_insert_id()")

        return result[0]
