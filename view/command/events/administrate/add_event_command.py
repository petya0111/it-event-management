from tkinter import messagebox

from entity.event_meeting import EventMeeting
from exception.time_pattern_exception import TimePatternExcetion


class AddEventCommand:

    def __init__(self, event_controller, user_id):
        self.user_id = user_id
        self.event_controller = event_controller

    def __call__(self, event: EventMeeting,tk_parent):
        try:
            self.event_controller.create_event_from_host(self.user_id, event)
        except TimePatternExcetion as t:
            messagebox.showerror("Error", f"Error : {str(t.message)}", parent=tk_parent)
        except Exception as e:
            messagebox.showerror("Error", f"Error : {str(e)}", parent=tk_parent)

