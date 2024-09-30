#main.py
from database.database import Database
from gui.gui import start_gui

if __name__ == "__main__":
    Database().create_connection()
    start_gui()
