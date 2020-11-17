class Quote:
    def __init__(self, quote: str, author='', date='', quote_id = None, tags=[]):
        self.quote = quote
        self.preview = quote[0:24] + '...'
        self.author = author
        self.date = date
        self.tags = tags
        self.quote_id = quote_id

    def __str__(self):
        return self.quote

    def __repr__(self):
        return '''
ID: %d
Quote: %s
Author: %s
Date: %s
''' % (self.quote_id, self.quote, self.author, self.date)

