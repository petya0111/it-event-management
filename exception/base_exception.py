class BaseUserException(Exception):
    def __init__(self, message: str, error_code: int):
        self.message = message
        self.error_code = 400
