import customtkinter
from storage import Database

class Dashboard(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("320x240")
        self.configure(fg_color="black")

        self.db = Database()

        self.frames = {}

        #Frame_a, the main portal screen
        self.frame_a = customtkinter.CTkFrame(self, fg_color="black")
        self.frame_a.place(relwidth=1, relheight=1)

        self.message1 = customtkinter.CTkLabel(self.frame_a, text="Welcome Back User !", font=("Arial", 24), text_color="royalblue")
        self.message1.pack(side="top", pady=20)

        self.message2 = customtkinter.CTkLabel(self.frame_a, text="Please select from options below:")
        self.message2.pack(pady=5)

        self.btnView = customtkinter.CTkButton(self.frame_a, text="View Passwords",
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

    #This method is responsible to to change bw 2 frames
    def changeFrame(self, name):
        if name == "ViewPasswords":
            self.view_passwords_frame.Display(self.db)
            self.view_passwords_frame.tkraise()
        elif name == "AddPassword":
            self.add_password_frame.tkraise()

#--------------------------------------------------------------------------#

#Buttons have each separate class

class ViewPasswords(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="black")
        self.controller = controller
        self.message1 = customtkinter.CTkLabel(self, text="Saved Passwords")
        self.message1.pack()
        self.backBtn = customtkinter.CTkButton(self, text="Back",
                                    command=lambda: controller.frame_a.tkraise())
        self.backBtn.pack()

    def Display(self, storage):
        rows = storage.get_rows()
        self.label1 = customtkinter.CTkLabel(self, text=str(rows))
        self.label1.pack()

class AddPassword(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="black")
        self.controller = controller
        self.message2 = customtkinter.CTkLabel(self, text="Add New Password")
        self.message2.pack()
        self.backBtn = customtkinter.CTkButton(self, text="Back",
                                    command=lambda: controller.frame_a.tkraise())
        self.backBtn.pack()

#.tkraise()

if __name__ == "__main__":
    app = Dashboard()
    app.mainloop()
