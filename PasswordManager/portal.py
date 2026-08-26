import customtkinter
from storage import Database
from encrypt import Encrypt
from encrypt import Decrypt

class Dashboard(customtkinter.CTk):

    def __init__(self, key):
        super().__init__()
        self.key = key
        self.geometry("320x240")
        self.configure(fg_color="black")

        self.db = Database()

        self.frames = {}

        #Frame_a, the main portal screen
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
        self.controller = controller
        super().__init__(parent, fg_color="black")
        self.message1 = customtkinter.CTkLabel(self, text="Saved Passwords", text_color="white")
        self.message1.pack()

        self.label1 = None

        # Back button fixed at the bottom
        self.backBtn = customtkinter.CTkButton(
            self,
            text="Back",
            command=self.controller.frame_a.tkraise
        )
        self.backBtn.pack(side="bottom", pady=10)
        
    def Display(self, storage):
        rows = storage.get_rows()
        if self.label1 is not None:
            self.label1.destroy()  # remove old label before adding new one
        self.label1 = customtkinter.CTkLabel(self, text=str(rows), text_color="white")
        self.label1.pack()


    
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

        self.lbl2 = customtkinter.CTkLabel(self.pass_frame, text="password", text_color="black")
        self.password = customtkinter.CTkTextbox(self.pass_frame, width=150, height=10)
                
        self.lbl2.pack(side="left", padx=10)
        self.password.pack(side="left", padx=10)

        self.btnAdd = customtkinter.CTkButton(self, text="Add", command=self.handleAdd)
        self.btnAdd.pack(pady=10)
        #Need to send password and username to encryption class to do security stuff
        #then from there send to SQL. 

        
        self.backBtn = customtkinter.CTkButton(self, text="Back",
            command=lambda: controller.frame_a.tkraise())
        self.backBtn.pack()

        plain_pass = self.password.get("1.0", "end-1c")

    def handleAdd(self):
        service = self.serviceTextBox.get("1.0", "end-1c")
        username = self.username.get("1.0", "end-1c")
        plain_pass = self.password.get("1.0", "end-1c")
        encrypted_pass = Encrypt(plain_pass, self.controller.key)

        self.controller.db.addStuff(service, username, encrypted_pass)

        decrypt_pass = Decrypt(encrypted_pass, self.controller.key)


#.tkraise()

if __name__ == "__main__":
    from cryptography.fernet import Fernet
    test_key = Fernet.generate_key()
    app = Dashboard(test_key)
    app.mainloop()