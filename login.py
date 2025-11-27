# login.py
import sqlite3

def login(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username='Aarti' AND password='Bhosale'"
    cursor.execute(query)
    user = cursor.fetchone()
    return user;
