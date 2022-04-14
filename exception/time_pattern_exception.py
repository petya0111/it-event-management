from exception.base_exception import BaseUserException


class TimePatternExcetion(BaseUserException):
    def __init__(self, field):
        self.message = f"Field '{field}' must be in format HH:MM:SS."
