import customtkinter
from encrypt import Encrypt


class AddPassword(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="black")
        self.controller = controller
        self.message2 = customtkinter.CTkLabel(self, text="Add New Password", text_color="white")
        self.message2.pack()

        # Frame 1
        self.service_frame = customtkinter.CTkFrame(self)
        self.service_frame.pack(pady=5)

        self.lblSer = customtkinter.CTkLabel(self.service_frame, text="service", text_color="black")
        self.serviceTextBox = customtkinter.CTkTextbox(self.service_frame, width=150, height=10)

        self.lblSer.pack(side="left", padx=10)
        self.serviceTextBox.pack(side="left", padx=10)

        # Frame 2
        self.user_frame = customtkinter.CTkFrame(self)
        self.user_frame.pack(pady=5)

        self.lbl1 = customtkinter.CTkLabel(self.user_frame, text="username", text_color="black")
        self.username = customtkinter.CTkTextbox(self.user_frame, width=150, height=10)

        self.lbl1.pack(side="left", padx=10)
        self.username.pack(side="left", padx=10)

        # Frame 3
        self.pass_frame = customtkinter.CTkFrame(self)
        self.pass_frame.pack(pady=5)

        self.lbl2 = customtkinter.CTkLabel(self.pass_frame, text="password", text_color="black", )
        self.password = customtkinter.CTkTextbox(self.pass_frame, width=150, height=10)

        self.lbl2.pack(side="left", padx=10)
        self.password.pack(side="left", padx=10)

        self.btnAdd = customtkinter.CTkButton(self, text="Add", command=self.handleAdd)
        self.btnAdd.pack(pady=10)
        # Need to send password and username to encryption class to do security stuff
        # then from there send to SQL.

        self.backBtn = customtkinter.CTkButton(self, text="Back",
            command=lambda: controller.frame_a.tkraise())
        self.backBtn.pack()

    def handleAdd(self):
        service = self.serviceTextBox.get("1.0", "end-1c")
        username = self.username.get("1.0", "end-1c")
        plain_pass = self.password.get("1.0", "end-1c")
        encrypted_pass = Encrypt(plain_pass, self.controller.key)

        self.controller.db.addStuff(service, username, encrypted_pass)