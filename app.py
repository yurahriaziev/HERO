import customtkinter as ctk
import time

class App(ctk.CTk):
    def __init__(self, screen_type, user=None):
        super().__init__()
        self.width = screen_type[0]
        self.height = screen_type[1]
        self.geometry(f'{str(self.width)}x{str(self.height)}')


    def boot(self):
        boot_frame = ctk.CTkFrame(self, fg_color='#c7c7c7', width=self.width, height=self.height).place(x=0, y=0)

        # add code to run the boot animation

        self.homepage(self)

        self.mainloop()

    def homepage(self, parent):
        home_frame = ctk.CTkFrame(parent, fg_color='#e3e3e3', width=self.width, height=self.height).place(x=0, y=0)

        

if __name__ == "__main__":
    phone = [400, 700]
    app = App(phone)
    app.boot()

