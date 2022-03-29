from dao.repository import Repository
from entity.user import User, RoleName, Role
from exception.already_registered_for_event_exception import AlreadyRegisteredForEventExcetion
from exception.user_email_not_found_exception import UserEmailNotFoundException
from utils.id_generator_uuid import IdGeneratorUuid


class UserRepository(Repository):
    def __init__(self):
        super().__init__(IdGeneratorUuid())

    def find_by_user_email(self, email: str):
        found: User
        for user in self._entities:
            if user.email == email:
                return user
        raise UserEmailNotFoundException(email)

    def create_role_for_user(self, role: RoleName):
        role = Role(role)
        return role
