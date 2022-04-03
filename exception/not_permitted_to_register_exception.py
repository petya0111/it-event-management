from exception.base_exception import BaseUserException


class NotPermittedToRegisterException(BaseUserException):
    def __init__(self):
        self.message = f'User can not register in closed for registrations event'
