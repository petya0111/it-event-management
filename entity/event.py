from datetime import datetime
from enum import Enum

from entity.user import User


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
                   prop_dict['registered_user_ids']
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
            '_module': self.__class__.__module__,
            '_class': self.__class__.__name__
        }

    def get_formatted_str(self):
        return f'| {self.id:24s} | {self.name:30.30s} | {self.description:40.40s} |  {str(self.creation_date):20.20s} | {str(self.place):15.15s} |'


class InvitationResponseTypeName(Enum):
    ACCEPT = 1,
    REJECT = 2,
    MAYBE = 3


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
