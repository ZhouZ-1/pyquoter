import sqlite3
import os
from ..model import Quote

path = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(path + '/data.db')
command = conn.cursor()

create_table_command = '''CREATE TABLE IF NOT EXISTS quotes (
                id INTEGER PRIMARY KEY,
                quote TEXT,
                author TEXT,
                date DATE)
                '''
command.execute(create_table_command)

insert_quote_command = "INSERT INTO quotes(quote, author, date) VALUES (?, ?, ?)"
query_all_command = 'SELECT * FROM quotes;'
drop_table_command = 'DROP TABLE IF EXISTS quotes'

def insert_quote(quote: Quote):
    command.execute(insert_quote_command,
                    [quote.quote, quote.author, quote.date])
def all_quotes():
    response = []
    quotes = command.execute(query_all_command)
    for quote in quotes:
        response.append(Quote(quote[1], quote[2], quote[3], quote[0]))
    return response

def reset_db():
    command.execute(drop_table_command)
    command.execute(create_table_command)
