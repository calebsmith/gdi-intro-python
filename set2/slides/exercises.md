![Girl Develop It Logo](../images/gdi_logo_badge.png)

###Intro to Python
####Additional Exercises
@@@

###Functions

* Write a program that uses at least one function to solve a geometry problem

* The program will generally have three steps:

    * Obtain input
    * Call a function to calculate the answer
    * Display the answer

* Hint: You can take user input with raw_input() as before, or use the example
below to take arguments from the command line
* Download [geometry.py](http://calebsmith.github.io/gdi-intro-python/examples/geometry.py) and use it as an example

Note: Let's Develop It 15 Minutes

@@@

###Text processing

Write a program that opens a text file and does some processing.

* The program should take a word as input and determine if the word appears in the file

* The program should use at least one function to do its work and you should be able to import this function in a Python shell and call it with a word and filename

The next page lists the things you will need.

Note:  Let's develop it: 15 minutes

@@@

###Text processing - Requirements

* Use the functions from [helpers.py](http://calebsmith.github.io/gdi-intro-python/examples/helpers.py) to help with reading in the lines and/or words of the file

* Download a plain text english dictionary like the following: [english.txt](http://calebsmith.github.io/gdi-intro-python/examples/english.txt) and put it into the same directory as your python file.

* Download a book in plain text from [Project Gutenburg](http://www.gutenberg.org/wiki/Main_Page) and put it into the same directory as your python file.

The next slide shows some code to help you get started.

@@@

###Text processing - Example Code

```python
from helpers import generate_cleaned_lines

def is_word_in_file(word, filename):
    for line in generate_cleaned_lines(filename):
        # line will be a string of each line of the file in order
        # Your code goes here.
        # Your code should do something with the word and line variables and assign the value to a variable for returning
input_word = raw_input("Enter a word to search for:")
answer = is_word_in_file(input_word, 'pride.txt')
# Display the answer in some meaningful way
```

I have used [Pride and Prejudice](http://calebsmith.github.io/gdi-intro-python/examples/pride.txt) from Project Gutenburg with my example code. You can click this link and copy/paste the text into a new text file called 'pride.txt' and save it in the same folder as your code
