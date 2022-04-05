from dao.group_repository import GroupRepository
from entity.group import Group
from exception.event_not_allowed_for_group_exception import EventNotAllowedForGroupException


class GroupService():
    def __init__(self, group_repo: GroupRepository):
        self._group_repo = group_repo

    def create(self, group: Group):
        self._group_repo.create(group)

    def update(self, group: Group):
        self._group_repo.update(group)

    def find_by_name(self, name: str):
        self._group_repo.find_by_name(name)

    def allow_event_in_group(self, event_id: str, group_id: str):
        group: Group = self._group_repo.find_by_id(group_id)
        group.allowed_event_ids_for_group.append(event_id)
        self._group_repo.update(group)

    def check_event_allowed_group(self, group_id: str, event_id: str) -> bool:
        group: Group = self._group_repo.find_by_id(group_id)
        if event_id not in group.allowed_event_ids_for_group:
            raise EventNotAllowedForGroupException(event_id, group.name)
        return True

    def find_all(self):
        return self._group_repo.find_all()

    def save(self):
        self._group_repo.save()

    def load(self):
        self._group_repo.load()