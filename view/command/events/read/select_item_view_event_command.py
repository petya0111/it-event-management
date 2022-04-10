class SelectItemViewEventCommand:

    def __init__(self, event_controller=None, can_enroll=False, user_id=None, event_id=None,):
        self.can_enroll = can_enroll
        self.event_id = event_id
        self.user_id = user_id
        self.event_controller = event_controller

    def __call__(self, event_id=None):
        event = self.event_controller.find_by_id(event_id)
        self.event_controller.show_enroll_event(event,self.can_enroll, self.user_id)
