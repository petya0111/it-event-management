from datetime import datetime
from enum import Enum


class EventPost:
    def __init__(self, event_id: str = None, text: str = None, creation_date: datetime = None,
                 creation_user_id: str = None):
        self._event_id = event_id
        self._text = text
        self._creation_date = str(creation_date)
        self._creation_user_id = creation_user_id

    @property
    def event_id(self):
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        self._event_id = event_id

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text

    @property
    def creation_date(self):
        return str(self._creation_date)

    @creation_date.setter
    def creation_date(self, creation_date):
        self._creation_date = creation_date

    @property
    def creation_user_id(self):
        return self._creation_user_id

    @creation_user_id.setter
    def creation_user_id(self, creation_user):
        self._creation_user_id = creation_user

    def to_json(self):
        return {
            'event_id': self.event_id,
            "text": self.text,
            "creation_date": str(self.creation_date),
            "creation_user_id": self.creation_user_id,
            '_module': self.__class__.__module__,
            '_class': self.__class__.__name__
        }


class InvitationResponseTypeName(Enum):
    ACCEPT = 1,
    REJECT = 2,
    MAYBE = 3

    @classmethod
    def from_json(cls, prop_dict):
        return cls[prop_dict['name']]

    def to_json(self):
        return {
            'name': self.name,
            '_module': self.__class__.__module__,
            '_class': self.__class__.__name__
        }


class EventInvitation:
    def __init__(self,
                 event_id: str = None,
                 user_id: str = None,
                 sent_date: datetime = None,
                 text_response: str = None,
                 response_date: datetime = None,
                 invitation_response: InvitationResponseTypeName = None):
        self._event_id = event_id
        self._user_id = user_id
        self._sent_date = str(sent_date)
        self._invitation_response = invitation_response
        self._text_response = text_response
        self._response_date = str(response_date)

    @property
    def event_id(self):
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        self._event_id = event_id

    @property
    def user_id(self):
        return str(self._user_id)

    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id

    @property
    def sent_date(self):
        return str(self._sent_date)

    @sent_date.setter
    def sent_date(self, sent_date):
        self._sent_date = sent_date

    @property
    def invitation_response(self):
        return self._invitation_response

    @invitation_response.setter
    def invitation_response(self, invitation_response):
        self._invitation_response = invitation_response

    @property
    def text_response(self):
        return self._text_response

    @text_response.setter
    def text_response(self, text_response):
        self._text_response = text_response

    @property
    def response_date(self):
        return str(self._response_date)

    @response_date.setter
    def response_date(self, response_date):
        self._response_date = response_date

    def to_json(self):
        return {
            'event_id': self.event_id,
            'user_id': self.user_id,
            "sent_date": str(self.sent_date),
            "invitation_response": self.invitation_response,
            "text_response": self.text_response,
            "response_date": str(self.response_date),
            '_module': self.__class__.__module__,
            '_class': self.__class__.__name__
        }


class EventTicket:
    def __init__(self, event_id: str = None, text: str = None, paid_date: datetime = None, is_paid: bool = False,
                 owner_ids=None):
        if owner_ids is None:
            owner_ids = []
        self._event_id = event_id
        self._text = text
        self._owner_ids = owner_ids
        self._is_paid = is_paid
        self._paid_date = str(paid_date)

    @property
    def event_id(self):
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        self._event_id = event_id

    @property
    def text(self):
        return str(self._text)

    @text.setter
    def text(self, text):
        self._text = text

    @property
    def owner_ids(self):
        return self._owner_ids

    @owner_ids.setter
    def owner_ids(self, owner_ids):
        self._owner_ids = owner_ids

    @property
    def paid_date(self):
        return str(self._paid_date)

    @paid_date.setter
    def paid_date(self, paid_date):
        self._paid_date = paid_date

    @property
    def is_paid(self):
        return self._is_paid

    @is_paid.setter
    def is_paid(self, is_paid):
        self._is_paid = is_paid

    def to_json(self):
        return {
            'event_id': self.event_id,
            'owner_ids': self.owner_ids,
            "text": self.text,
            "paid_date": str(self.paid_date),
            "is_paid": self.is_paid,
            '_module': self.__class__.__module__,
            '_class': self.__class__.__name__
        }


class EventStatusName(Enum):
    DRAFT = 1,
    OPEN_FOR_REGISTRATIONS = 2,
    CLOSED_TO_REGISTRATIONS = 3,
    ONGOING = 4.
    PAST = 5,
    CANCELLED = 6

    @classmethod
    def from_json(cls, prop_dict):
        return cls[prop_dict['name']]

    def to_json(self):
        return {
            'name': self.name,
            '_module': self.__class__.__module__,
            '_class': self.__class__.__name__
        }


class EventMeeting:

    def __init__(self,
                 name: str = None,
                 description: str = None,
                 creation_user_id: str = None,
                 start_date: str = None,
                 start_time: str = None,
                 end_date: str = None,
                 end_time: str = None,
                 registration_end_date: datetime = None,
                 place: str = None,
                 is_public: bool = None,
                 capacity: int = None,
                 price: float = None,
                 event_status: EventStatusName = EventStatusName.DRAFT,
                 registered_user_ids: list[str]=[],
                 # event_post: EventPost = None,
                 # event_ticket: EventTicket = None,
                 # event_invitation: EventInvitation = None,
                 id=None):
        self.id = id
        self.name = name
        self.description = description
        self.creation_user_id = creation_user_id
        self.start_date = start_date
        self.start_time = start_time
        self.end_date = end_date
        self.end_time = end_time
        self.registration_end_date = registration_end_date
        self.place = place
        self.is_public = is_public
        self.capacity = capacity
        self.price = price
        self.status_name = event_status
        self.registered_user_ids = registered_user_ids
        # self.event_post = event_post
        # self.event_ticket = event_ticket
        # self.event_invitation = event_invitation

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            "description": self.description,
            "creation_user_id": self.creation_user_id,
            "start_date": self.start_date,
            "start_time": self.start_time,
            "end_date": self.end_date,
            "end_time": self.end_time,
            "registration_end_date": str(self.registration_end_date),
            "place": self.place,
            "is_public": self.is_public,
            "capacity": self.capacity,
            "price": self.price,
            "event_status": self.status_name.name,
            "registered_user_ids": self.registered_user_ids,
            # "event_post": self.event_post,
            # "event_ticket": self.event_ticket,
            # "event_invitation": self.event_invitation,
            '_module': self.__class__.__module__,
            '_class': self.__class__.__name__
        }

    def get_formatted_str(self):
        return f'| {self.id:24s} | {self.name:30.30s} | {self.description:40.40s} |  {str(self.start_date):20.20s} | {str(self.place):15.15s} |'
