import customtkinter as ctk

class App():
    def __init__(self, screen_type, user=None):
        self.window = ctk.CTk()
        self.width = screen_type[0]
        self.height = screen_type[1]
        self.window.geometry(f'{str(self.width)}x{str(self.height)}')

        self.window.title('HERO')

        #fonts
        # self.title_font = ctk.CTkFont()


    def boot(self):
        boot_frame = ctk.CTkFrame(self.window, fg_color='#c7c7c7', width=self.width, height=self.height).place(x=0, y=0)

        boot_btn = ctk.CTkButton(boot_frame, text='START', width=150, height=70, bg_color='#c7c7c7', command=self.homepage).place(x=125, y=315)

        # add code to run the boot animation
        self.window.mainloop()

    def homepage(self):
        self.home_frame = ctk.CTkFrame(self.window, fg_color='#e3e3e3', width=self.width, height=self.height)
        self.home_frame.place(x=0, y=0)

        title_frame = ctk.CTkFrame(self.home_frame,bg_color='#c4c4c4', fg_color='#c4c4c4', width=self.width, height=50).place(x=0, y=0)
        title_text = ctk.CTkLabel(title_frame, text="be a hero", bg_color='#c4c4c4', text_color='#fc5000', font=('Borel', 25, 'bold')).place(x=145, y=10)  # add a font argument to this

        self.main_content_frame = ctk.CTkScrollableFrame(self.home_frame, width=self.width-20, height=self.height-60)
        self.main_content_frame.place(x=0,y=50)

        for i in range(20):
            self.card = ctk.CTkFrame(self.main_content_frame, fg_color='#c7c7c7', width=400, height=100)
            self.card.pack(pady=5)

            self.card_desc = ctk.CTkFrame(self.card, width=270, height=80, fg_color='#e3e3e3')
            self.card_desc.place(x=100, y=10)

            self.card_img = ctk.CTkFrame(self.card, width=80, height=80)   
            self.card_img.place(x=10, y=10)    

        self.window.mainloop()

        

if __name__ == "__main__":
    phone = [400, 700]
    app = App(phone)
    app.boot()
