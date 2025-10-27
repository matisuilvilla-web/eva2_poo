import sqlite3
import os


class Database:
    def __init__(self, db_name='eva2.db'):
        self.db_name = db_name

    def connect(self):
        return sqlite3.connect(self.db_name)
    
