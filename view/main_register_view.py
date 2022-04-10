from functools import partial
from tkinter import *
from tkinter import ttk, messagebox

from controller.credentals_controller import CredentialsController
from entity.user import RoleName, User
from exception.email_alredy_registered_exception import EmailAlreadyRegisteredExcetion


class MainRegisterView(ttk.Frame):

    def __init__(self, winsignup, credentials_controller: CredentialsController):
        super().__init__(winsignup)
        self.winsignup = winsignup
        self.credentials_controller = credentials_controller

        winsignup.title("IT events App")
        winsignup.maxsize(width=500, height=600)
        winsignup.minsize(width=500, height=600)

        # heading label
        heading = Label(winsignup, text="Signup", font='Verdana 20 bold')
        heading.place(x=80, y=60)

        # form data label
        first_name = Label(winsignup, text="First Name :", font='Verdana 10 bold')
        first_name.place(x=80, y=130)

        last_name = Label(winsignup, text="Last Name :", font='Verdana 10 bold')
        last_name.place(x=80, y=160)

        bio = Label(winsignup, text="Bio :", font='Verdana 10 bold')
        bio.place(x=80, y=190)

        role = Label(winsignup, text="Role :", font='Verdana 10 bold')
        role.place(x=80, y=220)

        email = Label(winsignup, text="Email :", font='Verdana 10 bold')
        email.place(x=80, y=303)

        password = Label(winsignup, text="Password :", font='Verdana 10 bold')
        password.place(x=80, y=333)

        very_pass = Label(winsignup, text="Verify Password:", font='Verdana 10 bold')
        very_pass.place(x=80, y=363)

        # Entry Box ------------------------------------------------------------------

        first_name = StringVar()
        last_name = StringVar()
        bio = StringVar()
        var = StringVar()
        email_var = StringVar()
        password = StringVar()
        very_pass = StringVar()
        roleType = IntVar()
        self.selected_role = RoleName.ANONYMOUS_USER.name

        first_name = Entry(winsignup, width=40, textvariable=first_name)
        first_name.place(x=210, y=133)

        last_name = Entry(winsignup, width=40, textvariable=last_name)
        last_name.place(x=210, y=163)

        bio = Entry(winsignup, width=40, textvariable=bio)
        bio.place(x=210, y=193)

        def role_chosen(value):
            self.selected_role = value

        self.rb1 = Radiobutton(winsignup, text='ADMIN', variable=roleType, value=0,
                               command=lambda: role_chosen("ADMIN"))
        self.rb2 = Radiobutton(winsignup, text='HOST', variable=roleType, value=1, command=lambda: role_chosen("HOST"))
        self.rb3 = Radiobutton(winsignup, text='PARTICIPANT', variable=roleType, value=2,
                               command=lambda: role_chosen("PARTICIPANT"))
        self.rb4 = Radiobutton(winsignup, text='ANONYMOUS_USER', variable=roleType, value=3,
                               command=lambda: role_chosen(RoleName.ANONYMOUS_USER.name))
        self.rb1.place(x=200, y=220)
        self.rb2.place(x=200, y=238)
        self.rb3.place(x=200, y=256)
        self.rb4.place(x=200, y=276)
        self.rb4.invoke()

        user_name = Entry(winsignup, width=40, textvariable=email_var)
        user_name.place(x=210, y=303)

        password = Entry(winsignup, width=40, textvariable=password)
        password.place(x=210, y=333)

        very_pass = Entry(winsignup, width=40, show="*", textvariable=very_pass)
        very_pass.place(x=210, y=363)

        def action():
            if first_name.get() == "" or last_name.get() == "" or bio.get() == "" or user_name.get() == "" or password.get() == "" or very_pass.get() == "":
                messagebox.showerror("Error", "All Fields Are Required", parent=winsignup)
            elif password.get() != very_pass.get():
                messagebox.showerror("Error", "Password & Confirm Password Should Be Same", parent=winsignup)
            else:
                try:
                    credentials_controller.register(User(first_name=first_name.get(), last_name=last_name.get(),
                                                         email=user_name.get(), password=password.get(), bio=bio.get(),
                                                         role=RoleName[self.selected_role]))
                    messagebox.showinfo("Success", "Registration Successful", parent=winsignup)
                    credentials_controller.reload_users()
                    clear()
                    switch()
                except EmailAlreadyRegisteredExcetion as email_ex:
                    messagebox.showerror("Error", f"Error : {str(email_ex.message)}", parent=winsignup)
                except Exception as es:
                    messagebox.showerror("Error", f"Error : {str(es)}", parent=winsignup)

        def switch():
            winsignup.destroy()

        def clear():
            first_name.delete(0, END)
            last_name.delete(0, END)
            bio.delete(0, END)
            var.set("ANONYMUS")
            user_name.delete(0, END)
            password.delete(0, END)
            very_pass.delete(0, END)

        btn_signup = Button(winsignup, text="Signup", font='Verdana 10 bold', command=partial(action))
        btn_signup.place(x=200, y=413)

        btn_login = Button(winsignup, text="Clear", font='Verdana 10 bold', command=partial(clear))
        btn_login.place(x=280, y=413)

        sign_up_btn = Button(winsignup, text="Close", command=partial(switch))
        sign_up_btn.place(x=350, y=20)

        winsignup.mainloop()
