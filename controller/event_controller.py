from datetime import datetime, timedelta

from entity.event_meeting import EventMeeting, EventStatusName
from service.event_service import EventService
from service.user_service import UserService
from view.command.events.administrate.add_event_command import AddEventCommand
from view.command.events.administrate.show_edit_event_command import ShowEditEventCommand
from view.command.events.read.enroll_event_command import EnrollEventCommand
from view.components.administrate.item_edit_event_form import ItemEditEventForm

from view.components.administrate.item_form import ItemForm
from view.components.read.item_enroll_event_form import ItemEnrollEventForm


class EventController():
    def __init__(self, service: EventService, view=None):
        self.view = view
        self.service = service

    def find_by_id(self, event_id):
        return self.service.find_by_id(event_id)

    def create_event_from_host(self, user_id: str, event: EventMeeting):
        self.service.create_event_from_host(user_id, event)
        self.view.refresh()

    def is_event_from_same_host_id(self,event_id,host_id):
        return self.service.is_event_from_same_host_id(event_id,host_id)

    def update_event_from_host(self, user_id: str, event: EventMeeting):
        self.service.update_event_from_host(user_id, event)
        self.view.refresh()

    def register_for_event(self,event_id,user_id):
        self.service.register_for_event(event_id,user_id)
        self.view.refresh()

    def delete_event_by_id(self, event_id: list[str]):
        self.service.delete_by_id(event_id)
        self.view.refresh()

    # def add_event_post(self, user_id: str, event_id: str, event_post: EventPost):
    #     self.service.add_event_post(user_id, event_id, event_post)

    # def respond_event_invitation(self, event_id: str, text_response: str, response_date: datetime,
    #                              invitation_response: InvitationResponseTypeName):
    #     self.service.respond_event_invitation(event_id, text_response, response_date, invitation_response)
    #
    # def send_event_invitation(self, event_id: str, event_invitation: EventInvitation):
    #     self.service.send_event_invitation(event_id, event_invitation)

    # def take_ticket(self, event_id: str, event_ticket: EventTicket):
    #     self.service.take_ticket(event_id, event_ticket)


    def get_all_events(self):
        return self.service.find_all()

    def save_events(self):
        return self.service.save()

    def reload_events(self):
        return self.service.load()

    def show_add_event(self, user_id: str):
        now = datetime.now()
        two_hours_later = now + timedelta(hours=2)
        two_hours_day = two_hours_later.strftime("%Y-%m-%d")
        two_hours_time = two_hours_later.strftime("%H:%M:%S")
        day = now.strftime("%Y-%m-%d")
        time = now.strftime("%H:%M:%S")
        form = ItemForm(self.view, user_id,
                        EventMeeting(name="", description="",
                                     # creation_date=None,
                                     registration_end_date=datetime.fromisoformat(f"{two_hours_day} {two_hours_time}"),
                                     start_date=day,
                                     start_time=time,
                                     end_time=two_hours_time,
                                     end_date=two_hours_day,
                                     place="",
                                     is_public=None,
                                     capacity=0,
                                     price=0,
                                     creation_user_id=None,
                                     event_status=EventStatusName(EventStatusName.OPEN_FOR_REGISTRATIONS),
                                     registered_user_ids=[]),
                        AddEventCommand(self, user_id))

    def show_edit_event(self, event, user_id):
        form = ItemEditEventForm(self.view, user_id, item=event, command=ShowEditEventCommand(self, user_id, event))

    def show_enroll_event(self, event,can_enroll, user_id):
        enroll_btn = self.service.is_registered_event(event.id,user_id)
        form = ItemEnrollEventForm(self.view, user_id,enroll_btn,can_enroll, item=event, command=EnrollEventCommand(self, user_id=user_id,event= event))
