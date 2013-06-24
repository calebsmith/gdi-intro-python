#!/usr/bin/python
"""
This file contains functions to help you open and process text files

"""

import string

# Punctuation characters other than hyphen and apostrophe
PUNCTUATION_CHARS = string.punctuation.replace('-', '').replace("'", '')


def file_reader(filename):
    """
    Given a filename, returns a list of strings for each line in the file
    """
    f = open(filename, 'r')
    file_contents = f.readlines()
    f.close()
    return file_contents


def remove_punctuation(line):
    """
    Given a string, remove punctuation characters other than - or ' and return
    the resulting string
    """
    return line.translate(string.maketrans('', ''), PUNCTUATION_CHARS)


def get_english_words():
    """Returns the set of English words in lower-case"""
    return set(word.strip().lower() for word in file_reader('english.txt'))

