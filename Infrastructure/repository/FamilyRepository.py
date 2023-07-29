from Domain.family.entities import AddFamily
from nanoid import generate
from Commons.exceptions import InvariantError


class FamilyRepository:
    def __init__(self, database):
        self.db = database

    def getFamilyById(self, id):
        result = self.db.execute("SELECT * FROM family WHERE id = %s LIMIT 1", (id,))

        return result[0]

    def verifyFamilyAvailability(self, owner_id):
        result = self.db.execute(
            "SELECT * FROM family WHERE owner_id = %s", (owner_id,)
        )

        if len(result) > 0:
            raise InvariantError("user already in family")

    def verifyFamilyOwners(self, owner_id, family_id):
        result = self.db.execute(
            "SELECT * FROM family WHERE owner_id = %s AND family_id = %s",
            (owner_id, family_id),
        )

        if len(result) < 0:
            raise InvariantError("user not in family")

    def addFamily(self, add_family: AddFamily):
        self.db.execute(
            "INSERT INTO family (owner_id, co_owner_id) VALUES (%s, %s)",
            (add_family.owner_id, add_family.co_owner_id),
        )

        return add_family

    def getLastAddedFamily(self):
        result = self.db.execute("SELECT * FROM family WHERE id = last_insert_id()")

        return result[0]

    def updateCoOwner(self, id, owner_id, co_owner_id):
        result = self.db.execute(
            "UPDATE family SET co_owner_id = %s WHERE owner_id = %s AND id = %s",
            (co_owner_id, owner_id, id),
        )

        return owner_id
