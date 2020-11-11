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
    execute_command(insert_quote_command, params=[quote.quote, quote.author, quote.date])

def all_quotes():
    response = []
    quotes = execute_command(query_all_command)
    for quote in quotes:
        response.append(_create_quote(quote))
    return response

def _create_quote(row):
    return Quote(row[1], row[2], row[3], row[0])

def reset_db():
    command.execute(drop_table_command)
    command.execute(create_table_command)

def execute_command(request, params=[]):
    try:
        if len(params) > 0:
            return command.execute(request, params)
        else:
            return command.execute(request)
    except sqlite3.OperationalError:
        reset_db()
        return []
