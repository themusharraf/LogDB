import sqlite3
conn = sqlite3.connect('date.db')
cursor = conn.cursor()

def create_table():