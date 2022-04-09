class ShowViewEnrollEventCommand:
    def __init__(self, event_controller,user_id,event=None):
        self.event = event
        self.user_id = user_id
        self.event_controller = event_controller

    def __call__(self, event):
        # self.event_controller.update_event_from_host(self.user_id, event)
