from .db import get_threadspecific_cursor

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @staticmethod
    def find(id):
        cursor, _ = get_threadspecific_cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
        return User(*cursor.fetchone())
    
    @staticmethod
    def find_by_username(username):
        cursor, _ = get_threadspecific_cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()
        return User(*result) if result else None
    
    @staticmethod
    def create(username, password):
        cursor, con = get_threadspecific_cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        con.commit()
        return User.find_by_username(username)
    
    @staticmethod
    def delete(id):
        cursor, con = get_threadspecific_cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (id,))
        con.connection.commit()

    @staticmethod
    def update(id, username, password):
        cursor, con = get_threadspecific_cursor()
        cursor.execute("UPDATE users SET username = ?, password = ? WHERE id = ?", (username, password, id))
        con.commit()
        return User.find(id)
    
    def check_password(self, password):
        return self.password == password 