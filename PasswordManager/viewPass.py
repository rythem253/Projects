import customtkinter
from encrypt import Decrypt


class ViewPasswords(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        super().__init__(parent, fg_color="black")

        self.label1 = None
        self.multiple_frames = []
        
        # Back button fixed at the bottom
        self.backBtn = customtkinter.CTkButton(
            self,
            text="Back",
            command=self.controller.frame_a.tkraise
        )
        self.backBtn.pack(side="bottom", pady=10)


#rows all combines database rows
#row single row

# row_frame            
# └── info_row         
#     ├── username_row 
#     └── pass_row     

    def Display(self, storage):

        for frame in self.multiple_frames:
            frame.destroy()
        self.multiple_frames.clear()

        rows = storage.get_rows()  # Displays encrypted rn

        for row in rows:
            service = row[1]
            username = row[2]
            encrypted_password = row[3]

            # Row was encrypted with a different key (or is corrupted).
            # Show it instead of crashing the whole dashboard.
            try:
                decrypt_pass = Decrypt(encrypted_password, self.controller.key)
            except Exception:
                decrypt_pass = "<undecryptable - wrong key?>"

            # The card container for this one row
            row_frame = customtkinter.CTkFrame(self, fg_color="#1c1c1c", corner_radius=10)
            row_frame.pack(fill="x", padx=10, pady=4)
            self.multiple_frames.append(row_frame)

            info_row = customtkinter.CTkFrame(row_frame,fg_color="transparent")
            info_row.pack(fill="x", padx=10, pady=8)

            info_row.columnconfigure(0, weight=3, uniform="cols")
            info_row.columnconfigure(1, weight=3, uniform="cols")
            info_row.columnconfigure(2, weight=3, uniform="cols")
            info_row.columnconfigure(3, weight=1, uniform="cols")

            # Sub-frame
            service_label = customtkinter.CTkLabel(info_row, text=service, text_color="white", anchor="w")
            service_label.grid(row=0, column=0, sticky="w", padx=5)

            username_label = customtkinter.CTkLabel(info_row, text=username, text_color="white", anchor="w")
            username_label.grid(row=0, column=1, sticky="w", padx=5)

            pass_label = customtkinter.CTkLabel(info_row, text="********", text_color="white", anchor="w")
            pass_label.grid(row=0, column=2, sticky="w", padx=5)

            button_show = customtkinter.CTkButton(info_row, text="👁", width=40)
            button_show.grid(row=0, column=3, padx=5)

            button_hide = customtkinter.CTkButton(info_row, text="‿", width=40)
            button_hide.grid(row=0, column=3, padx=5)
            button_hide.grid_remove()    # start hidden, only the eye shows at first

            def showPass(label=pass_label, pw=decrypt_pass, show=button_show, hide=button_hide):
                label.configure(text=pw)
                show.grid_remove()
                hide.grid()

            def hidePass(label=pass_label, show=button_show, hide=button_hide):
                label.configure(text="********")
                hide.grid_remove()
                show.grid()

            button_show.configure(command=showPass)
            button_hide.configure(command=hidePass)