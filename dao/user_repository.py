from dao.repository import Repository
from entity.event import Event
from entity.user import User
from exception.already_registered_for_event_exception import AlreadyRegisteredForEventExcetion


class UserRepository(Repository):
    def __init__(self, user: User):
        super().__init__()
