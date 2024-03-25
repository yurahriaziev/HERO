import customtkinter as ctk
from PIL import Image, ImageTk
from db import DB

class App():
    def __init__(self, screen_type, user=None):
        self.window = ctk.CTk()
        self.width = screen_type[0]
        self.height = screen_type[1]
        self.window.geometry(f'{str(self.width)}x{str(self.height)}')
        self.window.resizable(0, 0)

        self.window.title('HERO')

        #fonts
        # self.title_font = ctk.CTkFont()

        #loading in icons
        self.menu_icon = ImageTk.PhotoImage(Image.open("icons/menu.png").resize((20, 20)))
        self.open_card_icon = ImageTk.PhotoImage(Image.open("icons/open_card.png").resize((20, 20)))


    def boot(self):
        boot_frame = ctk.CTkFrame(self.window, fg_color='#c7c7c7', width=self.width, height=self.height).place(x=0, y=0)

        boot_btn = ctk.CTkButton(boot_frame, text='START', width=150, height=70, bg_color='#c7c7c7', command=self.homepage).place(x=125, y=315)

        # add code to run the boot animation
        self.window.mainloop()

    def homepage(self):
        self.home_frame = ctk.CTkFrame(self.window, fg_color='#e3e3e3', width=self.width, height=self.height)
        self.home_frame.place(x=0, y=0)

        title_frame = ctk.CTkFrame(self.home_frame,bg_color='#ff861c', fg_color='#ff861c', width=self.width, height=50).place(x=0, y=0)
        title_text = ctk.CTkLabel(title_frame, text="be a hero", bg_color='#ff861c', text_color='white', font=('Borel', 25, 'bold')).place(x=145, y=10)  # add a font argument to this
        menu_button = ctk.CTkButton(title_frame, image=self.menu_icon, text="", width=40, height=40, fg_color='#ff861c', bg_color='#ff861c', corner_radius=2, hover_color='#ff9a42')
        menu_button.place(x=self.width-45, y=5)

        self.main_content_frame = ctk.CTkScrollableFrame(self.home_frame, width=self.width-20, height=self.height-60, fg_color='#dedede')
        self.main_content_frame.place(x=0,y=50)

        for i in range(20):
            self.card = ctk.CTkFrame(self.main_content_frame, fg_color='#c7c7c7', width=400, height=100)
            self.card.pack(pady=5)

            self.card_desc = ctk.CTkFrame(self.card, width=230, height=80, fg_color='#e3e3e3')
            self.card_desc.place(x=100, y=10)

            self.card_img = ctk.CTkFrame(self.card, width=80, height=80)   
            self.card_img.place(x=10, y=10)  

            open_card_btn = ctk.CTkButton(self.card, image=self.open_card_icon, text="", width=40, height=80, fg_color='#ff861c', bg_color='#c7c7c7', corner_radius=5, hover_color='#ff9a42')
            open_card_btn.place(x=340, y=10)

        self.window.mainloop()

        

if __name__ == "__main__":
    phone = [400, 700]
    app = App(phone)
    app.boot()
