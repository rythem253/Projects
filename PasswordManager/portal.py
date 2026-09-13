import customtkinter
from storage import Database
from viewPass import ViewPasswords
from addPass import AddPassword


class DashboardFrame(customtkinter.CTkFrame):
    """
    The main password-manager screen. This is a *frame* placed inside
    the app's single CTk root (see main.py), not its own Tk root window -

    that's what avoids the multi-mainloop / after-job crash on close.
    """

    def __init__(self, parent, app):
        super().__init__(parent, fg_color="black")
        self.key = app.key
        self.root = app

        self.db = Database()

        self.frames = {}

        # Frame_a, the main portal screen
        self.frame_a = customtkinter.CTkFrame(self, fg_color="black")
        self.frame_a.place(relwidth=1, relheight=1)

        self.message1 = customtkinter.CTkLabel(self.frame_a, text="Welcome Back User !", font=("Arial", 24), text_color="royalblue")
        self.message1.pack(side="top", pady=20)

        self.message2 = customtkinter.CTkLabel(self.frame_a, text="Please select from options below:", text_color="white")
        self.message2.pack(pady=5)

        self.btnView = customtkinter.CTkButton(self.frame_a, text="View Passwords", text_color="white",
                        command=lambda: self.changeFrame("ViewPasswords"))

        self.btnView.pack(pady=5)

        self.btnAdd = customtkinter.CTkButton(self.frame_a, text="Add Password",
                        command=lambda: self.changeFrame("AddPassword"))

        self.btnAdd.pack(pady=5)

        # Create ViewPasswords frame
        self.view_passwords_frame = ViewPasswords(self, self)
        self.view_passwords_frame.place(relwidth=1, relheight=1)

        # Create AddPassword frame
        self.add_password_frame = AddPassword(self, self)
        self.add_password_frame.place(relwidth=1, relheight=1)

        self.frame_a.tkraise()

    # This method is responsible to to change bw 2 frames
    def changeFrame(self, name):
        if name == "ViewPasswords":
            self.root.geometry("500x600")
            self.view_passwords_frame.Display(self.db)
            self.view_passwords_frame.tkraise()
        elif name == "AddPassword":
            self.add_password_frame.tkraise()


if __name__ == "__main__":
    # Small standalone harness so you can still test this screen on its
    # own, using the same single-root pattern as the real app.
    from cryptography.fernet import Fernet

    class _TestApp(customtkinter.CTk):
        def __init__(self):
            super().__init__()
            self.geometry("320x240")
            self.configure(fg_color="black")
            self.key = Fernet.generate_key()
            self.frame = DashboardFrame(self, self)
            self.frame.place(relwidth=1, relheight=1)

    _TestApp().mainloop()