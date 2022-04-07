from dao.user_repository import UserRepository
from entity.user import  User
from service.user_service import UserService


class UserController():
    def __init__(self, service: UserService):
        self._service = service

    def create(self, user: User):
        self._service.create(user)

    def find_all_users(self):
        self._service.find_all()

    def register(self, user: User):
        self._service.create(user)

    def update_data(self, user: User):
        self._service.update(user)

    def find_user_by_email(self, email: str):
        self._service.find_by_email(email)

    def get_all_users(self):
        self._service.find_all()
