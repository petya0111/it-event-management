from dao.json_repository import JsonRepository
from entity.user import User
from utils.fuction_utils import find_first


class UserRepository(JsonRepository):
    def __init__(self, id_generator, file_name):
        super().__init__(id_generator, file_name)

    def find_by_email(self, email: str) -> User | None:
        return find_first(lambda u: u.email == email, self.find_all())
