import argparse


def main():
    parser = argparse.ArgumentParser(description='Save and view your favorite quotes on the commandline!')
    parser.add_argument('-q', '--quote', type=str, nargs='?', help='The quote text to save/search for')
    parser.add_argument('-a', '--author', type=str, nargs='?', help='The author to save with'
                                                                'the quote or search for')
    parser.add_argument('-t', '--tags', type=str, nargs='+', help='Tags to associate the quote with for'
                                                                'later searching/tag to search for')
    parser.add_argument('-f', '--find', action='store_true', help='Search for quotes')
    parser.add_argument('-d', '--delete', type=int, nargs='?', help='Delete a quote based on id')
    args = parser.parse_args()
    print(args)


if __name__ == "__main__":
    main()

