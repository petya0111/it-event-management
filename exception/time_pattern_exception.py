from exception.base_exception import BaseUserException


class TimePatternExcetion(BaseUserException):
    def __init__(self):
        self.message = f"Time must be in format HH:MM:SS."
