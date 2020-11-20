#! /usr/bin/env python3
import argparse
import datetime

from quoter.data import *
from quoter.model import *


def save_quote(args):
    quote = args.quote
    author = args.author
    date = args.date
    if (date is not None):
        date = datetime.datetime.strptime(args.date, '%m/%d/%Y').date()
    tags = [] if args.tags is None else args.tags
    insert_quote(Quote(quote, author, date, tags=tags))

def delete_quote(num: int):
    delete_quote_id(num)

def find_quote(args):
    if(args.quote is not None):
        quotes = query_quotes(args.quote)
    elif (args.id is not None):
        quotes = [query_id(args.id)]
    elif(args.author is not None):
        quotes = query_author(args.author)
    elif (args.tags is not None):
        quotes = query_tag(args.tags[0])
    else:
        quotes = query_all()
    print_quotes(quotes)

def print_quotes(quotes):
    base = "[{}] {}\n - {} {}\n"
    for quote in quotes:
        date = '' if quote.date is None else '{0:%m}/{0:%d}/{0:%Y}'.format(quote.date)
        print(base.format(quote.quote_id, quote.quote, quote.author, date))

def main():
    parser = argparse.ArgumentParser(
        description='Save and view your favorite quotes on the commandline!',
        epilog='Pass a -f flag to turn a quote insertion into a search, all flags besides date support this.')
    parser.add_argument('-q', '--quote', type=str, nargs='?', help='The quote text to save/search for')
    parser.add_argument('-a', '--author', type=str, nargs='?', help='The author to save with'
                                                                '/the author to search for')
    parser.add_argument('-t', '--tags', type=str, nargs='+', help='Tags to associate the quote with for '
                                                                'later searching/the tag to search for')
    parser.add_argument('-i', '--id', type=int, nargs='?', help='The quote_id to query for (use with -f)')
    parser.add_argument('-d', '--date', type=str, nargs='?', help='The date this quote was created in '
                                                                'month/day/YEAR format')
    parser.add_argument('-f', '--find', action='store_true', help='Search for quotes')
    parser.add_argument('--delete', metavar='ID', type=int, nargs='?', help='Delete a quote based on id')
    args = parser.parse_args()
    if(args.find):
        find_quote(args)
    elif(args.delete):
        delete_quote(args.delete)
    elif(args.quote is not None):
        save_quote(args)

if __name__ == "__main__":
    main()

