from functools import partial
from tkinter import *
from tkinter import ttk

from controller.credentals_controller import CredentialsController
from controller.event_controller import EventController
from view.command.events.administrate.add_event_command import AddEventCommand
from view.command.events.administrate.delete_events_command import DeleteEventsCommand
from view.command.events.administrate.register_user_command import RegisterUserCommand
from view.command.events.administrate.select_item_edit_event_command import SelectItemEditEventCommand
from view.command.events.list_events_command import ListEventsCommand
from view.command.events.administrate.show_add_event_command import ShowAddEventCommand
from view.command.events.read.select_item_view_event_command import SelectItemViewEventCommand
from view.command.exit_command import ExitCommand
from view.command.load_data_command import LoadDataCommand
from view.command.save_data_command import SaveDataCommand
from view.components.administrate.event_main_view import EventMainView

from view.utils.tkinter_utils import print_hierarchy, center_resize_window


class MainEventsHomeView(ttk.Frame):
    def __init__(self, root, event_controller: EventController, credentials_controller: CredentialsController,
                 user_id: str):
        super().__init__(root, padding="3 3 12 12")
        self.credentials_controller = credentials_controller
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
        # menu_file.add_command(label="Logout", command=partial(self.logout))
        root.bind_all("<Control-Shift-KeyPress-X>", exit_command)

        # Create commands
        self.show_add_event_command = ShowAddEventCommand(event_controller, user_id)
        self.add_event_command = AddEventCommand(event_controller, user_id)
        self.edit_event_command = SelectItemEditEventCommand(event_controller, user_id)
        self.delete_events_command = DeleteEventsCommand(event_controller)
        self.list_events_command = ListEventsCommand(event_controller)
        self.view_event_command = SelectItemViewEventCommand(event_controller, True, user_id)

        menu_events = Menu(self.menubar)
        self.menubar.add_cascade(menu=menu_events, label="Events", underline=0)
        menu_events.add_command(label="List Events", command=self.list_events_command)
        menu_events.add_separator()
        menu_events.add_command(label="Add Event", command=self.show_add_event_command)
        menu_events.add_command(label="Edit Event", command=self.edit_event_command)
        menu_events.add_command(label="Delete Event", command=self.delete_events_command)

        is_admin: bool = self.credentials_controller.get_role(user_id) == "ADMIN"
        if is_admin:
            self.register_user_command = RegisterUserCommand(credentials_controller, user_id)
            menu_events.add_command(label="Register User", command=self.register_user_command)
        # Show items
        self.item_list = EventMainView(user_id, is_admin, self.root, self.event_controller,
                                       self.show_add_event_command,
                                       self.edit_event_command,
                                       self.delete_events_command, self.register_user_command,
                                       self.view_event_command)

        print_hierarchy(root)

    # def logout(self):
    #     self.root.destroy()
    #     self.root = Tk()
    #     center_resize_window(self.root, 800, 400)
    #     self.root.columnconfigure(0, weight=1)
    #     self.root.rowconfigure(0, weight=1)
    #
    #     login_view = MainLoginHomeView(self.root, self.credentials_controller, self.event_controller)
    #     self.credentials_controller.view = login_view
    #     self.root.mainloop()

    def refresh(self):
        self.item_list.refresh()
