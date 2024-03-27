import customtkinter as ctk
from PIL import Image, ImageTk
from db import DB

class App():
    def __init__(self, screen_type, user=None):
        self.user = user
        self.window = ctk.CTk()
        self.width = screen_type[0]
        self.height = screen_type[1]
        self.window.geometry(f'{str(self.width)}x{str(self.height)}')
        self.window.resizable(0, 0)

        self.window.title('HERO')
        self.font = 'Baloo Bhai 2'

        #database connection
        self.database = DB()
        # create needed tables at boot up
        self.database.create_table('OpportunityEvents', 'title TEXT', 'description TEXT',
                                   'location_country_city TEXT', 'date_start TEXT',
                                   'organizer TEXT', 'contact_phone TEXT', 'contact_email TEXT',
                                   'application_link TEXT')
        self.database.create_table('Users', 'first_n TEXT', 'last_n TEXT', 'username TEXT',
                                   'birth_date_day INTEGER', 'birth_date_month TEXT',
                                   'birth_date_year INTEGER', 'email TEXT', 'password TEXT')
        
        # adding ADMIN user to the database     RUN ONES TO CREATE ADMIN ACCOUNT
        # self.database.cur.execute('''INSERT INTO Users (first_n, last_n, username, birth_date_day, birth_date_month, birth_date_year, email, password) VALUES ('AdminName', 'AdminLast', 'admin001', 8, 'Feb', 2006, 'admin@gmail.com', 'myadminpass')''')
        # self.database.conn.commit()
        print('Current users')
        users = self.database.view_table('Users')

        # adding dummy opportunity events and accessing the Opportunity Events table
        

        self.events = self.database.view_table('OpportunityEvents')

        #fonts
        # self.title_font = ctk.CTkFont()

        #loading in icons
        self.menu_icon = ImageTk.PhotoImage(Image.open("icons/menu.png").resize((20, 20)))
        self.open_card_icon = ImageTk.PhotoImage(Image.open("icons/open_card.png").resize((20, 20)))


    def boot(self):
        boot_frame = ctk.CTkFrame(self.window, fg_color='white', width=self.width, height=self.height).place(x=0, y=0)

        boot_btn = ctk.CTkButton(boot_frame, text='START', width=150, height=70, bg_color='#c7c7c7', command=self.login_page).place(x=125, y=315)

        # add code to run the boot animation
        self.window.mainloop()

    def header(self, master):

        title_frame = ctk.CTkFrame(master, bg_color='#ff861c', fg_color='#ff861c', width=self.width, height=50).place(x=0, y=0)
        title_text = ctk.CTkLabel(title_frame, text="be a hero", bg_color='#ff861c', text_color='white', font=('Borel', 25, 'bold')).place(x=145, y=10)  # add a font argument to this
        menu_btn = ctk.CTkButton(title_frame, image=self.menu_icon, text="", width=40, height=40, fg_color='#ff861c', bg_color='#ff861c', corner_radius=2, hover_color='#ff9a42')
        menu_btn.place(x=self.width-45, y=5)

        if self.user == 'admin':
            admin_icon = ImageTk.PhotoImage(Image.open("icons/user.png").resize((30, 30)))
            admin_account_btn = ctk.CTkButton(title_frame, image=admin_icon, text="", width=40, height=40, fg_color='#ff861c', bg_color='#ff861c', corner_radius=2, hover_color='#ff9a42', command=self.user_page)
            admin_account_btn.place(x=5, y=5)

    def homepage(self):
        self.home_frame = ctk.CTkFrame(self.window, fg_color='#e3e3e3', width=self.width, height=self.height)
        self.home_frame.place(x=0, y=0)
        self.header(self.home_frame)

        self.main_content_frame = ctk.CTkScrollableFrame(self.home_frame, width=self.width-20, height=self.height-60, fg_color='#dedede')
        self.main_content_frame.place(x=0,y=50)

        # adding opportunity card placeholders
        for i in range(len(self.events)):
            self.card = ctk.CTkFrame(self.main_content_frame, fg_color='#c7c7c7', width=400, height=100)
            self.card.pack(pady=5)

            self.card_desc = ctk.CTkFrame(self.card, width=230, height=80, fg_color='#e3e3e3')
            self.card_desc.place(x=100, y=10)

            self.card_img = ctk.CTkFrame(self.card, width=80, height=80)   
            self.card_img.place(x=10, y=10)  

            open_card_btn = ctk.CTkButton(self.card, image=self.open_card_icon, text="", width=40, height=80, fg_color='#ff861c', bg_color='#c7c7c7', corner_radius=5, hover_color='#ff9a42')
            open_card_btn.place(x=340, y=10)

        self.window.mainloop()

    def user_page(self):
        self.user_page_frame = ctk.CTkFrame(self.window, width=self.width, height=self.height)
        self.user_page_frame.place(x=0, y=0)

    def login_page(self):
        self.title = ctk.CTkLabel(self.window, text='hero', font=(self.font, 50, 'bold'), text_color='#ff861c', bg_color='white')
        self.title.place(x=135, y=100)
        self.main_login_frame = ctk.CTkFrame(self.window, width=self.width-100, height=190, bg_color='white', fg_color='#c7c7c7')
        self.main_login_frame.place(x=50, y=250)

        self.username = ctk.CTkEntry(self.window, width=280, height=60, placeholder_text='Username', font=(self.font, 20), bg_color='#c7c7c7', fg_color='white', border_color='white', corner_radius=10, placeholder_text_color='#a3a3a3', text_color='#a3a3a3')
        self.username.place(x=60, y=260)
        self.password = ctk.CTkEntry(self.window, width=280, height=60, placeholder_text='Password', font=(self.font, 20), bg_color='#c7c7c7', fg_color='white', border_color='white', corner_radius=10, placeholder_text_color='#a3a3a3', text_color='#a3a3a3')
        self.password.place(x=60, y=330)

        open_card_btn = ctk.CTkButton(self.window, image=self.open_card_icon, text="", width=290, height=30, fg_color='#ff861c', bg_color='#c7c7c7', corner_radius=5, hover_color='#ff9a42', command=self.access_user)
        open_card_btn.place(x=55, y=400)

    def access_user(self):
        username = self.username.get()
        password = self.password.get()
        self.current_user = self.database.get_user(username, password)

        if self.current_user:
            self.homepage()
        else:
            ctk.CTkLabel(self.window, text='Could not find user', text_color='red', font=(self.font, 10)).place(x=200, y=420)

        

if __name__ == "__main__":
    phone = [400, 700]
    app = App(phone, 'admin')
    app.boot()
