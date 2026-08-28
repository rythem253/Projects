import customtkinter
from storage import Database
from encrypt import Encrypt
from encrypt import Decrypt

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
            self.root.geometry("500x600")
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
        self.message1 = customtkinter.CTkLabel(self, text="Saved Passwords", text_color="white", font=("Times New Roman", 30))
        self.message1.pack(pady=20)
        self.gap1 = customtkinter.CTkLabel(self, text="---------------------------------------", font=("Arial", 35), text_color="White")
        self.gap1.pack()

        self.label1 = None

        # Back button fixed at the bottom
        self.backBtn = customtkinter.CTkButton(
            self,
            text="Back",
            command=self.controller.frame_a.tkraise
        )
        self.backBtn.pack(side="bottom", pady=10)
        
    def Display(self, storage):
        rows = storage.get_rows() # Displays encrypted rn

        for row in rows:
            service = row[1]
            username = row[2]
            encrypted_password = row[3]

            try:
                decrypt_pass = Decrypt(encrypted_password, self.controller.key)
            except Exception:
                # Row was encrypted with a different key (or is corrupted).
                # Show it instead of crashing the whole dashboard.
                decrypt_pass = "<undecryptable - wrong key?>"

            # The card container for this one row
            row_frame = customtkinter.CTkFrame(self, fg_color="#1c1c1c", corner_radius=8)
            row_frame.pack(fill="x", padx=10, pady=4)

            # Sub-frame just for this one row's two labels, side by side
            info_row = customtkinter.CTkFrame(row_frame, fg_color="transparent")
            info_row.pack(fill="x", padx=10, pady=8)
                                                                            #Well Well Dont Forget this long line            
            username_row = customtkinter.CTkLabel(info_row, text=f"{service}                 {username}", text_color="white", anchor="w")
            username_row.pack(side="left")

            pass_row = customtkinter.CTkLabel(info_row, text=decrypt_pass, text_color="white", anchor="e")
            pass_row.pack(side="right", padx=(0, 100))
      
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


#.tkraise()

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