#!/usr/bin/python
"""
Suitable after taking class 4

Some text processing functions that help open a plain-text book and process
its lines into a collection of discreet words therein.

Plain text books without copyright can be obtained from Project Gutenberg:
http://www.gutenberg.org/

run 'python book.py' to see the list of words in a text file, that are not in
the dictionary.

The default book is "Pride and Prejudice" by Jane Austen found
in pride.txt

run 'python book.py a.txt' to open a different book (in this case a.txt)
"""

import sys
from helpers import get_english_words, generate_words


DEFAULT_BOOK = 'pride.txt' 


def main(filename):
    try:
        words_set = set(generate_words(filename))
    except IOError:
        print 'File {0} not found'.format(filename)
        return
    english_words = get_english_words()
    not_in_english = words_set.difference(english_words)
    print 'Words in {0} that are not in the dictionary:'.format(filename)
    for word in sorted(list(not_in_english)):
        print word


if __name__ == '__main__':
    help_flag = False
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == '-h' or arg == '--help':
            help_flag = True
            print __doc__
        filename = sys.argv[1]
    else:
        filename = DEFAULT_BOOK
    if not help_flag:
        main(filename)

