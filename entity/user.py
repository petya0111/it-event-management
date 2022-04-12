from enum import Enum


class RoleName(Enum):
    ADMIN = 1,
    HOST = 2,
    REGISTERED_USER = 3
    ANONYMOUS_USER = 4

    @classmethod
    def from_json(cls, prop_dict):
        return cls[prop_dict['name']]

    def to_json(self):
        return {
            'name': self.name,
            '_module': self.__class__.__module__,
            '_class': self.__class__.__name__
        }


class User:

    def __init__(self, first_name: str = None, last_name: str = None, email: str = None, password: str = None,
                 bio: str = None, is_active: bool = False,
                 group_id: str = None, role: RoleName = RoleName.ANONYMOUS_USER, id=None):
        self.id = id
        self.role = role
        self.group_id = group_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.bio = bio
        self.is_active = is_active

    def to_json(self):
        return {
            'id': self.id,
            'email': self.email,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "bio": self.bio,
            "role": self.role.name,
            "is_active": self.is_active,
            '_module': self.__class__.__module__,
            '_class': self.__class__.__name__
        }

    def __str__(self):
        return f'{self.id} {self.role.name} {self.first_name} {self.last_name} {self.email} {self.bio} is active: {self.is_active}'

    def get_formatted_str(self):
        return f'| {self.id:24s} | {self.first_name:15.15s} | {self.last_name:15.15s} | {self.email:15.15s} | ** {self.password:15.15s} | {self.role:35.35s} |'
