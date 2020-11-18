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
    elif(args.author is not None):
        quotes = query_author(args.author)
    elif (args.tags is not None):
        quotes = query_tag(args.tags[0])
    else:
        quotes = query_all()
    base = "[{}] {}\n - {} {}"
    for quote in quotes:
        print(base.format(quote.quote_id, quote.quote, quote.author, quote.date))



def main():
    parser = argparse.ArgumentParser(description='Save and view your favorite quotes on the commandline!')
    parser.add_argument('-q', '--quote', type=str, nargs='?', help='The quote text to save/search for')
    parser.add_argument('-a', '--author', type=str, nargs='?', help='The author to save with'
                                                                'the quote or search for')
    parser.add_argument('-t', '--tags', type=str, nargs='+', help='Tags to associate the quote with for'
                                                                'later searching/tag to search for')
    parser.add_argument('-d', '--date', type=str, nargs='?', help='The date this quote was created in'
                                                                'month/day/YEAR format')
    parser.add_argument('-f', '--find', action='store_true', help='Search for quotes')
    parser.add_argument('--delete', type=int, nargs='?', help='Delete a quote based on id')
    args = parser.parse_args()
    if(args.find):
        find_quote(args)
    elif(args.delete):
        delete_quote(args.delete)
    else:
        save_quote(args)

if __name__ == "__main__":
    main()

