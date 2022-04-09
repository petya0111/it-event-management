from controller.event_controller import EventController


class DeleteEventsCommand:
    def __init__(self, event_controller: EventController):
        self.event_controller = event_controller

    def __call__(self,  event_id: list[str]=None):
        self.event_controller.delete_event_by_id(event_id)
