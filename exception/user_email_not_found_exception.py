from exception.base_exception import BaseUserException


class UserEmailNotFoundException(BaseUserException):
    def __init__(self, id):
        self.message = f'User with email:{id} not found'
