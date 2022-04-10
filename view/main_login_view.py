from functools import partial
from tkinter import *
from tkinter import ttk, messagebox

from controller.credentals_controller import CredentialsController
from controller.event_controller import EventController
from entity.user import RoleName
from exception.credentials_exception import CredentialsException
from view.main_guest_view import MainGuestView
from view.main_view import MainView


class MainLoginView(ttk.Frame):

    def __init__(self, win, credentials_controller: CredentialsController, event_controller: EventController):
        super().__init__(win)
        self.event_controller = event_controller
        self.root = win
        self.credentials_controller = credentials_controller

        # app title
        win.title("IT events App")

        # window size
        win.maxsize(width=500, height=500)
        win.minsize(width=500, height=500)

        # heading label
        heading = Label(win, text="Login", font='Verdana 25 bold')
        heading.place(x=80, y=150)

        username = Label(win, text="Email :", font='Verdana 10 bold')
        username.place(x=80, y=220)

        userpass = Label(win, text="Password :", font='Verdana 10 bold')
        userpass.place(x=80, y=260)

        # Entry Box
        user_name = StringVar()
        password = StringVar()

        userentry = Entry(win, width=40, textvariable=user_name)
        userentry.focus()
        userentry.place(x=200, y=223)

        passentry = Entry(win, width=40, show="*", textvariable=password)
        passentry.place(x=200, y=260)

        def validate_login():
            user = self.credentials_controller.login(user_name.get(), password.get())
            win.destroy()
            if user.role == RoleName.ADMIN.name or user.role == RoleName.HOST.name:
                event_root = Tk()
                event_controller.reload_events()
                main_view = MainView(event_root, event_controller,credentials_controller, credentials_controller.get_logged_user())
                event_controller.view = main_view
                event_root.mainloop()
            elif user.role == RoleName.ANONYMOUS_USER.name or user.role == RoleName.PARTICIPANT.name:
                event_root = Tk()
                event_controller.reload_events()
                main_view = MainGuestView(event_root, event_controller, credentials_controller)
                event_controller.view = main_view
                event_root.mainloop()

        def clear():
            userentry.delete(0, END)
            passentry.delete(0, END)

        def login():
            if user_name.get() == "" or password.get() == "":
                messagebox.showerror("Error", "Enter Email And Password", parent=win)
            else:
                try:
                    validate_login()
                except CredentialsException as es:
                    messagebox.showerror("Error", f"Login failed : {str(es.message)}", parent=win)
                except Exception as e:
                    messagebox.showerror("Error", f"Login failed : {str(e)}", parent=win)



        btn_login = Button(win, text="Login", font='Verdana 10 bold', command=partial(login))
        btn_login.place(x=200, y=293)

        btn_login = Button(win, text="Clear", font='Verdana 10 bold', command=partial(clear))
        btn_login.place(x=260, y=293)

