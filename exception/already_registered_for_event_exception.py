from exception.base_exception import BaseUserException


class AlreadyRegisteredForEventExcetion(BaseUserException):
    def __init__(self, user_id: str):
        self.message = f"User with id {user_id} is already registered to this event."
