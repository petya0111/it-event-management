from tkinter import *
from tkinter import ttk

from controller.credentals_controller import CredentialsController
from controller.event_controller import EventController
from entity.user import RoleName
from view.command.events.list_events_command import ListEventsCommand
from view.command.events.read.select_item_view_event_command import SelectItemViewEventCommand
from view.command.exit_command import ExitCommand
from view.command.load_data_command import LoadDataCommand
from view.command.save_data_command import SaveDataCommand
from view.components.read.event_main_guest_view import EventMainGuestView
from view.utils.tkinter_utils import print_hierarchy


class MainGuestView(ttk.Frame):
    def __init__(self, root, event_controller: EventController, credentials_controller: CredentialsController):
        super().__init__(root, padding="3 3 12 12")
        self.credentials_controller = credentials_controller
        self.user_id = credentials_controller.get_logged_user()
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

        self.view_event_command = SelectItemViewEventCommand(event_controller,
                                                             credentials_controller.get_role(credentials_controller.get_logged_user()) != RoleName.ANONYMOUS_USER.name,
                                                             self.user_id)
        self.list_events_command = ListEventsCommand(event_controller)

        # Books menu
        menu_books = Menu(self.menubar)
        self.menubar.add_cascade(menu=menu_books, label="Events", underline=0)
        menu_books.add_command(label="List Events", command=self.list_events_command)
        menu_books.add_separator()

        # Show items
        self.item_list = EventMainGuestView(self.user_id, self.root, self.event_controller,
                                            self.view_event_command)

        print_hierarchy(root)

    def refresh(self):
        self.item_list.refresh()
