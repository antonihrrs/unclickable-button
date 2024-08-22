import random
import customtkinter as ctk

class UnclickableButton:
    def __init__(self, master):
        self.master = master
        self.master.title("Unclickable Button")
        self.root_geometry()

        self.buttons = {"click_here": None}

        self.show_button_first()

    def show_button_first(self):
        self.buttons["click_here"] = ctk.CTkButton(self.master, text="Click here",
                                                   text_color="dark blue", fg_color="light grey",
                                                   border_width=2, border_color="purple",
                                                   corner_radius=8)
        self.buttons["click_here"].place(relx=0.5, rely=0.5, anchor="center")
        self.buttons["click_here"].bind("<Enter>", self.hovering_react)

    def hovering_react(self, event):
        on_x, on_y = self.random_position()
        self.buttons["click_here"].place(relx=on_x, rely=on_y, anchor="center")

    def random_position(self):
        return random.uniform(0.1, 0.9), random.uniform(0.1, 0.9)

    def root_geometry(self):
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        self.master.geometry(f"{screen_width}x{screen_height}")

if __name__ == "__main__":
    root = ctk.CTk()
    game = UnclickableButton(root)
    root.mainloop()
