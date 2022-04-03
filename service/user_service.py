from dao.user_repository import UserRepository
from entity.user import RoleName, User


class UserService(UserRepository):
    def __init__(self):
        super().__init__()

    def find_all_users(self):
        self.find_all()

    def register(self, user: User):
        self.create(user)

    def update_data(self, user: User):
        self.update(user)

    def find_user_by_email(self, email: str):
        self.find_by_user_email(email)

    def save_json(self):
        self.save()

    def load_json(self):
        self.load()