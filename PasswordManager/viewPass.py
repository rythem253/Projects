import customtkinter
from encrypt import Decrypt


class ViewPasswords(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        super().__init__(parent, fg_color="black")
        self.message1 = customtkinter.CTkLabel(self, text="Saved Passwords", text_color="white", font=("Times New Roman", 30))
        self.message1.pack(pady=20)
        self.gap1 = customtkinter.CTkLabel(self, text="---------------------------------------", font=("Arial", 35), text_color="White")
        self.gap1.pack()

        self.label1 = None
        self.row_frames = []

        # Back button fixed at the bottom
        self.backBtn = customtkinter.CTkButton(
            self,
            text="Back",
            command=self.controller.frame_a.tkraise
        )
        self.backBtn.pack(side="bottom", pady=10)

    def Display(self, storage):

        for frame in self.row_frames:
            frame.destroy()
        self.row_frames.clear()

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
            row_frame = customtkinter.CTkFrame(self, fg_color="#1c1c1c", corner_radius=8)
            row_frame.pack(fill="x", padx=10, pady=4)
            self.row_frames.append(row_frame)

            # Sub-frame just for this one row's two labels, side by side
            info_row = customtkinter.CTkFrame(row_frame, fg_color="transparent")
            info_row.pack(fill="x", padx=10, pady=8)

            username_row = customtkinter.CTkLabel(info_row, text=f"{service}                 {username}", text_color="white", anchor="w")
            username_row.pack(side="left")

            pass_row = customtkinter.CTkLabel(info_row, text=decrypt_pass, text_color="white", anchor="e")
            pass_row.pack(side="right", padx=(0, 100))