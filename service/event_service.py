from datetime import datetime

from dao.event_repository import EventRepository
from dao.user_repository import UserRepository
from entity.event_meeting import EventMeeting, EventStatusName, EventPost, EventInvitation, InvitationResponseTypeName, \
    EventTicket
from entity.user import User, RoleName
from exception.already_registered_for_event_exception import AlreadyRegisteredForEventExcetion
from exception.not_host_modification_event_exception import NotHostCreationEventException
import re

from exception.time_pattern_exception import TimePatternExcetion


class EventService():
    def __init__(self, event_repository: EventRepository, user_repository: UserRepository):
        self._event_repository = event_repository
        self._user_repository = user_repository


    def check_permitted_to_modify(self, user_id: str):
        user = self._user_repository.find_by_id(user_id)
        if type(user.role) == str:
            if user.role != RoleName.HOST.name and user.role != RoleName.ADMIN.name:
                raise NotHostCreationEventException()
        else:
            if user.role != RoleName.HOST and user.role != RoleName.ADMIN:
                raise NotHostCreationEventException()

    def create_event_from_host(self, user_id: str, event: EventMeeting):
        self.check_permitted_to_modify(user_id)
        event.creation_user_id = user_id
        event.status_name = EventStatusName.OPEN_FOR_REGISTRATIONS
        time_pattern = "([01]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]"
        if not re.search(time_pattern,event.start_time) or not re.search(time_pattern,event.end_time):
            raise TimePatternExcetion()
        event.registration_end_date = datetime.fromisoformat(f"{event.end_date} {event.end_time}")
        self._event_repository.create(event)
        self._event_repository.save()

    def is_event_from_same_host_id(self,event_id,host_id):
        event:EventMeeting = self._event_repository.find_by_id(event_id)
        if host_id == event.creation_user_id:
            return True
        return False

    def is_registered_event(self, event_id, user_id):
        event: EventMeeting = self._event_repository.find_by_id(event_id)
        if event.registered_user_ids == 0:
            return False
        if user_id in event.registered_user_ids:
            return True
        else:
            return False

    def update_event_from_host(self, user_id: str, event: EventMeeting):
        self.check_permitted_to_modify(user_id)
        # time_pattern = "([01]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]"
        # if not re.search(time_pattern, event.start_time) or not re.search(time_pattern, event.end_time):
        #     raise TimePatternExcetion()
        # event.registration_end_date = datetime.fromisoformat(f"{event.end_date} {event.end_time}")
        self._event_repository.update(event)
        self._event_repository.save()

    # def add_event_post(self, user_id: str, event_id: str, event_post: EventPost):
    #     self.check_permitted_to_modify(user_id)
    #     event: EventMeeting = self._event_repository.find_by_id(event_id)
    #     event.event_post = event_post
    #     self._event_repository.update(event)

    # def respond_event_invitation(self, event_id: str, text_response: str, response_date: datetime,
    #                              invitation_response: InvitationResponseTypeName):
    #     event: EventMeeting = self._event_repository.find_by_id(event_id)
    #     event.event_invitation.text_response = text_response
    #     event.event_invitation.response_date = response_date
    #     event.event_invitation.invitation_response = invitation_response
    #     self._event_repository.update(event)

    def send_event_invitation(self, event_id: str, event_invitation: EventInvitation):
        event: EventMeeting = self._event_repository.find_by_id(event_id)
        event.event_invitation = event_invitation
        self._event_repository.update(event)

    # def take_ticket(self, event_id: str, event_ticket: EventTicket):
    #     event: EventMeeting = self._event_repository.find_by_id(event_id)
    #     event.event_ticket = event_ticket
    #     self._event_repository.update(event)

    def check_if_already_registered_in_event(self, user_id: str, event: EventMeeting):
        if user_id in event.registered_user_ids:
            raise AlreadyRegisteredForEventExcetion(user_id)

    def register_for_event(self, event_id: str, user_id: str):
        event = self._event_repository.find_by_id(event_id)
        self.check_if_already_registered_in_event(user_id, event)
        # if event.status_name != EventStatusName.OPEN_FOR_REGISTRATIONS.name:
        #     raise NotPermittedToRegisterException()
        # event.event_ticket = EventTicket(event_id=event.id, text=event.event_post.text, paid_date=datetime.now(),
        #                                  is_paid=is_paid)
        # event.event_ticket.owner_ids.append(user_id)
        event.registered_user_ids.append(user_id)
        self._event_repository.update(event)
        self._event_repository.save()

    def find_by_id(self, id):
        return self._event_repository.find_by_id(id)

    def delete_by_id(self, id):
        self._event_repository.delete_by_id(id)
        self._event_repository.save()

    def find_all(self):
        return self._event_repository.find_all()

    def save(self):
        self._event_repository.save()

    def load(self):
        self._event_repository.load()
