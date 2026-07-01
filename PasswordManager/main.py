import customtkinter

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("300x250")
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
        
        def button1_event():
            print('Hi')

        self.button1 = customtkinter.CTkButton(self, text="Submit", command=button1_event) #add command
        self.button1.pack(pady=20)

app = App()
app.mainloop()