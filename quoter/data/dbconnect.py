import sqlite3
import os
from ..model import Quote

path = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(path + '/data.db')
command = conn.cursor()

create_table_command = '''CREATE TABLE IF NOT EXISTS quotes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                quote TEXT,
                author TEXT,
                date DATE);
                '''
create_tags_command = '''CREATE TABLE IF NOT EXISTS tags (
                id INTEGER PRIMARY KEY,
                tag TEXT NOT NULL,
                quote_id INTEGER REFERENCES quotes(quote_id) ON DELETE CASCADE
                );
                '''
command.execute(create_table_command)
command.execute(create_tags_command)

insert_quote_command = "INSERT INTO quotes(quote, author, date) VALUES (?, ?, ?)"
insert_tag_command = "INSERT INTO tags(tag, quote_id) VALUES (?, ?)"
query_all_command = 'SELECT * FROM quotes;'
query_tag_command = '''SELECT q.id, q.quote, q.author, q.date
                    FROM quotes as q
                    JOIN tags AS t
                    ON q.id = t.quote_id
                    WHERE t.tag = ?;
                    '''
drop_table_command = 'DROP TABLE IF EXISTS quotes;'
drop_tags_command = 'DROP TABLE IF EXISTS tags'
query_author_command = 'SELECT * FROM quotes WHERE author LIKE ?'
query_quote_command = 'SELECT * FROM quotes WHERE quote LIKE ?'
select_last_id_command = 'SELECT last_insert_rowid() FROM quotes'
delete_quote_command = 'DELETE FROM quotes WHERE id=?'

def insert_quote(quote: Quote):
    execute_command(insert_quote_command, params=(quote.quote, quote.author, quote.date))
    quote.quote_id = execute_command(select_last_id_command).lastrowid
    tags = quote.tags;
    for t in tags:
        execute_command(insert_tag_command, (t, quote.quote_id))

def delete_quote_id(quote_id: int):
    execute_command(delete_quote_command, (quote_id,))

def query_all():
    response = []
    quotes = execute_command(query_all_command)
    for quote in quotes:
        response.append(_create_quote(quote))
    return response

def query_author(author: str):
    response = []
    quotes = execute_command(query_author_command, ('%' + author + '%',))
    for quote in quotes:
        response.append(_create_quote(quote))
    return response

def query_tag(tag: str):
    response = []
    quotes = execute_command(query_tag_command, (tag,))
    for quote in quotes:
        response.append(_create_quote(quote))
    return response

def query_quotes(quote: str):
    response = []
    quotes = execute_command(query_quote_command, ('%' + quote + '%',))
    for quote in quotes:
        response.append(_create_quote(quote))
    return response

def reset_db():
    command.execute(drop_table_command)
    command.execute(drop_tags_command)
    command.execute(create_table_command)
    command.execute(create_tags_command)
    conn.commit()

def execute_command(request, params=()):
    try:
        if len(params) > 0:
            res = command.execute(request, params)
        else:
            res = command.execute(request)
        conn.commit()
        return res
    except sqlite3.OperationalError:
        print('Data Error for command %s, resetting Table' % request)
        reset_db()
        return []

def _create_quote(row):
    return Quote(row[1], row[2], row[3], row[0])

