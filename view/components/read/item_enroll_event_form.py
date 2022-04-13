from datetime import datetime
from tkinter import *
from tkinter import ttk
from view.utils.tkinter_utils import center_resize_window

DEFAULT_ENTRY_WIDTH_PX = 250


class ItemEnrollEventForm(Toplevel):
    def __init__(self, parent, user_id, enroll_btn: bool, can_enroll: bool, item, command, edit=False):
        super().__init__(parent)
        self.user_id = user_id
        self.parent = parent
        self.item = item
        self.command = command
        self.edit = edit

        self.frame = ttk.Frame(self, padding="20 20 20 20")
        self.title("View Event")
        self.frame.grid(row=0, column=0, sticky=NSEW)
        center_resize_window(self,width=600,height=450)

        self.models = []
        self.types = []
        self.entries = []

        self.columns = tuple(self.item.__dict__.keys())

        for i, col in enumerate(self.columns):
            # add view models
            attr = getattr(self.item, col)
            if isinstance(attr, int):
                self.types.append("int")
            elif isinstance(attr, float):
                self.types.append("float")
            elif isinstance(attr, (tuple, list)):
                self.types.append("list")
            else:
                self.types.append("str")
            model = StringVar()
            model.set(attr)
            self.models.append(model)

            # add labels
            ttk.Label(self.frame, text=col.title(), justify=LEFT).grid(column=0, row=i, sticky=EW)

            # add entries
            entry = ttk.Label(self.frame, text=model.get())
            entry.grid(column=1, row=i, sticky=EW)
            if col == 'id':
                entry.configure(state=DISABLED)
            if col == 'registration_end_date':
                self.reg_end_date = model.get()

            self.entries.append(entry)

        # make form resizable
        rows, cols = self.frame.grid_size()
        for row in range(rows):
            self.frame.rowconfigure(row, weight=1)
        self.frame.columnconfigure(0, weight=1, minsize=DEFAULT_ENTRY_WIDTH_PX)
        self.frame.columnconfigure(1, weight=1, minsize=DEFAULT_ENTRY_WIDTH_PX)

        if can_enroll:
            # add buttons
            buttons_frame = ttk.Frame(self.frame, padding="20 10 20 10")
            buttons_frame.grid(column=0, row=len(self.columns), columnspan=2, sticky=NSEW)
            if enroll_btn:
                self.add_button = ttk.Button(buttons_frame, text="You are going to this event", padding=10,
                                             state=DISABLED)
            else:
                self.add_button = ttk.Button(buttons_frame, text="Enroll", padding=10, command=self.submit)
            if datetime.fromisoformat(self.reg_end_date) < datetime.now():
                self.add_button = ttk.Button(buttons_frame, text="Expired event", padding=10,
                                             state=DISABLED)
            self.add_button.grid(column=1, row=0, sticky=NE, padx=40, pady=20)

            rows, cols = buttons_frame.grid_size()
            for col in range(cols):
                buttons_frame.columnconfigure(col, minsize=100, pad=30)

        # modal - capture visibility
        self.protocol("WM_DELETE_WINDOW", self.dismiss)
        self.transient(self.parent)
        self.wait_visibility()
        self.grab_set()
        self.wait_window()

    def submit(self):
        cls = type(self.item)
        result = cls()
        for i, col in enumerate(self.columns):
            str_val = self.models[i].get()
            if self.types[i] == "int":
                value = int(str_val)
            elif self.types[i] == "float":
                value = float(str_val)
            elif self.types[i] == "str":
                value = str_val
            elif self.types[i] == "list":
                value = [s.strip() for s in str_val.split(',')]
            setattr(result, col, value)
        print(self.command, result)
        self.dismiss()
        self.command(result)

    def dismiss(self):
        self.grab_release()
        self.destroy()
