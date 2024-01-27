import sqlite3

conn = sqlite3.connect('date.db')
cursor = conn.cursor()


conn.commit()
conn.close()


def create_table():
    ...
