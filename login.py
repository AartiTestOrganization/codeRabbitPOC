# login.py
import sqlite3

def login(username, password):
    conn = sqlite3.connect("users.database")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username='{username}' and password='{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    return user
