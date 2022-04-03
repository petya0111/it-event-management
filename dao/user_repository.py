from dao.json_repository import JsonRepository
from exception.user_email_not_found_exception import UserEmailNotFoundException
from dao.id_generator_uuid import IdGeneratorUuid
from utils.fuction_utils import find_first


class UserRepository(JsonRepository):
    def __init__(self):
        super().__init__(IdGeneratorUuid(),'output_json_db/users_db.json')

    def find_by_user_email(self, email: str):
        found = find_first(lambda u: u.email == email, self.find_all())
        if found is None:
            raise UserEmailNotFoundException(email)
        return found
