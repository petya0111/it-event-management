from dao.repository import Repository
from entity.event import Event
from entity.user import User, RoleName
from exception.already_registered_for_event_exception import AlreadyRegisteredForEventExcetion
from exception.not_host_creation_event_exception import NotHostCreationEventException
from utils.id_generator_uuid import IdGeneratorUuid


class EventRepository(Repository):
    def __init__(self):
        super().__init__(IdGeneratorUuid())

    def check_for_already_registered_user(self, user_id:str, event: Event):
        if str(user_id) in event.registered_user_ids:
            raise AlreadyRegisteredForEventExcetion(str(user_id))

    def register_for_event(self, event: Event, user: User):
        self.check_for_already_registered_user(user.id,event)
        event.registered_user_ids.append(user.id)
        self.update(event)

    def create_event_from_host(self, user: User, event: Event):
        if user.role.role_name != RoleName.HOST:
            raise NotHostCreationEventException()
        event.creation_user_id = user.id
        self.create(event)
