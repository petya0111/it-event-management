from datetime import datetime

from entity.event_meeting import EventMeeting, EventStatusName, EventPost, EventInvitation, InvitationResponseTypeName, EventTicket
from service.event_service import EventService
from tkinter import *
from view.command.events.add_event_command import AddEventCommand

from view.components.item_form import ItemForm
from view.utils.tkinter_utils import center_resize_window


class EventController():
    def __init__(self, service: EventService,view=None):
        self.view=view
        self.service = service

    def create_event_from_host(self, user_id: str, event: Event):
        self.service.create_event_from_host(user_id, event)
        self.view.refresh()

    def update_event_from_host(self, user_id: str, event: Event):
        self.service.update_event_from_host(user_id, event)

    def add_event_post(self, user_id: str, event_id: str, event_post: EventPost):
        self.service.add_event_post(user_id, event_id, event_post)

    def respond_event_invitation(self, event_id: str, text_response: str, response_date: datetime,
                                 invitation_response: InvitationResponseTypeName):
        self.service.respond_event_invitation(event_id, text_response, response_date, invitation_response)

    def send_event_invitation(self, event_id: str, event_invitation: EventInvitation):
        self.service.send_event_invitation(event_id, event_invitation)

    def take_ticket(self, event_id: str, event_ticket: EventTicket):
        self.service.take_ticket(event_id, event_ticket)

    def register_for_event(self, event_id: str, user_id: str, is_paid: bool):
        self.service.register_for_event(event_id, user_id, is_paid)

    def get_all_events(self):
        return self.service.find_all()

    def save_events(self):
        return self.service.save()

    def reload_events(self):
        return self.service.load()

    def show_add_book(self):
        form = ItemForm(self.view,
                        EventMeeting(name="", description="",
                                     creation_date=None,
                                     registration_end_date=None,
                                     start_datetime=None,
                                     end_datetime=None,
                                     place="",
                                     is_public=None,
                                     capacity=0,
                                     price=0,
                                     creation_user_id=None,  # TODO
                                     event_status=EventStatusName(EventStatusName.OPEN_FOR_REGISTRATIONS),
                                     registered_user_ids=[]),
                        AddEventCommand(self))
