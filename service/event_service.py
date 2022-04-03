from datetime import datetime

from dao.event_repository import EventRepository
from entity.event import Event, EventStatusName, EventPost, EventInvitation, InvitationResponseTypeName, EventTicket
from entity.user import User, RoleName
from exception.already_registered_for_event_exception import AlreadyRegisteredForEventExcetion
from exception.not_host_modification_event_exception import NotHostCreationEventException
from exception.not_permitted_to_register_exception import NotPermittedToRegisterException


class EventService(EventRepository):
    def __init__(self):
        super().__init__()

    def check_permitted_to_modify(self, host: User):
        if host.role not in [RoleName.HOST, RoleName.ADMIN]:
            raise NotHostCreationEventException()

    def create_event_from_host(self, user: User, event: Event):
        self.check_permitted_to_modify(user)
        event.creation_user_id = user.id
        event.status_name = EventStatusName.OPEN_FOR_REGISTRATIONS
        self.create(event)

    def update_event_from_host(self, user: User, event: Event):
        self.check_permitted_to_modify(user)
        self.update(event)

    def add_event_post(self, user: User, event_id: str, event_post: EventPost):
        self.check_permitted_to_modify(user)
        event: Event = self.find_by_id(event_id)
        event.event_post = event_post
        self.update(event)

    def respond_event_invitation(self, event_id: str, text_response: str, response_date: datetime,
                                 invitation_response: InvitationResponseTypeName):
        event: Event = self.find_by_id(event_id)
        event.event_invitation.text_response = text_response
        event.event_invitation.response_date = response_date
        event.event_invitation.invitation_response = invitation_response
        self.update(event)

    def send_event_invitation(self, event_id: str, event_invitation: EventInvitation):
        event: Event = self.find_by_id(event_id)
        event.event_invitation = event_invitation
        self.update(event)

    def take_ticket(self, event_id: str, event_ticket: EventTicket):
        event: Event = self.find_by_id(event_id)
        event.event_ticket = event_ticket
        self.update(event)

    def check_if_already_registered_in_event(self, user_id: str, event: Event):
        if user_id in event.registered_user_ids:
            raise AlreadyRegisteredForEventExcetion(user_id)

    def register_for_event(self, event: Event, user: User, paid_date: datetime, is_paid: bool):
        user_id = user.id
        self.check_if_already_registered_in_event(user_id, event)
        if event.status_name != EventStatusName.OPEN_FOR_REGISTRATIONS:
            raise NotPermittedToRegisterException()
        event.event_ticket = EventTicket(event_id=event.id, text=event.event_post.text, paid_date=paid_date,
                                         is_paid=is_paid)
        event.event_ticket.owner_ids.append(user_id)
        event.registered_user_ids.append(user_id)
        self.update(event)

    def save_json(self):
        self.save()

    def load_json(self):
        self.load()
