![Girl Develop It Logo](../images/gdi_logo_badge.png)

###Intro to Python
####Section 1
@@@

## Welcome
Girl Develop It is here to provide affordable and accessible programs to learn software through mentorship and hands-on instruction.

Some rules

* We are here for you
* Every question is important
* Help each other
* Have fun
@@@

###What we will cover today

* Why Python? <!-- .element: class="fragment" -->
* What is programming? <!-- .element: class="fragment" -->
* Variables and arithmetic <!-- .element: class="fragment" -->
* Statements and Error Messages <!-- .element: class="fragment" -->
* Development Environment Setup <!-- .element: class="fragment" -->
@@@

###Why Python?

* Suitable for beginners, yet used by professionals
* Readable, maintainable code
* Rapid rate of development
* Few "magical" side-effects
* Variety of applications
Note: Block 1 begins - 25 minutes
@@@

###What is Python used for?

* System Administration (Fabric, Salt, Ansible)
* 3D animation and image editing (Maya, Blender, Gimp)
* Scientific computing (numpy, scipy)
* Web development (Django, Flask)
* Game Development (Civilization 4, EVE Online)
@@@

###Who is using Python?

* Disney
* Dropbox
* Canonical and Red Hat
* Google
* NASA
Note: Caktus uses Python
@@@

###What is programming?</h3>

* Teaching the computer to do a task
* A program is made of one or more files of code, each of which solve part of the overall task
* Programming code is human readable but also needs a form that the computer can run directly. This form is not human readable.
* To create the form of code the computer can use, we use the Python <a href="http://en.wikipedia.org/wiki/Interpreter_(computing)">interpreter</a>. Other languages use other interpreters or a <a href="http://en.wikipedia.org/wiki/Compiler">compiler</a>
* Don't focus on what's "under the hood" for now. We will "drive the car" first
* In other words, there are many layers to the onion. We start at one layer and slowly move toward layers that are beneath or above us
@@@

###Command line, Python Shell, Text Editors</h3>

Program      | Description
-------------|----------
Terminal     | A program that has a command line interface and issues commands to the operating system.
Python Shell | A command line program that runs inside of the terminal, takes Python code as input, interprets it, and prints out any results.
Text Editor  | A program that opens text files and allows the user to edit and save them. (Different than a word processor).
@@@

###Example Text Editors

Platform  | Examples
----------|----------
Linux     | Gedit, Jedit, Kate
MacOSX    | TextMate, TextWrangler
Windows   | Notepad++
All       | Sublime Text, Vim, Emacs
@@@

###Let's Develop It
Let's setup our computer for Python programming

* Let's install a text editor - [Install Sublime Text 3](http://www.sublimetext.com/3)
* [Install Python](http://www.python.org/download/) - (This step is for Windows users only. GNU/Linux and MacOSX come with Python installed)
* (Windows only): After installing Python, open the "powershell" program and type:
<pre style="width: 100%">[Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\Python27", "User")</pre>
* Locate and run the terminal program. Type 'python' and hit enter.
* More setup instructions are available: [here](http://learnpythonthehardway.org/book/ex0.html)
* (You can, but don't have to install the other text editors recommended in this guide)
Note: 15 minutes
@@@

##Block 2
Note: 30 minutes
@@@

###Working in the Python Shell

Open up your terminal and type 'python' <!-- .element class="left-align" -->

* Follow along with the examples in the slides. Type them in! <!-- .element class="fragment" -->
* Feel free to explore as well. You will not accidentally break things <!-- .element class="fragment" -->
* $ means you are in the terminal (not python). >>> means you are in python <!-- .element class="fragment" -->
* Type exit() to leave python and return to the terminal. <!-- .element class="fragment" -->

@@@

###Variables and Arithmetic
```python
>>> 3 + 4
7
>>> 2 * 4
8
>>> 6 - 2
4
>>> 4 / 2
2
```
```python
>>> a = 2
>>> print a
2
>>> b = 3
>>> c = a + b
>>> print c
5
```
```python
>>> a = 0
>>> a = a + .5
>>> print a
0.5
```
@@@

###Strings
```python
>>> a = 'Hello '
>>> b = 'World'
>>> c = a + b
>>> print c
'Hello World'
```
```python
>>> a = "Spam "
>>> b = a * 4
>>> print b
"Spam Spam Spam Spam"
```
@@@

###Data types
* Variables are names of objects <!-- .element class="fragment" -->
* Among other things, variables are used to represent something that can't be known until the program is run <!-- .element class="fragment" -->
* Objects always have a "type" <!-- .element class="fragment" -->
* The type of an object helps define what it can do <!-- .element class="fragment" -->
* The type can be found using: type() <!-- .element class="fragment" -->
* type() is a function. We call it by using parenthesis and pass it an object by placing the object inside the parenthesis <!-- .element class="fragment" -->
```python
>>> print type(4)
<type 'int'>
>>> a = 4
>>> print type(a)
<type 'int'>
>>> print type("But I don't like spam")
<type 'str'>
>>> print type(3.5)
<type 'float'>
```
@@@

###Data types - continued ...
* Objects can be used with a set of operators <!-- .element class="fragment" -->
* An int or float can be used with any of: +, -, *, / <!-- .element class="fragment" -->
* A string can be used with any of: +, * <!-- .element class="fragment" -->
* What happens if we try to use division or subtraction with a string? <!-- .element class="fragment" -->
```python
>>> print "Spam" / "eggs"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```
@@@


###Errors

* There are different kinds of errors that can occur. We've seen a few of these so far <!-- .element class="fragment" -->
* A runtime error results in an Exception. An Exception gives us some information about the nature of the error and how to correct it <!-- .element class="fragment" -->
* One type of exception is a SyntaxError. This results when our code can not be evaluated because it is incorrect at a syntactic level. In other words, we are not following the "rules" of the language. <!-- .element class="fragment" -->
* Some other examples are the TypeError and NameError exceptions. <!-- .element class="fragment" -->
@@@

###Errors - continued ...

* A \# is a code comment. These are not evaluated by Python

```python
# SyntaxError - Doesn't conform to the rules of Python.
# This statement isn't meaningful to the computer
>>> 4spam)eggs(garbage) + 10

# NameError - Using a name that hasn't been defined yet.
>>> a = 5
>>> print b

# TypeError - Using an object in a way that its type does not support
>>> 'string1' / 'string2'
```
@@@

###Let's Develop It
* We'll practice what we've learned in the shell
* Review the slides on your computer and practice entering any commands you didn't fully understand before
* Ask the teacher or a TA for any help
Note: Let's develop it: 30 minutes.
@@@

###Using the terminal
Try each of the following commands in turn:

Command         | Short for               | Description
----------------|-------------------------|-------------
pwd             | Print working directory | Displays what folder you are in
ls              | List                    | Displays the files and folders in the current folder
cd <folder>     | Change Directory        | Change to another folder, where <folder> is the target
cat <filename>  | Concatenate k           | Prints the contents of the file
file <filename> | File                    | Displays the type of the file

Note: Block 3 begins, 30 minutes
@@@

###Creating a folder
We need a folder to save and run our code from.

($ shows the shell prompt where commands are entered. Lines without $ are output)
```bash
$ cd
$ pwd
/home/username ( or /User/username or similar)
$ mkdir gdipython
$ cd gdipython
$ pwd
/home/username/gdipython
```
Now that the folders are made, we only have to use this in the future:

`$ cd ~/gdipython`
@@@

###The Text Editor
Open sublime text.

* Click File, then Open folder. Navigate to the gdipython folder we created and click "open"
* In the text editor, enter the following:

```python
print 'This is a Python program'
```

* Click file, save as. Type 'program.py' and click ok.

---
Open a terminal and type
```bash
$ cd
$ cd gdipython
$ python program.py
```

You should see the terminal print:

`This is a Python program`
@@@

###User Input
To obtain user input, use 'raw_input()'. This will become a string

We use float() to make it a number

Change the program.py text to the following and run it again
```python
input_value = raw_input("Enter a radius:")
radius = float(input_value)
area = 3.14159 * radius * radius
print "The area of a circle with radius", input_value, "is", area
```
@@@

###Let's Develop It
Write your own program that uses raw_input and does something else with the value

You can use float() or int() to treat the input as a number if you need a number, or you can use the input directly if you need a string

Note: Let's develop it: 15 minutes
@@@

###Questions?
