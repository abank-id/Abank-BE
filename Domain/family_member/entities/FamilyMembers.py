from .FamilyMember import FamilyMember


class FamilyMembers:
    def __init__(self, rows_member, owner_id, co_owner_id):
        self.members = []

        for row in rows_member:
            print(row)
            self.members.append(FamilyMember(owner_id, co_owner_id, row).__dict__)
