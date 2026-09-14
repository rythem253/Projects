import os
import customtkinter
from cryptography.fernet import Fernet
from portal import DashboardFrame

# Anchor paths to this script's folder instead of the current working
# directory, so the key file is always found/created in the same place
# no matter where you launch `python main.py` from.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KEY_FILE = os.path.join(BASE_DIR, "secret.key")


def get_key():
    """Load the existing encryption key, or create and save a new one."""
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as f:
            return f.read()

    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    return key


class App(customtkinter.CTk):
    """
    The ONE Tk root window for the whole app. We never create a second
    CTk() root or call mainloop() more than once - instead we swap
    between a LoginFrame and a DashboardFrame inside this single window.

    (Two separate CTk() roots + a nested mainloop() call is what was
    causing the "invalid command name ...<lambda>" errors on close -
    pending after() jobs from the login textboxes' blinking cursor kept
    firing after that window was destroyed mid-callback.)
    """

    def __init__(self):
        super().__init__()
        self.geometry("400x450")
        self.configure(fg_color="black")
        self.title("Password Manager")

        self.key = get_key()

        self.login_frame = LoginFrame(self, self)
        self.login_frame.place(relwidth=1, relheight=1)

        self.dashboard_frame = None  # created lazily, after a successful login

        self.login_frame.tkraise()

    def show_dashboard(self):
        if self.dashboard_frame is None:
            self.dashboard_frame = DashboardFrame(self, self)
            self.dashboard_frame.place(relwidth=1, relheight=1)
        self.geometry("320x240")
        self.dashboard_frame.tkraise()


class LoginFrame(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="black")
        self.controller = controller

        self.messageLabel = customtkinter.CTkLabel(
            self,
            text="Welcome Back!",
            fg_color="transparent",
            text_color="white"
        )
        self.messageLabel.pack(pady=20)

        # Frame for Username row
        self.user_frame = customtkinter.CTkFrame(self)
        self.user_frame.pack(pady=10)

        self.message1 = customtkinter.CTkLabel(self.user_frame, text="Username")
        self.username = customtkinter.CTkTextbox(self.user_frame, width=120, height=40)

        self.message1.pack(side="left", padx=10)
        self.username.pack(side="left", padx=10)

        # Frame for Password row
        self.pass_frame = customtkinter.CTkFrame(self)
        self.pass_frame.pack(pady=10)

        self.message2 = customtkinter.CTkLabel(self.pass_frame, text="Password")
        self.password = customtkinter.CTkTextbox(self.pass_frame, width=120, height=40)

        self.message2.pack(side="left", padx=10)
        self.password.pack(side="left", padx=10)

        self.button1 = customtkinter.CTkButton(self, text="Submit", command=self.extract_data)  # add command
        self.button1.pack(pady=20)

        self.createButton = customtkinter.CTkButton(self, text="Create Account")  # command takes to another screen
        self.createButton.pack(pady=5)

    # ReadMe #1
    # Extract the field of username and password filled by the user
    # Temporary master password
    def extract_data(self):
        # ReadMe #2
        getUser = self.username.get("1.0", "end-1c")
        getPass = self.password.get("1.0", "end-1c")

        if getUser == "admin" and getPass == "123":
            print("OK DONE")
            self.controller.show_dashboard()  # We can pass username to then display "Welcome ____"

        # connect DB
        # add encryption(make ur own algo maybe)
        # master pass
        # cool GUI
        # use at least 1 data structure


if __name__ == "__main__":
    app = App()
    app.mainloop()