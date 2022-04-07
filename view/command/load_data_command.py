from controller.event_controller import EventController


class LoadDataCommand:
    def __init__(self, events_controller: EventController):
        self.book_controller = events_controller

    def __call__(self, *args, **kwargs):
        self.book_controller.reload_events()