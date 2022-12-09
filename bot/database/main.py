import sqlite3

class Database():
    def __init__(self):
        pass
    connect = sqlite3.connect('users2.db', check_same_thread=False)
    cursor = connect.cursor()

db = Database()
