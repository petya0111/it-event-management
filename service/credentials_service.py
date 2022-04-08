from dao.user_repository import UserRepository
from entity.user import User
from exception.credentials_exception import CredentialsException


class CredentialsService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        self._logged_user = None

    def register(self, user: User) -> User:
        # TODO validate user
        created = self.user_repository.create(user)
        self.user_repository.save()
        return created

    def login(self, email: str, password: str) -> User:
        user = self.user_repository.find_by_email(email)
        if user is not None and user.password == password:
            self._logged_user = user
            return user
        raise CredentialsException()

    def logout(self):
        self._logged_user = None

    def get_logged_user(self) -> User:
        return self._logged_user

    def reload_users(self):
        return self.user_repository.load()