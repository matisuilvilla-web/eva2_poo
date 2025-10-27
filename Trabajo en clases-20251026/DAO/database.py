import sqlite3

class Database:
    def __init__(self, db_name='personas.db'):
        self.db_name = db_name

    def connect(self):
        return sqlite3.connect(self.db_name)
