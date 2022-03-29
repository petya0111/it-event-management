from enum import Enum

from entity.group import Group


class RoleName(Enum):
    ADMIN = "Admin",
    HOST = "Host",
    GUEST = "Guest in event"


class Role:
    def __init__(self, role_name: RoleName, description: str, id=None):
        self.id = id
        self.role_name = role_name
        self.description = description

    def __str__(self):
        return f'{self.id}) {self.role_name.name} {self.description}'


class User:

    def __init__(self, first_name: str, last_name: str, email: str, bio: str, is_active: bool, role: Role, group: Group, id=None):
        self.id = id
        self.role = role
        self.group = group
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.bio = bio
        self.is_active = is_active

    def __str__(self):
        return f'{self.id} {self.role.role_name.name} {self.first_name} {self.last_name} {self.email} {self.bio} is active: {self.is_active}'


class UserRole:
    def __init__(self, user: User, role: Role):
        self.user_id = user.id
        self.role_id = role.id
