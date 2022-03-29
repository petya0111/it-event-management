from user import User


class Group:

    def __init__(self, name: str, description: str, person: User, id=None):
        self.id = id
        self.person = person
        self.name = name
        self.description = description


# search event in allowed groups
class AllowedEventGroup:
    def __init__(self, person: User, group: Group):
        self.person_id = person.id
        self.group_id = group.id
