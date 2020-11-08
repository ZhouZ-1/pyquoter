import sqlite3
import os

path = os.path.dirname(os.path.abspath(__file__))
print(path)
conn = sqlite3.connect(path + '/test.db')

cursor = conn.cursor()
cursor.execute('''CREATE TABLE test (
                id INTEGER PRIMARY KEY,
                quote text,
                author text)
                ''')
