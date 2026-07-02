import customtkinter

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

    #ReadMe #1
    def extract_data(self):
        #ReadMe #2
        single_line_input = self.username.get("1.0", "end-1c")
        print("Input was", single_line_input)

        

        #connect DB
        #add encryption(make ur own algo maybe)
        #master pass
        #cool GUI
        #use at least 1 data structure
        #

app = App()
app.mainloop()