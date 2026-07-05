import customtkinter

class Dashboard(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("320x240")
        self.configure(fg_color="black")

        #Frame_a, the main portal screen
        self.frame_a = customtkinter.CTkFrame(self, fg_color="black")
        self.frame_a.place(relwidth=1, relheight=1)

        self.message1 = customtkinter.CTkLabel(self.frame_a, text="Welcome Back User !", font=("Arial", 24), text_color="royalblue")
        self.message1.pack(side="top", pady=20)

        self.message2 = customtkinter.CTkLabel(self.frame_a, text="Please select from options below:")
        self.message2.pack(pady=5)

        self.btnView = customtkinter.CTkButton(self.frame_a, text="View Passwords")
        self.btnView.pack(pady=5)

        self.btnAdd = customtkinter.CTkButton(self.frame_a, text="Add Password")
        self.btnAdd.pack(pady=5)

        #Frame_b, to view saved passwords
        #Display database
        

#.tkraise()
