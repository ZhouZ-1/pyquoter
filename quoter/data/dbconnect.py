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
query_author_command = 'SELECT * FROM quotes WHERE author LIKE ?'

def insert_quote(quote: Quote):
    execute_command(insert_quote_command, params=[quote.quote, quote.author, quote.date])

def all_quotes():
    response = []
    quotes = execute_command(query_all_command)
    for quote in quotes:
        response.append(_create_quote(quote))
    return response

def query_author(author: str):
    response = []
    quotes = execute_command(query_author_command, [author])
    for quote in quotes:
        response.append(_create_quote(quote))
    return response



def reset_db():
    command.execute(drop_table_command)
    command.execute(create_table_command)
    conn.commit()

def execute_command(request, params=[]):
    try:
        if len(params) > 0:
            res = command.execute(request, params)
        else:
            res = command.execute(request)
        conn.commit()
        return res
    except sqlite3.OperationalError:
        print('Data Error, resetting Table')
        reset_db()
        return []

def _create_quote(row):
    return Quote(row[1], row[2], row[3], row[0])

