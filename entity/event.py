from datetime import datetime
from enum import Enum

from entity.user import User


class EventPost:
    def __init__(self, event_id: str, text: str, creation_date: datetime, creation_user: User):
        self._event_id = event_id
        self._text = text
        self._creation_date = creation_date
        self._creation_user = creation_user

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
    def creation_user(self):
        return self._creation_user

    @creation_user.setter
    def creation_user(self, creation_user):
        self._creation_user = creation_user

    @classmethod
    def from_json(cls, prop_dict):
        return cls[prop_dict['id'],
                   prop_dict['event_id'],
                   prop_dict['text'],
                   prop_dict['creation_date'],
                   prop_dict['creation_user']
        ]

    def to_json(self):
        return {
            'event_id': self.event_id,
            "text": self.text,
            "creation_date": str(self.creation_date),
            "creation_user": str(self.creation_user),
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
                 event_id: str,
                 user_id: str,
                 sent_date: datetime,
                 text_response: str = None,
                 response_date: datetime = None,
                 invitation_response: InvitationResponseTypeName = None):
        self._event_id = event_id
        self._user_id = user_id
        self._sent_date = sent_date
        self._invitation_response = invitation_response
        self._text_response = text_response
        self._response_date = response_date

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

    @classmethod
    def from_json(cls, prop_dict):
        return cls[prop_dict['event_id'],
                   prop_dict['user_id'],
                   prop_dict['sent_date'],
                   prop_dict['invitation_response'],
                   prop_dict['text_response'],
                   prop_dict['response_date']
        ]

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
    def __init__(self, event_id: str, text: str, paid_date: datetime, is_paid: bool = False, owner_ids=None):
        if owner_ids is None:
            owner_ids = []
        self._event_id = event_id
        self._text = text
        self._owner_ids = owner_ids
        self._is_paid = is_paid
        self._paid_date = paid_date

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


    @classmethod
    def from_json(cls, prop_dict):
        return cls[prop_dict['event_id'],
                   prop_dict['text'],
                   prop_dict['owner_ids'],
                   prop_dict['paid_date'],
                   prop_dict['is_paid']
        ]

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
                 event_status: EventStatusName,
                 registered_user_ids: list[str],
                 event_post: EventPost = None,
                 event_ticket: EventTicket = None,
                 event_invitation: EventInvitation = None,
                 creation_user_id: str = None,
                 id=None):
        self._id = id
        self._name = name
        self._description = description
        self._creation_date = creation_date
        self._creation_user_id = creation_user_id
        self._registration_end_date = registration_end_date
        self._start_datetime = start_datetime
        self._end_datetime = end_datetime
        self._place = place
        self._is_public = is_public
        self._capacity = capacity
        self._price = price
        self._status_name = event_status.name
        self._registered_user_ids = registered_user_ids
        self._event_post = event_post
        self._event_ticket = event_ticket
        self._event_invitation = event_invitation

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

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
    def creation_user_id(self, creation_user_id):
        self._creation_user_id = creation_user_id

    @property
    def registration_end_date(self):
        return str(self._registration_end_date)

    @registration_end_date.setter
    def registration_end_date(self, registration_end_date):
        self._registration_end_date = registration_end_date

    @property
    def start_datetime(self):
        return str(self._start_datetime)

    @start_datetime.setter
    def start_datetime(self, start_datetime):
        self._start_datetime = start_datetime

    @property
    def end_datetime(self):
        return str(self._end_datetime)

    @end_datetime.setter
    def end_datetime(self, end_datetime):
        self._end_datetime = end_datetime

    @property
    def place(self):
        return self._place

    @place.setter
    def place(self, place):
        self._place = place

    @property
    def is_public(self):
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        self._is_public = is_public

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def status_name(self):
        return self._status_name

    @status_name.setter
    def status_name(self, status_name):
        self._status_name = status_name

    @property
    def registered_user_ids(self):
        return self._registered_user_ids

    @registered_user_ids.setter
    def registered_user_ids(self, registered_user_ids):
        self._registered_user_ids = registered_user_ids

    @property
    def event_post(self):
        return self._event_post

    @event_post.setter
    def event_post(self, event_post):
        self._event_post = event_post

    @property
    def event_ticket(self):
        return self._event_ticket

    @event_ticket.setter
    def event_ticket(self, event_ticket):
        self._event_ticket = event_ticket

    @property
    def event_invitation(self):
        return self._event_invitation

    @event_invitation.setter
    def event_invitation(self, event_invitation):
        self._event_invitation = event_invitation

    @classmethod
    def from_json(cls, prop_dict):
        return cls[prop_dict['id'],
                   prop_dict['name'],
                   prop_dict['description'],
                   prop_dict['creation_date'],
                   prop_dict['registration_end_date'],
                   prop_dict['start_datetime'],
                   prop_dict['end_datetime'],
                   prop_dict['place'],
                   prop_dict['is_public'],
                   prop_dict['capacity'],
                   prop_dict['price'],
                   prop_dict['creation_user_id'],
                   prop_dict['event_status'],
                   prop_dict['registered_user_ids'],
                   prop_dict['event_post'],
                   prop_dict['event_ticket'],
                   prop_dict['event_invitation']
        ]

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            "description": self.description,
            "creation_date": self.creation_date,
            "registration_end_date": self.registration_end_date,
            "start_datetime": self.start_datetime,
            "end_datetime": self.end_datetime,
            "place": self.place,
            "is_public": self.is_public,
            "capacity": self.capacity,
            "price": self.price,
            "creation_user_id": self.creation_user_id,
            "event_status": self.status_name,
            "registered_user_ids": self.registered_user_ids,
            "event_post": self.event_post,
            "event_ticket": self.event_ticket,
            "event_invitation": self.event_invitation,
            '_module': self.__class__.__module__,
            '_class': self.__class__.__name__
        }

    def get_formatted_str(self):
        return f'| {self.id:24s} | {self.name:30.30s} | {self.description:40.40s} |  {str(self.creation_date):20.20s} | {str(self.place):15.15s} |'
