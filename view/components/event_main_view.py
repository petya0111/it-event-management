from tkinter import *
from tkinter import ttk

from view.command.events.delete_events_command import DeleteEventsCommand
from view.command.events.edit_event_command import ShowEditEventCommand
from view.command.events.show_add_event_command import ShowAddEventCommand
from view.components.item_list import ItemList
from view.utils.tkinter_utils import center_resize_window

from controller.event_controller import EventController

DEFAULT_COLUMN_WIDTH_PX = 140
SCROLLBAR_WIDTH_PX = 20
BUTTONS_PANEL_HEIGHT_PX = 100


class EventMainView(ttk.Frame):
    def __init__(self, parent, event_controller: EventController,
                 show_add_event_command: ShowAddEventCommand,
                 edit_event_command: ShowEditEventCommand, delete_events_command: DeleteEventsCommand):
        super().__init__(parent, padding="3 3 12 12")
        self.show_add_book_command = show_add_event_command
        self.edit_book_command = edit_event_command
        self.delete_books_command = delete_events_command
        self.event_controller = event_controller
        self.parent = parent
        self.grid(row=0, column=0, sticky='nsew')
        parent.rowconfigure(0, weight=1, minsize=300, pad=30)
        parent.columnconfigure(0, weight=1, minsize=300, pad=30)

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
        self.add_button = ttk.Button(buttons_frame, text="Add Event", padding=10,
                                     command=self.show_add_book_command)
        self.add_button.grid(column=1, row=0, sticky="NE", padx=40, pady=20)

        self.add_button = ttk.Button(buttons_frame, text="Edit Event", padding=10,
                                     command=self.edit_book_command)
        self.add_button.grid(column=2, row=0, sticky="NE", padx=40, pady=20)
        self.add_button = ttk.Button(buttons_frame, text="Delete Events", padding=10,
                                     command=self.delete_selected)
        self.add_button.grid(column=3, row=0, sticky="NE", padx=40, pady=20)

        rows, cols = buttons_frame.grid_size()
        for col in range(cols):
            buttons_frame.columnconfigure(col, minsize=300, pad=30)

    def delete_selected(self):
        items = self.item_list.get_selected_tems()
        ids = list(map(lambda item: item[0], items))
        print(ids)

    def refresh(self):
        books = self.event_controller.get_all_events()
        self.item_list.set_items(books)
