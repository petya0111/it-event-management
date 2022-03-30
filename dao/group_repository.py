import uuid

from dao.repository import Repository
from entity.group import AllowedEventGroup, Group
from exception.event_not_allowed_for_group_exception import EventNotAllowedForGroupException
from utils.id_generator_uuid import IdGeneratorUuid


class GroupRepository(Repository):
    def __init__(self):
        super().__init__(IdGeneratorUuid())

    def allow_event_in_group(self, event_ids: list[str], group_id: str):
        group: Group = self.find_by_id(group_id)
        group.allowed_event_group = AllowedEventGroup(event_ids=event_ids, group_id=group_id)
        self.update(group)

    def check_event_allowed_group(self, group_id:str,event_id: str):
        group: Group =  self.find_by_id(group_id)
        if event_id not in group.allowed_event_group.allowed_event_ids:
            raise EventNotAllowedForGroupException()
        return True