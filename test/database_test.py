import unittest

from quoter.data import *
from quoter.model import *

class TestDataBase(unittest.TestCase):

    def test_insertion(self):
        create_dummy_data(1)
        quotes = all_quotes()
        self.assertTrue(len(quotes) > 0)
        quote = quotes[0]
        self.assertTrue(quote.quote == 'test_quote0')
        self.assertTrue(quote.author == 'test_author0')
        self.assertTrue(quote.date == '2000-01-01 10:00:00')
        self.assertTrue(quote.quote_id == 1)

    def test_query_author(self):
        create_dummy_data(2)
        authors = query_author('test_author1')
        self.assertEqual(len(authors), 1)

        create_dummy_data(3)
        authors = query_author('author')
        self.assertEqual(len(authors), 3)

    def test_query_quote(self):
        create_dummy_data(3)
        quotes = query_quotes('quote')
        self.assertEqual(len(quotes), 3)
        quotes = query_quotes('quote2')
        self.assertEqual(len(quotes), 1)

def create_dummy_data(num: int):
    reset_db()
    for i in range(num):
        quote = Quote('test_quote%d' % i, 'test_author%d' % i,
                      '2000-01-01 10:00:0%d' % i)
        insert_quote(quote)


if __name__ == '__main__':
    unittest.main()
