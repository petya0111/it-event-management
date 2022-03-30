

class AllowedEventGroup:
    def __init__(self, event_ids: list[str], group_id: str):
        self.allowed_event_ids = event_ids
        self.group_id = group_id

    def get_formatted_str(self):
        return f'| {str(self.allowed_event_ids):24s} | {self.group_id:30.30s} |'


class Group:

    def __init__(self, name: str, description: str, user_ids: list[int], event_ids: list[str], id=None):
        self.allowed_event_group = AllowedEventGroup
        self.id = id
        self.user_ids = user_ids
        self.event_ids = event_ids
        self.name = name
        self.description = description

    def get_formatted_str(self):
        return f'| {str(self.id):24s} | {self.name:30.30s} | {self.description:40.40s} |  {str(self.allowed_event_group.allowed_event_ids):20.20s} | '


class GroupUser:
    def __init__(self, user_ids: list[str], group_id):
        self.user_ids = user_ids
        self.group_id = group_id
