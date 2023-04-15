import sqlite3

def get_threadspecific_cursor():
    connection = sqlite3.connect('./db/data.db')
    return connection.cursor(), connection