from functools import partial
from tkinter import ttk
from tkinter import *

from controller.credentals_controller import CredentialsController
from controller.event_controller import EventController
from entity.user import RoleName
from view.main_guest_view import MainGuestView
from view.main_view import MainView


class MainCredentialsView(ttk.Frame):

    def __init__(self, root, credentials_controller: CredentialsController, event_controller: EventController):
        super().__init__(root, padding="3 3 12 12")
        self.event_controller = event_controller
        self.root = root
        self.credentials_controller = credentials_controller

        root.geometry('400x150')
        root.title('Login Form')

        # username label and text entry box
        username_label = Label(root, text="User Name").grid(row=0, column=0)
        username = StringVar()
        username_entry = Entry(root, textvariable=username).grid(row=0, column=1)

        # password label and password entry box
        password_label = Label(root, text="Password").grid(row=1, column=0)
        password = StringVar()
        password_entry = Entry(root, textvariable=password, show='*').grid(row=1, column=1)

        def validate_login(username, password):
            user = self.credentials_controller.login(username.get(), password.get())
            root.destroy()
            if user.role == RoleName.ADMIN.name or user.role == RoleName.HOST.name:
                event_root = Tk()
                event_controller.reload_events()
                main_view = MainView(event_root, event_controller, credentials_controller.get_logged_user())
                event_controller.view = main_view
                event_root.mainloop()
            elif user.role == RoleName.PARTICIPANT.name or user.role == RoleName.ANONYMUS_USER.name:
                event_root = Tk()
                event_controller.reload_events()
                main_view = MainGuestView(event_root, event_controller, credentials_controller.get_logged_user())
                event_controller.view = main_view
                event_root.mainloop()

        validate_login_command = partial(validate_login, username, password)

        # login button
        login_button = Button(root, text="Login", command=validate_login_command).grid(row=4, column=0)
