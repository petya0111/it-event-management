class Group:

    def __init__(self, name: str = None, description: str = None, user_ids=None, event_ids=None, id=None):
        self.allowed_event_ids_for_group = []
        self.id = id
        self.user_ids = user_ids
        self.event_ids = event_ids
        self.name = name
        self.description = description

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            "description": self.description,
            "user_ids": self.user_ids,
            "event_ids": self.event_ids,
            "allowed_event_ids_for_group": self.allowed_event_ids_for_group,
            '_module': self.__class__.__module__,
            '_class': self.__class__.__name__
        }

    def get_formatted_str(self):
        return f'| {self.id:24s} | {self.name:30.30s} | {self.description:40.40s} |  {str(self.allowed_event_ids_for_group):20.20s} | '


class GroupUser:
    def __init__(self, user_ids: list[str], group_id):
        self.user_ids = user_ids
        self.group_id = group_id
