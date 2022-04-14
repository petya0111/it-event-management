from tkinter import ttk

from view.command.events.read.select_item_view_event_command import SelectItemViewEventCommand
from view.components.item_list import ItemList
from view.utils.tkinter_utils import center_resize_window

from controller.event_controller import EventController

DEFAULT_COLUMN_WIDTH_PX = 140
SCROLLBAR_WIDTH_PX = 20
BUTTONS_PANEL_HEIGHT_PX = 100


class EventMainGuestView(ttk.Frame):
    def __init__(self, user_id, parent, event_controller: EventController,
                 select_item_vew_event_command: SelectItemViewEventCommand):
        super().__init__(parent, padding="3 3 12 12")
        self.user_id = user_id
        self.select_item_vew_event_command = select_item_vew_event_command
        self.event_controller = event_controller
        self.parent = parent
        self.grid(row=0, column=0, sticky='nsew')
        parent.rowconfigure(0, weight=1, minsize=300, pad=40)
        parent.columnconfigure(0, weight=1, minsize=300, pad=40)

        items = event_controller.get_all_events()
        self.item_list = ItemList(self, items)
        self.grid(column=0, row=0, sticky="nsew")

        # resize the parent window to show treeview widget
        self.item_list.update_idletasks()
        print(self.item_list.winfo_width(), self.item_list.winfo_height())
        center_resize_window(parent,
                             self.item_list.winfo_width(),
                             self.item_list.winfo_height() + BUTTONS_PANEL_HEIGHT_PX)

        # add buttons
        buttons_frame = ttk.Frame(self, padding="20 10 20 10")
        buttons_frame.grid(column=0, row=1, sticky="nsew")

        self.add_button = ttk.Button(buttons_frame, text="View Event", padding=10,
                                     command=self.view_selected)
        self.add_button.grid(column=2, row=0, sticky="NE", padx=40, pady=20)

        rows, cols = buttons_frame.grid_size()
        for col in range(cols):
            buttons_frame.columnconfigure(col, minsize=300, pad=30)

    def view_selected(self):
        items = self.item_list.get_selected_tems()
        ids = list(map(lambda item: item[0], items))
        if len(ids) > 0:
            id_str = ids[0]
            print("edit ids", id_str)
            return self.select_item_vew_event_command(id_str)

    def refresh(self):
        events = self.event_controller.get_all_events()
        if len(events) != 0:
            self.item_list.set_items(events)
        else:
            self.item_list.set_items([])
