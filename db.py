import sqlite3

class DB:
    def __init__(self):
        self.conn = sqlite3.connect('HERO')
        self.cur = self.conn.cursor()

    def create_table(self, table_name, *t_columns):
        columns = ', '.join(columns)
        query = f'CREATE TABLE IF NOT EXISTS {table_name} ({columns})'

        self.cur.execute(query)
        self.conn.commit()

    def add_item(self, table_name, **col_data):
        columns = ', '.join(col_data.keys())
        placeholders = ', '.join('?' * len(col_data))

        query = f'INSERT INTO {table_name}'