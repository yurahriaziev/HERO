import customtkinter as ctk
from PIL import Image, ImageTk
from db import DB

class App():
    def __init__(self, screen_type, user=None):
        self.current_user = user
        self.window = ctk.CTk()
        self.width = screen_type[0]
        self.height = screen_type[1]
        self.window.geometry(f'{str(self.width)}x{str(self.height)}')
        self.window.resizable(0, 0)

        self.current_page = ''

        self.blue = '#2d89a3'
        self.light_blue = '#3492AD'

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
        # print('Current users')
        users = self.database.view_table('Users')
        # for user in users: print(user)
        # adding dummy opportunity events and accessing the Opportunity Events table
        # event1_desc = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras ultricies, nisl id elementum porta, tortor urna placerat risus, non lobortis enim leo ac ex. Proin tempor lorem id lacus luctus laoreet. Praesent tempus lectus lectus. Aliquam cursus, felis sit amet aliquam elementum, dolor massa aliquam sem, quis aliquet lorem nunc.'
        # self.database.cur.execute('''INSERT INTO OpportunityEvents (title, description, location_country_city, date_start, organizer, contact_phone, contact_email, application_link) VALUES ('Opportunity Event 1', ?, 'Israel/Tel Aviv', '5/4/2024', 'Organizer1', '300-434-0000', 'organizer1@gmail.com', 'url2apply.com')''', (event1_desc,))
        # self.database.cur.execute('''INSERT INTO OpportunityEvents (title, description, location_country_city, date_start, organizer, contact_phone, contact_email, application_link) VALUES ('Opportunity Event 2', ?, 'Israel/Jerusalem', '12/3/2024', 'Organizer1', '300-434-0000', 'organizer1@gmail.com', 'url2apply.com')''', (event1_desc,))
        # self.database.cur.execute('''INSERT INTO OpportunityEvents (title, description, location_country_city, date_start, organizer, contact_phone, contact_email, application_link) VALUES ('Opportunity Event 3', ?, 'Israel/Tel Aviv', '30/6/2024', 'Organizer2', '300-434-0890', 'organizer2@gmail.com', 'url2apply.com')''', (event1_desc,))
        # self.database.cur.execute('''INSERT INTO OpportunityEvents (title, description, location_country_city, date_start, organizer, contact_phone, contact_email, application_link) VALUES ('Opportunity Event 4', ?, 'Israel/Jerusalem', '11/2/2024', 'Organizer3', '300-434-2800', 'organizer3@gmail.com', 'url2apply.com')''', (event1_desc,))
        # self.database.cur.execute('''INSERT INTO OpportunityEvents (title, description, location_country_city, date_start, organizer, contact_phone, contact_email, application_link) VALUES ('Opportunity Event 5', ?, 'Israel/Tel Aviv', '3/4/2024', 'Organizer4', '300-434-2300', 'organizer4@gmail.com', 'url2apply.com')''', (event1_desc,))
        # self.database.cur.execute('''INSERT INTO OpportunityEvents (title, description, location_country_city, date_start, organizer, contact_phone, contact_email, application_link) VALUES ('Opportunity Event 6', ?, 'Israel/Jerusalem', '28/5/2024', 'Organizer4', '300-434-2300', 'organizer4@gmail.com', 'url2apply.com')''', (event1_desc,))
        # self.database.cur.execute('''INSERT INTO OpportunityEvents (title, description, location_country_city, date_start, organizer, contact_phone, contact_email, application_link) VALUES ('Opportunity Event 7', ?, 'Israel/Tel Aviv', '15/8/2024', 'Organizer5', '300-434-0980', 'organizer5@gmail.com', 'url2apply.com')''', (event1_desc,))
        # self.database.conn.commit()
        

        self.events = self.database.view_table('OpportunityEvents')
        # for event in self.events:
        #     print(event)

        #fonts
        # self.title_font = ctk.CTkFont()

        #loading in icons
        self.menu_icon = ImageTk.PhotoImage(Image.open("icons/menu.png").resize((20, 20)))
        self.open_card_icon = ImageTk.PhotoImage(Image.open("icons/open_card.png").resize((20, 20)))
        self.location_icon = ctk.CTkImage(light_image=Image.open("icons/location.png").resize((20, 20)))
        self.email_icon = ctk.CTkImage(light_image=Image.open("icons/arroba.png").resize((20, 20)))
        self.phone_icon = ctk.CTkImage(light_image=Image.open("icons/call.png").resize((20, 20)))
        self.left_arrow = ctk.CTkImage(light_image=Image.open("icons/left_arrow.png").resize((20, 20)))

    def boot(self):
        boot_frame = ctk.CTkFrame(self.window, fg_color='white', width=self.width, height=self.height).place(x=0, y=0)

        boot_btn = ctk.CTkButton(boot_frame, text='START', width=150, height=70, bg_color='#c7c7c7', command=self.login_page).place(x=125, y=315)

        # add code to run the boot animation
        self.window.mainloop()

    def header(self, master):
        self.my_x = -200
        # change orange everywhere to blue
        title_frame = ctk.CTkFrame(master, bg_color=self.blue, fg_color=self.blue, width=self.width, height=50).place(x=0, y=0)
        self.menu = self.menu_frame()
        title_text = ctk.CTkLabel(title_frame, text="be a hero", bg_color=self.blue, text_color='white', font=('Borel', 25, 'bold')).place(x=145, y=10)  # add a font argument to this
        self.menu_btn = ctk.CTkButton(title_frame, image=self.menu_icon, text="", width=40, height=40, fg_color=self.blue, bg_color=self.blue, corner_radius=2, hover_color=self.light_blue, command=self.open_menu)
        self.menu_btn.place(x=5, y=5)

        if self.current_user:
            admin_icon = ImageTk.PhotoImage(Image.open("icons/user.png").resize((30, 30)))
            admin_account_btn = ctk.CTkButton(title_frame, image=admin_icon, text="", width=40, height=40, fg_color=self.blue, bg_color=self.blue, corner_radius=2, hover_color=self.light_blue, command=self.user_page)
            admin_account_btn.place(x=self.width-45, y=5)

    def homepage(self):
        self.current_page = 'home-page'
        self.home_frame = ctk.CTkFrame(self.window, fg_color='white', width=self.width, height=self.height)
        self.home_frame.place(x=0, y=0)
        self.header(self.home_frame)

        self.main_content_frame = ctk.CTkScrollableFrame(self.home_frame, width=self.width-20, height=self.height-60, fg_color='white')
        self.main_content_frame.place(x=0,y=50)

        # adding opportunity card placeholders
        if len(self.events) > 0:
            for event in self.events:
                self.card = ctk.CTkFrame(self.main_content_frame, fg_color='#c7c7c7', width=400, height=100)
                self.card.pack(pady=5)

                self.card_desc = ctk.CTkFrame(self.card, width=230, height=80, fg_color='#e3e3e3')
                self.card_desc.place(x=100, y=10)

                self.card_img = ctk.CTkFrame(self.card, width=80, height=80)   
                self.card_img.place(x=10, y=10)

                # event details
                event_title = ctk.CTkLabel(self.card_desc, text=event[1], text_color='black', font=(self.font, 15, 'bold'))
                event_title.place(x=5, y=0) 
                event_desc = ctk.CTkLabel(self.card_desc, text=event[2], text_color='#8f8f8f', font=(self.font, 12))
                event_desc.place(x=5, y=25) 
                event_location = ctk.CTkLabel(self.card_desc, text=f'Where: {event[3]}', text_color='black', font=(self.font, 12))
                event_location.place(x=5, y=50) 

                open_card_btn = ctk.CTkButton(self.card, image=self.open_card_icon, text="", width=40, height=80, fg_color=self.blue,
                                            bg_color='#c7c7c7', corner_radius=5, hover_color=self.light_blue, command=lambda e=event: self.event_page(e))
                open_card_btn.place(x=340, y=10)
        else:
            message = ctk.CTkLabel(self.main_content_frame, text='No available events', font=(self.font, 20, 'bold'), text_color='#c7c7c7')
            message.pack(pady=20)

        self.window.mainloop()

    def user_page(self):
        self.current_page = 'user-page'
        self.user_page_frame = ctk.CTkFrame(self.window, width=self.width, height=self.height, fg_color='white')
        self.user_page_frame.place(x=0, y=0)

        self.header(self.user_page_frame)

    def login_page(self):
        self.current_page = 'login-page'
        if not self.current_user:
            self.title = ctk.CTkLabel(self.window, text='hero', font=(self.font, 50, 'bold'), text_color=self.blue, bg_color='white')
            self.title.place(x=155, y=100)
            self.main_login_frame = ctk.CTkFrame(self.window, width=self.width-100, height=170, bg_color='white', fg_color='#c7c7c7')
            self.main_login_frame.place(x=50, y=250)

            self.username = ctk.CTkEntry(self.window, width=280, height=50, placeholder_text='Username', font=(self.font, 20), bg_color='#c7c7c7', fg_color='white', border_color='white', corner_radius=10, placeholder_text_color='#a3a3a3', text_color='#a3a3a3')
            self.username.place(x=60, y=260)
            self.password = ctk.CTkEntry(self.window, width=280, height=50, placeholder_text='Password', font=(self.font, 20), bg_color='#c7c7c7', fg_color='white', border_color='white', corner_radius=10, placeholder_text_color='#a3a3a3', text_color='#a3a3a3')
            self.password.place(x=60, y=320)

            open_card_btn = ctk.CTkButton(self.window, image=self.open_card_icon, text="", width=290, height=30, fg_color=self.blue, bg_color='#c7c7c7', corner_radius=5, hover_color=self.light_blue, command=self.access_user)
            open_card_btn.place(x=55, y=380)
        else:
            self.homepage()

    def access_user(self):
        username = self.username.get()
        password = self.password.get()
        self.current_user = self.database.get_user(username, password)

        if self.current_user:
            self.homepage()
        else:
            ctk.CTkLabel(self.window, text='Could not find user', text_color='#ff384c', bg_color='white', font=(self.font, 30, 'bold')).place(x=70, y=430)

    def event_page(self, event):
        self.current_page = 'event-page'
        self.page = ctk.CTkFrame(self.window, width=self.width, height=self.height)
        self.page.place(x=0, y=0)

        self.header(self.page)

        self.event_frame = ctk.CTkScrollableFrame(self.page, width=self.width-20, height=self.height-50, fg_color='white', bg_color='white')
        self.event_frame.place(x=0, y=50)

        self.event_img_frame = ctk.CTkFrame(self.event_frame, width=self.width-40)
        self.event_img_frame.pack(pady=(10, 0))

        self.event_title = ctk.CTkLabel(self.event_frame, text=event[1], font=(self.font, 30, 'bold'), text_color='black')
        self.event_title.pack(pady=10, padx=10, anchor='w')

        self.event_desc = ctk.CTkTextbox(self.event_frame, width=self.width-10, fg_color='white', text_color='black', wrap='word')
        self.event_desc.insert("0.0", event[2])
        self.event_desc.configure(state='disabled')
        self.event_desc.pack(padx=10)

        self.location_frame = ctk.CTkFrame(self.event_frame, width=self.width-40, height=30, fg_color='white')
        self.location_frame.pack()
        self.location1 = ctk.CTkLabel(self.location_frame, image=self.location_icon, text="") #, width=self.width-40, height=30 , text=f'Where: {event[3]}', text_color='#5c5c5c'
        self.location1.place(x=0, y=0)
        self.location2 = ctk.CTkLabel(self.location_frame, text=event[3], text_color='#5c5c5c')
        self.location2.place(x=20, y=0)

        self.contact_frame = ctk.CTkFrame(self.event_frame, width=self.width-40, height=85, fg_color='white')
        self.contact_frame.pack()
        self.contact_title = ctk.CTkLabel(self.contact_frame, bg_color='white', text='Contact Us', font=(self.font, 15, 'bold'), text_color='#212121')
        self.contact_title.place(x=0, y=0)
        email_img = ctk.CTkLabel(self.contact_frame, image=self.email_icon, text="", bg_color='white')
        email_img.place(x=0, y=25)
        email = ctk.CTkLabel(self.contact_frame, text=event[7], text_color='black')
        email.place(x=25, y=22)
        phone_img = ctk.CTkLabel(self.contact_frame, image=self.phone_icon, text="", bg_color='white')
        phone_img.place(x=0, y=55)
        phone = ctk.CTkLabel(self.contact_frame, text=event[6], text_color='black')
        phone.place(x=25, y=52)



        self.placeholder_frame = ctk.CTkFrame(self.event_frame, height=120, bg_color='white', fg_color='white')
        self.placeholder_frame.pack(pady=5)

        self.apply_btn = ctk.CTkButton(self.page, text='apply now', width=self.width-40, height=100, fg_color=self.blue, corner_radius=20, bg_color='white', hover_color=self.light_blue)
        self.apply_btn.place(x=16, y=580)

    def menu_frame(self):
        frame = ctk.CTkFrame(self.window, height=self.height-50, width=200)

        if not self.current_page == 'home-page':
            home_text = ctk.CTkLabel(frame, text='Back Home', font=(self.font, 25), text_color='#c7c7c7')
            home_text.place(x=26, y=0)
            home_btn = ctk.CTkButton(frame, text='', image=self.left_arrow, fg_color='#7d7d7d', hover_color='#c7c7c7', corner_radius=0,command=self.homepage)
            home_btn.place(x=20, y=30)
        else:
            searcb_text = ctk.CTkLabel(frame, text='Search Events', font=(self.font, 25), text_color='#c7c7c7')
            searcb_text.place(x=26, y=0)

            search_box = ctk.CTkTextbox(frame, width=180, height=30, wrap='none', bg_color='white', fg_color='white', text_color='black')
            search_box.place(x=10,y=40)

        return frame

    def open_menu(self):
        # Define a function to animate the menu opening
        def animate_open():
            if self.my_x < 0:
                self.my_x += 20
                self.menu.place(x=self.my_x, y=50)
                # Call animate_open again after a delay if menu is not fully opened
                if self.my_x < 0:
                    self.window.after(10, animate_open)

        # Define a function to animate the menu closing
        def animate_close():
            if self.my_x > -200:
                self.my_x -= 20
                self.menu.place(x=self.my_x, y=50)
                # Call animate_close again after a delay if menu is not fully closed
                if self.my_x > -200:
                    self.window.after(10, animate_close)

        # Define the close_menu function
        def close_menu():
            animate_close()
            # Change command of menu button to open_menu after closing animation
            self.menu_btn.configure(command=self.open_menu)

        # Check if menu is currently closed
        if self.my_x < 0:
            # If menu is closed, start opening animation
            animate_open()
            # Change command of menu button to close_menu
            self.menu_btn.configure(command=close_menu)
        else:
            # If menu is open, start closing animation
            close_menu()


if __name__ == "__main__":
    phone = [400, 700]
    app = App(phone)
    app.boot()
