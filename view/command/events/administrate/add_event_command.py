from entity.event_meeting import EventMeeting


class AddEventCommand:

    def __init__(self, event_controller, user_id):
        self.user_id = user_id
        self.event_controller = event_controller

    def __call__(self, event: EventMeeting):
        self.event_controller.create_event_from_host(self.user_id, event)

