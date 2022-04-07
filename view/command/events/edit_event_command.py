from controller.event_controller import EventController


class ShowEditEventCommand:
    def __init__(self, event_controller: EventController):
        self.event_controller = event_controller

    def __call__(self, *args, **kwargs):
        #TODO show add book dialog
        print("Showing 'Edit Book' dialog")