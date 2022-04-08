from exception.base_exception import BaseUserException


class CredentialsException(BaseUserException):
    def __init__(self):
        self.message = f'Invalid username or password. Try again.'
