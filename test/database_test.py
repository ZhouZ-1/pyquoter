import unittest
import os
import sys

from quoter.data import *
from quoter.model import *

class TestDataBase(unittest.TestCase):

    def test_insertion(self):
        reset_db()
        quote = Quote('test_quote', 'test_author', '2000-01-01 10:00:00')
        insert_quote(quote)
        quotes = all_quotes()
        quote = quotes[0]
        self.assertTrue(quote.quote == 'test_quote')
        self.assertTrue(quote.author == 'test_author')
        self.assertTrue(quote.date == '2000-01-01 10:00:00')
        self.assertTrue(quote.quote_id == 1)

if __name__ == '__main__':
    unittest.main()
