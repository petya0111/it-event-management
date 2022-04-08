from tkinter import *
from tkinter import ttk

from controller.event_controller import EventController
from view.command.events.add_event_command import AddEventCommand
from view.command.events.delete_events_command import DeleteEventsCommand
from view.command.events.edit_event_command import ShowEditEventCommand
from view.command.events.list_events_command import ListEventsCommand
from view.command.events.show_add_event_command import ShowAddEventCommand
from view.command.exit_command import ExitCommand
from view.command.load_data_command import LoadDataCommand
from view.command.save_data_command import SaveDataCommand
from view.components.event_main_view import EventMainView
from view.utils.tkinter_utils import print_hierarchy


class MainView(ttk.Frame):
    def __init__(self, root, event_controller: EventController, user_id: str):
        super().__init__(root, padding="3 3 12 12")
        self.user_id = user_id
        self.root = root
        self.event_controller = event_controller

        # Set root
        self.root.title('IT events')
        self.grid(column=0, row=0, sticky="NWES")

        # Create menus
        self.menubar = Menu(root)
        root['menu'] = self.menubar
        # print(root.tk.call('tk', 'windowingsystem'))  # returns x11, win32 or aqua
        root.option_add('*tearOff', False)

        # File menu
        menu_file = Menu(self.menubar)
        self.menubar.add_cascade(menu=menu_file, label="File", underline=0)
        menu_file.add_command(label="Load Data", command=LoadDataCommand(event_controller))
        menu_file.add_command(label="Save Data", command=SaveDataCommand(event_controller))
        menu_file.add_separator()
        exit_command = ExitCommand(root)
        menu_file.add_command(label="Exit", command=exit_command, underline=1, accelerator='Ctrl-Shift-X')
        root.bind_all("<Control-Shift-KeyPress-X>", exit_command)

        # Create commands
        self.show_add_event_command = ShowAddEventCommand(event_controller, user_id)
        self.add_event_command = AddEventCommand(event_controller, user_id)
        self.show_edit_book_command = ShowEditEventCommand(event_controller)
        self.delete_books_command = DeleteEventsCommand(event_controller)
        self.list_books_command = ListEventsCommand(event_controller)

        # Books menu
        menu_books = Menu(self.menubar)
        self.menubar.add_cascade(menu=menu_books, label="Events", underline=0)
        menu_books.add_command(label="List Events", command=self.list_books_command)
        menu_books.add_separator()
        menu_books.add_command(label="Add Event", command=self.show_add_event_command)
        menu_books.add_command(label="Edit Event", command=self.show_edit_book_command)
        menu_books.add_command(label="Delete Events", command=self.delete_books_command)

        # Show items
        self.item_list = EventMainView(user_id, self.root, self.event_controller,
                                       self.show_add_event_command,
                                       self.show_edit_book_command,
                                       self.delete_books_command)

        print_hierarchy(root)

    def refresh(self):
        self.item_list.refresh()
