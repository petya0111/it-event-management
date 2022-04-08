from controller.event_controller import EventController


class ListEventsCommand:
    def __init__(self, event_controller: EventController):
        self.event_controller = event_controller

    def __call__(self, *args, **kwargs):
        print("Listing all events")
