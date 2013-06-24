#!/usr/bin/python
"""
Suitable for hacking after class 3.

This file contains functions to help you open and process text files

It also provides a function for obtaining the set of English words. This can be
used to help with anything you might want to do with spell-checking or
determing if a word is valid according to the dictionary.

N.B. The dictionary isn't necessarily exhaustive and isn't meant to be
authoritative, just a useful example to work with.

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

