import sqlite3

def loadscript(name):
    with open(f"./db/scripts/{name}", 'r') as file:
        return file.read()

def init_db():
    connection = sqlite3.connect('./db/data.db')
    cursor = connection.cursor()
    cursor.executescript(loadscript('init.sql'))