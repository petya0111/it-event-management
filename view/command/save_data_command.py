from controller.event_controller import EventController


class SaveDataCommand:
    def __init__(self, event_controller: EventController):
        self.book_controller = event_controller

    def __call__(self, *args, **kwargs):
        self.book_controller.save_events()