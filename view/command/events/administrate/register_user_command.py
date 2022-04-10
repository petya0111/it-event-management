from tkinter import Tk

from view.main_register_view import MainRegisterView


class RegisterUserCommand:

    def __init__(self, credentials_controller, user_id):
        self.credentials_controller = credentials_controller
        self.user_id = user_id

    def __call__(self):
        root = Tk()
        login_view = MainRegisterView(root, self.credentials_controller)
        self.view = login_view
        root.mainloop()

