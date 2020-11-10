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


def insert_quote(quote: Quote):
    command.execute(insert_quote_command,
                    [quote.quote, quote.author, quote.date])
def all_quotes():
    quotes = command.execute('SELECT * FROM quotes;')
    return quotes
