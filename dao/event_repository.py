from dao.json_repository import JsonRepository
from entity.event_meeting import EventMeeting


class EventRepository(JsonRepository):
    def __init__(self, id_generator, file_name):
        super().__init__(id_generator, file_name)

    def is_registered_event(self, event_id, user_id):
        event: EventMeeting = self.find_by_id(event_id)
        if event.registered_user_ids == 0:
            return False
        if user_id in event.registered_user_ids:
            return True
        else:
            return False

    def is_event_from_same_host_id(self, event_id, host_id):
        event: EventMeeting = self.find_by_id(event_id)
        if host_id == event.creation_user_id:
            return True
        return False