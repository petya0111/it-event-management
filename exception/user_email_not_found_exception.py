from exception.base_exception import BaseUserException


class UserEmailNotFoundException(BaseUserException):
    def __init__(self, email):
        self.message = f'User with email:{email} not found'
