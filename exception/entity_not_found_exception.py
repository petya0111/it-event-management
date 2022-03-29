from exception.base_exception import BaseUserException


class EntityNotFoundException(BaseUserException):
    def __init__(self, id):
        self.message = f'Entity with ID:{id} not found'
