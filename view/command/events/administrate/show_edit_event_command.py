from tkinter import messagebox

from exception.time_pattern_exception import TimePatternExcetion


class ShowEditEventCommand:
    def __init__(self, event_controller,user_id,event=None):
        self.event = event
        self.user_id = user_id
        self.event_controller = event_controller

    def __call__(self, event,tk_parent):
        # try:
        self.event_controller.update_event_from_host(self.user_id, event)
        # except TimePatternExcetion as t:
        #     messagebox.showerror("Error", f"Error : {str(t.message)}", parent=tk_parent)
        # except Exception as e:
        #     messagebox.showerror("Error", f"Error : {str(e)}", parent=tk_parent)