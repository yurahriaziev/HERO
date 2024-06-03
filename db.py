import sqlite3

class DB:
    def __init__(self):
        self.conn = sqlite3.connect('HERO')
        self.cur = self.conn.cursor()

    def create_table(self, table_name, *columns):
        columns = ', '.join(columns)
        query = f'CREATE TABLE IF NOT EXISTS {table_name} ({columns})'

        self.cur.execute(query)
        self.conn.commit()

    def add_item(self, table_name, **col_data):
        colums = ', '.join(col_data.keys())
        placeholders = ', '.join('?' * len(col_data))
        print(placeholders)

        query = f'INSERT INTO {table_name} ({colums}) VALUES ({placeholders})'

        values = tuple(col_data.values())

        self.cur.execute(query, values)

        self.conn.commit()

    def get_user(self, username, password):
        user = self.cur.execute(f'SELECT * FROM Users WHERE username = ? AND password = ?', (username, password,)).fetchone()
        return user

    def view_table(self, table):
        data = self.cur.execute(f'SELECT rowid, * FROM {table}').fetchall()
        return data

# for  testing
if __name__ == '__main__':
    db = DB()
    db.cur.execute('''INSERT INTO Users (first_n, last_n, username, birth_date_day, birth_date_month, birth_date_year, email, password) VALUES ('AdminName', 'AdminLast', 'admin001', 8, 'Feb', 2006, 'admin@gmail.com', 'myadminpass')''')
    db.cur.execute('''INSERT INTO Users (first_n, last_n, username, birth_date_day, birth_date_month, birth_date_year, email, password) VALUES ('John', 'Doe', 'johndoe343', 4, 'Mar', 2004, 'johnd@gmail.com', 'password1234')''')
    db.cur.execute('''INSERT INTO Users (first_n, last_n, username, birth_date_day, birth_date_month, birth_date_year, email, password) VALUES ('Bob', 'Morch', 'BigBob', 18, 'Jun', 2008, 'bobm@gmail.com', '00000000')''')
    db.view_table('Users')
    user = db.get_user('admin001', 'myadminpass')
    print(user[2])