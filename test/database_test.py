import unittest
import os
import sys

from quoter.data import *
from quoter.model import *

class TestDataBase(unittest.TestCase):

    def test_insertion(self):
        quote = Quote('test_quote', 'test_author', '2000-01-01 10:00:00')
        insert_quote(quote)
        quotes = all_quotes()

if __name__ == '__main__':
    unittest.main()
