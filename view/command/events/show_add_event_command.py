
class ShowAddEventCommand:
    def __init__(self, event_controller):
        self.event_controller = event_controller

    def __call__(self, *args, **kwargs):
        self.event_controller.show_add_book()
