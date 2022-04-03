from exception.base_exception import BaseUserException


class NotHostCreationEventException(BaseUserException):
    def __init__(self):
        self.message = f'Only host of events can create events.'
