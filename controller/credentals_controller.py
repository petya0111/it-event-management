
from entity.user import  User
from service.credentials_service import CredentialsService


class CredentialsController():
    def __init__(self, service: CredentialsService,view=None):
        self.view= view
        self._service = service

    def register(self, user: User) -> User:
        user =self._service.register(user)
        return user


    def login(self, email: str, password: str)->User:
        return self._service.login(email,password)

    def logout(self):
        self._service.logout()

    def get_logged_user(self) -> str:
        if self._service.get_logged_user() is not None:
            return self._service.get_logged_user().id

    def reload_users(self):
        return self._service.reload_users()

    def get_role(self, user_id):
        return self._service.get_role(user_id)
