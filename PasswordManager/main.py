import customtkinter
from portal import Dashboard

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("300x350")
        self.configure(fg_color="black")

        self.messageLabel = customtkinter.CTkLabel(
            self,
            text="Welcome Back!",
            fg_color="transparent"
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

        self.button1 = customtkinter.CTkButton(self, text="Submit",command=self.extract_data) #add command
        self.button1.pack(pady=20)

        self.createButton = customtkinter.CTkButton(self, text="Create Account") #command takes to another screen)
        self.createButton.pack(pady=5)

    #ReadMe #1
    #Extract the field of username and password filled by the user
    #Temporary master password
    def extract_data(self):
        #ReadMe #2
        getUser = self.username.get("1.0", "end-1c")
        getPass = self.password.get("1.0", "end-1c")
        
        if getUser == "user" and getPass == "1234":
            print("OK DONE")
            self.destroy()
            portal = Dashboard() #We can pass username to then display "Welcome ____"
            portal.mainloop()

        #connect DB
        #add encryption(make ur own algo maybe)
        #master pass
        #cool GUI
        #use at least 1 data structure

app = App()
app.mainloop()