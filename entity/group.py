

class Group:

    def __init__(self, name: str, description: str, user_ids: list[int], event_ids: list[str], id=None):
        self._allowed_event_ids_for_group = []
        self._id = id
        self._user_ids = user_ids
        self._event_ids = event_ids
        self._name = name
        self._description = description

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def user_ids(self):
        return self._user_ids

    @user_ids.setter
    def user_ids(self, user_ids):
        self._user_ids = user_ids

    @property
    def event_ids(self):
        return self._event_ids

    @event_ids.setter
    def event_ids(self, event_ids):
        self._event_ids = event_ids

    @property
    def allowed_event_ids_for_group(self):
        return self._allowed_event_ids_for_group

    @allowed_event_ids_for_group.setter
    def allowed_group_ids_for_event(self, allowed_event_ids_for_group):
        self._allowed_event_ids_for_group = allowed_event_ids_for_group

    @classmethod
    def from_json(cls, prop_dict):
        return cls[prop_dict['id'],
                   prop_dict['name'],
                   prop_dict['description'],
                   prop_dict['user_ids'],
                   prop_dict['event_ids'],
                   prop_dict['allowed_event_ids_for_group']]

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            "description": self.description,
            "user_ids": self._user_ids,
            "event_ids": self.event_ids,
            "allowed_event_ids_for_group": self.allowed_group_ids_for_event,
            '_module': self.__class__.__module__,
            '_class': self.__class__.__name__
        }

    def get_formatted_str(self):
        return f'| {self.id:24s} | {self.name:30.30s} | {self.description:40.40s} |  {str(self.allowed_group_ids_for_event):20.20s} | '


class GroupUser:
    def __init__(self, user_ids: list[str], group_id):
        self.user_ids = user_ids
        self.group_id = group_id
