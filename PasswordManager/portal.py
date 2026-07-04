import customtkinter

class Dashboard(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("320x240")
        self.configure(fg_color="black")

        self.message1 = customtkinter.CTkLabel(self, text="Welcome Back User !", font=("Arial", 24), text_color="royalblue")
        self.message1.pack(side="top", pady=20)

        self.message2 = customtkinter.CTkLabel(self, text="Please select from options below:")
        self.message2.pack(pady=5)

        self.btnView = customtkinter.CTkButton(self, text="View Passwords")
        self.btnAdd = customtkinter.CTkButton(self, text="Add Password")

        self.btnView.pack(pady=5)
        self.btnAdd.pack(pady=5)

