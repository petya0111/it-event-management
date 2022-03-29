from datetime import datetime
from enum import Enum

from entity.user import User


class EventStatusName(Enum):
    DRAFT = "Draft",
    OPEN_FOR_REGISTRATIONS = "Open for registrations",
    CLOSED_TO_REGISTRATIONS = "Closed to registrations"
    ONGOING = "Ongoing"
    PAST = "Past"
    CANCELLED = "Cancelled"


class EventStatus:
    def __init__(self, event_status_name: EventStatusName, id=None):
        self.id = id
        self.name = event_status_name


class Event:

    def __init__(self,
                 name: str,
                 description: str,
                 creation_date: datetime,
                 registration_end_date: datetime,
                 start_datetime: datetime,
                 end_datetime: datetime,
                 place: str,
                 is_public: bool,
                 capacity: int,
                 price: float,
                 creation_user_id: str,
                 event_status: EventStatus,
                 registered_user_ids: list[str],
                 id=None):
        self.id = id
        self.name = name
        self.description = description
        self.creation_date = creation_date
        self.creation_user_id = creation_user_id
        self.registration_end_date = registration_end_date
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.place = place
        self.is_public = is_public
        self.capacity = capacity
        self.price = price
        self.status_name = event_status.name
        self.registered_user_ids = registered_user_ids

    def get_formatted_str(self):
        return f'| {str(self.id):24s} | {self.name:30.30s} | {self.description:40.40s} |  {str(self.creation_date.astimezone()):20.20s} | {str(self.place):15.15s} |'


class InvitationResponseTypeName(Enum):
    ACCEPT = "Accept",
    REJECT = "Reject",
    MAYBE = "Maybe"


class InvitationResponseType:
    def __init__(self, event_status_name: InvitationResponseTypeName, id=None):
        self.id = id
        self.name = event_status_name


class EventInvitation:
    def __init__(self,
                 event: Event,
                 user: User,
                 sent_date: datetime,
                 invitation_response: InvitationResponseType,
                 text_response: str,
                 response_date: datetime,
                 id=None):
        self.id = id
        self.event_id = event.id
        self.user_id = user.id
        self.sent_date = sent_date
        self.invitation_response_id = invitation_response.id
        self.text_response = text_response
        self.response_date = response_date


class EventTicket:
    def __init__(self, event: Event, text: str, owner: User, is_paid: bool, paid_date: datetime, id=None):
        self.id = id
        self.event_id = event.id
        self.text = text
        self.owner_id = owner.id
        self.is_paid = is_paid
        self.paid_date = paid_date


class EventPost:
    def __init__(self, event: Event, text: str, creation_date: datetime, creation_user: User, id=None):
        self.id = id
        self.event = event
        self.text = text
        self.creation_date = creation_date
        self.creation_user = creation_user
