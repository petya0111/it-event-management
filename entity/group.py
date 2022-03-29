

class Group:

    def __init__(self, name: str, description: str, user_ids:list[int], id=None):
        self.id = id
        self.user_ids = user_ids
        self.name = name
        self.description = description


# search event in allowed groups
class AllowedEventGroup:
    def __init__(self, user_id: int, group: Group):
        self.user_id = user_id
        self.group_id = group.id
