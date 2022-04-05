from dao.json_repository import JsonRepository
from entity.group import Group
from utils.fuction_utils import find_first


class GroupRepository(JsonRepository):
    def __init__(self, id_generator, file_name):
        super().__init__(id_generator, file_name)

    def find_by_name(self, name: str) -> Group | None:
        return find_first(lambda u: u.name == name, self.find_all())
