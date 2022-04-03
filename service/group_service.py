from dao.group_repository import GroupRepository
from entity.group import Group
from exception.event_not_allowed_for_group_exception import EventNotAllowedForGroupException


class GroupService(GroupRepository):
    def __init__(self):
        super().__init__()

    def allow_event_in_group(self, event_id: str, group_id: str):
        group: Group = self.find_by_id(group_id)
        group.allowed_event_ids_for_group.append(event_id)
        self.update(group)

    def check_event_allowed_group(self, group_id: str, event_id: str) -> bool:
        group: Group = self.find_by_id(group_id)
        if event_id not in group.allowed_group_ids_for_event:
            raise EventNotAllowedForGroupException(event_id, group.name)
        return True

    def save_json(self):
        self.save()

    def load_json(self):
        self.load()