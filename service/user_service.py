from dao.user_repository import UserRepository
from entity.user import User


class UserService():
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    def create(self, user: User):
        self._user_repository.create(user)

    def get_role(self,user_id):
        return self._user_repository.get_role_of_user(user_id)

    def find_all_users(self):
        self._user_repository.find_all()

    def register(self, user: User):
        self._user_repository.create(user)

    def update_data(self, user: User):
        self._user_repository.update(user)

    def find_all(self):
        self._user_repository.find_all()

    def save(self):
        self._user_repository.save()

    def load(self):
        self._user_repository.load()

    def find_by_email(self, email):
        self._user_repository.find_by_email(email)

    def update(self, user):
        self._user_repository.update(user)