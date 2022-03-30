from exception.base_exception import BaseUserException


class EventNotAllowedForGroupException(BaseUserException):
    def __init__(self, event_id: str, group_name: str):
        self.message = f"Event with id {event_id} is not allowed for group name {group_name}."
