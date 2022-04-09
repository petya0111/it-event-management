class ShowAddEventCommand:
    def __init__(self, event_controller,user_id):
        self.user_id = user_id
        self.event_controller = event_controller

    def __call__(self, *args, **kwargs):
        self.event_controller.show_add_event(self.user_id)
