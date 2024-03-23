import customtkinter as ctk

class App():
    def __init__(self, screen_type, user=None):
        self.window = ctk.CTk()
        self.width = screen_type[0]
        self.height = screen_type[1]
        self.window.geometry(f'{str(self.width)}x{str(self.height)}')

        #fonts
        # self.title_font = ctk.CTkFont()


    def boot(self):
        boot_frame = ctk.CTkFrame(self.window, fg_color='#c7c7c7', width=self.width, height=self.height).place(x=0, y=0)

        boot_btn = ctk.CTkButton(boot_frame, width=150, height=70, bg_color='#c7c7c7', command=self.homepage).place(x=125, y=315)

        # add code to run the boot animation
        self.window.mainloop()

    def homepage(self):
        home_frame = ctk.CTkFrame(self.window, fg_color='#e3e3e3', width=self.width, height=self.height).place(x=0, y=0)

        title_frame = ctk.CTkFrame(home_frame,bg_color='#c4c4c4', fg_color='#c4c4c4', width=self.width, height=50).place(x=0, y=0)
        title_text = ctk.CTkLabel(title_frame, text="be a hero", bg_color='#c4c4c4', text_color='#fc5000', font=('Borel', 25, 'bold')).place(x=145, y=10)  # add a font argument to this

        

if __name__ == "__main__":
    phone = [400, 700]
    app = App(phone)
    app.boot()

