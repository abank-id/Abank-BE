from Commons.exceptions import InvariantError
from Domain.family.entities import AddFamilyMember


class FamilyMemberRepository:
    def __init__(self, database):
        self.db = database

    def getFamilyByUserId(self, user_id):
        result = self.db.execute(
            "SELECT * FROM family_member WHERE user_id = %s LIMIT 1", (user_id,)
        )

        return result[0]

    def verifyUserInFamily(self, user_id):
        result = self.db.execute(
            "SELECT * FROM family_member WHERE user_id = %s", (user_id,)
        )

        if len(result) > 0:
            raise InvariantError("user already in family")

    def addFamilyMember(self, add_family_member: AddFamilyMember):
        self.db.execute(
            "INSERT INTO family_member (family_id, user_id, daily_limit) VALUES (%s, %s, %s)",
            (
                add_family_member.family_id,
                add_family_member.user_id,
                add_family_member.daily_limit,
            ),
        )

        return add_family_member.user_id

    def getLastAddedFamilyMember(self):
        result = self.db.execute(
            "SELECT * FROM family_member WHERE id = last_insert_id()"
        )

        return result[0]

    # def getFamilyMember(self, family_id):
    #     result = self.db.execute(
    #         "SELECT owner_id FROM family_member WHERE family_id = %s", (family_id,)
    #     )

    #     return result

    # def updateDailyBudget(self, owner_id, family_id, daily_budget):
    #     self.db.execute(
    #         "UPDATE family_member SET daily_budget = %s WHERE owner_id = %s AND family_id = %s",
    #         (daily_budget, owner_id, family_id),
    #     )

    #     return owner_id
