from enum import Enum

from entity.group import Group


class RoleName(Enum):
    ADMIN = 1,
    HOST = 2,
    GUEST = 3,
    ANONYMUS_USER = 4


class User:

    def __init__(self, first_name: str, last_name: str, email: str, password: str, bio: str, is_active: bool,
                 group: Group,
                 role: RoleName = RoleName.ANONYMUS_USER,
                 id=None):
        self._id = id
        self._role = role
        self._group = group
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._password = password
        self._bio = bio
        self._is_active = is_active

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def bio(self):
        return self._bio

    @bio.setter
    def bio(self, bio):
        self._bio = bio

    @property
    def is_active(self):
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        self._is_active = is_active

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, role):
        self._role = role

    @classmethod
    def from_json(cls, prop_dict):
        return cls[prop_dict['id'],
                   prop_dict['email'],
                   prop_dict['password'],
                   prop_dict['first_name'],
                   prop_dict['last_name'],
                   prop_dict['bio'],
                   prop_dict['is_active']]

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
        return f'| {self.id:24s} | {self.first_name:15.15s} | {self.last_name:15.15s} | {self.email:15.15s} | {str(self.role.name):35.35s} |'
