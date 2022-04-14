from dao.json_repository import JsonRepository
from entity.user import User, RoleName
from utils.fuction_utils import find_first


class UserRepository(JsonRepository):
    def __init__(self, id_generator, file_name):
        super().__init__(id_generator, file_name)

    def find_by_email(self, email: str) -> User | None:
        return find_first(lambda u: u.email == email, self.find_all())

    def get_role_of_user(self,user_id):
        user = self.find_by_id(user_id)
        return user.role.name