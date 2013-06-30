#!/usr/bin/python
"""
This small program acts as a template to help you create your own programs.

The first line of this file '#!/usr/bin/python' tells the operating system to
use the Python program to run this file. On MacOSX and GNU/Linux, this allows
the program to be run from the terminal with './boilerplate.py' rather than
'python boilerplate.py'

A program using the 'if __name__ == '__main__' pattern at the bottom of this
file is more reusable because it will not automatically run main() when the
file is imported in another Python file. Therefore, functions and other code
defined here can be used elsewhere without the risk of accidentally running
code specific to this program.

For example, another file can 'import boilerplate' and use
'boilerplate.example_func()'. If main() were called at the bottom of this file
without the surrounding if statement, it would automatically execute when
boilerplate was imported with 'import boilerplate'.

This allows us to use the same Python file as a program on its own, or as Python
code for other Python code to import and use.
"""

def example_func(x):
    return x + 5


def main():
    value = example_func(5)
    print 'I am a placeholder for a program'
    print 'Surely, 5 + 5 is', value
    # call other functions and do meaningful work from here


if __name__ == '__main__':
    # This block only executes if this python file is run as a program from
    # the command line (E.g. `python boilerplate.py`).
    main()

