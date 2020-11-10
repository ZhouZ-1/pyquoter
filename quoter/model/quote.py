class Quote:
    def __init__(self, quote: str, author='', date='', quote_id = None, tags=[]):
        self.quote = quote
        self.author = author
        self.date = date
        self.tags = tags
        self.quote_id = quote_id

