#/usr/bin/python
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
    Given a filename, yields each line in the file
    """
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()


def remove_punctuation(line):
    """
    Given a string, remove punctuation characters other than - or ' and return
    the resulting string
    """
    return line.translate(string.maketrans('', ''), PUNCTUATION_CHARS)


def generate_cleaned_lines(filename):
    """
    Given a filename, yields each line of the file without punctuation
    """
    return (
        remove_punctuation(line.replace('--', ' '))
        for line in file_reader(filename)
    )


def generate_words(filename):
    """
    Given a filename, generates every word of the file in lowercase, stripping
    any whitespace or punctuation. Numbers are also removed
    """
    cleaned_lines = generate_cleaned_lines(filename)
    return (
        word.lower()
        for line in cleaned_lines for word in line.split()
        if not word.isdigit() and not word.startswith("'")
    )


def get_words_list(filename):
    """
    Given a filename, returns a list of words in that file, using the same
    stripping rules as generate_words()
    """
    return list(generate_words(filename))


def get_english_words():
    """Returns the set of English words in lower-case"""
    return set(word.strip().lower() for word in file_reader('english.txt'))

