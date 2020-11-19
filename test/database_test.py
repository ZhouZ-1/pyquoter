import unittest
import datetime

from quoter.data import *
from quoter.model import *

class TestDataBase(unittest.TestCase):

    def test_insertion(self):
        create_dummy_data(1)
        quotes = query_all()
        self.assertTrue(len(quotes) > 0)
        quote = quotes[0]
        self.assertTrue(quote.quote == 'test_quote0')
        self.assertTrue(quote.author == 'test_author0')
        self.assertEqual(quote.date, datetime.datetime.strptime('11/01/2020', '%m/%d/%Y').date())
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

    def test_delete_quote(self):
        create_dummy_data(4)
        delete_quote_id(2)
        quotes = query_all()
        self.assertEqual(len(quotes), 3)
        quotes = query_quotes('quote1')
        self.assertEqual(len(quotes), 0)

    def test_tags(self):
        create_dummy_data(4)
        date = datetime.datetime.strptime('11/10/2020', '%m/%d/%Y').date()
        insert_quote(Quote('quote', 'auth', date, tags=['tag0']))
        quotes = query_tag("tag0")
        self.assertEqual(len(quotes), 2)

    def test_all_tags(self):
        create_dummy_data(4)
        tags = query_all_tags()
        self.assertEqual(len(tags['tag']), 4)
        date = datetime.datetime.strptime('11/10/2020', '%m/%d/%Y').date()
        insert_quote(Quote('quote', 'auth', date, tags=['tag0']))
        tags = query_all_tags()
        self.assertEqual(len(tags['tag0']), 2)

    def test_none(self):
        insert_quote(Quote('',''))
        quotes = query_all()

    def test_query_id(self):
        create_dummy_data(4)
        quote = query_id(1)
        self.assertIsNotNone(quote)

def create_dummy_data(num: int):
    reset_db()
    for i in range(num):
        date = datetime.datetime.strptime('11/%d/2020' % (i+1), '%m/%d/%Y').date()
        quote = Quote('test_quote%d' % i, 'test_author%d' % i,
                      date, tags=['tag', 'tag%d' % i])
        insert_quote(quote)


if __name__ == '__main__':
    unittest.main()
