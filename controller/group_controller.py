from dao.group_repository import GroupRepository
from entity.group import Group
from exception.event_not_allowed_for_group_exception import EventNotAllowedForGroupException
from service.group_service import GroupService


class GroupController():
    def __init__(self, service: GroupService):
        self._service = service

    def create(self, group: Group):
        self._service.create(group)

    def update(self, group: Group):
        self._service.update(group)

    def find_by_name(self, name: str):
        self._service.find_by_name(name)

    def find_all(self):
        return self._service.find_all()

