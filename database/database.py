#database/database.py
import sqlite3

class Database:
    def __init__(self):
        self.connection = None

    def create_connection(self):
        self.connection = sqlite3.connect('catering_service.db')
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS events (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    date TEXT,
                    total_hours REAL
                )
            ''')
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS workers (
                    id INTEGER PRIMARY KEY,
                    event_id INTEGER,
                    name TEXT,
                    hours REAL,
                    FOREIGN KEY (event_id) REFERENCES events (id)
                )
            ''')
