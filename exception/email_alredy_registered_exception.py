from exception.base_exception import BaseUserException


class EmailAlreadyRegisteredExcetion(BaseUserException):
    def __init__(self, email: str):
        self.message = f"User with email {email} is already registered."
