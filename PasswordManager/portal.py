import customtkinter

class Dashboard(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("520x480")
        self.configure(fg_color="black")