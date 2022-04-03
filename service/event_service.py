from dao.event_repository import EventRepository
from entity.event import Event, EventStatusName
from entity.user import User, RoleName
from exception.already_registered_for_event_exception import AlreadyRegisteredForEventExcetion
from exception.not_host_creation_event_exception import NotHostCreationEventException
from exception.not_permitted_to_register_exception import NotPermittedToRegisterException


class EventService(EventRepository):
    def __init__(self):
        super().__init__()

    def check_if_already_registered_in_event(self, user_id: str, event: Event):
        if user_id in event.registered_user_ids:
            raise AlreadyRegisteredForEventExcetion(user_id)

    def register_for_event(self, event: Event, user: User):
        user_id = user.id
        self.check_if_already_registered_in_event(user_id, event)
        if event.status_name == EventStatusName.CLOSED_TO_REGISTRATIONS:
            raise NotPermittedToRegisterException()
        event.registered_user_ids.append(user_id)
        self.update(event)

    def create_event_from_host(self, user: User, event: Event):
        if user.role != RoleName.HOST:
            raise NotHostCreationEventException()
        event.creation_user_id = user.id
        event.status_name = EventStatusName.OPEN_FOR_REGISTRATIONS
        self.create(event)

    def update_event_from_host(self, user: User, event: Event):
        if user.role != RoleName.HOST:
            raise NotHostCreationEventException()
        self.update(event)

    def save_json(self):
        self.save()

    def load_json(self):
        self.load()