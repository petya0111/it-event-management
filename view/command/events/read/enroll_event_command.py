class EnrollEventCommand:
    def __init__(self, event_controller,user_id,event=None):
        self.event = event
        self.user_id = user_id
        self.event_controller = event_controller

    def __call__(self, event):
        self.event_controller.register_for_event(event.id,self.user_id)
