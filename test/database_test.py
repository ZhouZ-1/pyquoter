import unittest

from quoter.data import *
from quoter.model import *

class TestDataBase(unittest.TestCase):

    def test_insertion(self):
        reset_db()
        quote = Quote('test_quote', 'test_author', '2000-01-01 10:00:00')
        insert_quote(quote)
        quotes = all_quotes()
        self.assertTrue(len(quotes) > 0)
        quote = quotes[0]
        self.assertTrue(quote.quote == 'test_quote')
        self.assertTrue(quote.author == 'test_author')
        self.assertTrue(quote.date == '2000-01-01 10:00:00')
        self.assertTrue(quote.quote_id == 1)

    def test_query_author(self):
        reset_db()
        quote = Quote('test_quote1', 'test_author1', '2000-01-01 10:00:00')
        insert_quote(quote)
        quote = Quote('test_quote1', 'test_author2', '2000-01-01 10:00:00')
        insert_quote(quote)
        authors = query_author('test_author1')
        self.assertEqual(len(authors), 1)

        reset_db()
        quote = Quote('test_quote1', 'test_author1', '2000-01-01 10:00:00')
        insert_quote(quote)
        quote = Quote('test_quote2', 'test_author2', '2000-01-01 10:00:00')
        insert_quote(quote)
        quote = Quote('test_quote3', 'test_author2', '2000-01-01 10:00:00')
        insert_quote(quote)
        authors = query_author('author')
        self.assertEqual(len(authors), 3)

if __name__ == '__main__':
    unittest.main()
