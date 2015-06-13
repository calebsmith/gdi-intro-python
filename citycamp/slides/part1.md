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

###This Session

* Why Python? <!-- .element: class="fragment" -->
* What is programming? <!-- .element: class="fragment" -->
* Variables and arithmetic <!-- .element: class="fragment" -->
* Statements and Error Messages <!-- .element: class="fragment" -->
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
* Caktus
@@@

###What is programming?</h3>

* Teaching the computer to do a task
* A program is made of one or more files of code
* Programming code is human readable but also needs a form that the computer can run
* Don't focus on what's "under the hood" for now. We will "drive the car" first
@@@

##Block 2
Note: 30 minutes
@@@

###Working in repl.it

Navigate to http://repl.it in a browser. Find "Python3" under languages

* Follow along with the examples in the slides. Type them in! <!-- .element class="fragment" -->
* Feel free to explore as well. You will not accidentally break things <!-- .element class="fragment" -->

@@@

###Variables and Arithmetic
```python
> 3 + 4
=> 7
> 2 * 4
=> 8
> 6 - 2
=> 4
> 4 / 2
=> 2
```

```python
> a = 2
> b = 3
> c = a + b
> print(c)
=> 5
```
```python
> a = 0
> a = a + .5
> print(a)
=> 0.5
```
@@@

###Strings
```python
> a = 'Hello '
> b = 'World'
> c = a + b
> print(c)
=> 'Hello World'
```
@@@

###Data types
* Variables are a name for some data <!-- .element class="fragment" -->
* Variables always have a "type" <!-- .element class="fragment" -->
* The type defines what it can do <!-- .element class="fragment" -->
* The type can be found using: type() <!-- .element class="fragment" -->

```python
> print type(4)
=> <type 'int'>
> a = 4
> print type(a)
=> <type 'int'>
> print type("But I don't like spam")
=> <type 'str'>
> print type(3.5)
=> <type 'float'>
```
@@@

###Type Errors
* Variables of a given type can be used with a set of operators <!-- .element class="fragment" -->
* An int or float can be used with any of: +, -, \*, / <!-- .element class="fragment" -->
* A string can be used with any of: +, \* <!-- .element class="fragment" -->
* What happens if we try to use division or subtraction with a string? <!-- .element class="fragment" -->
```python
> print "Spam" / "eggs"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```
@@@

###Errors
* An Exception gives us some information about the cause of the error <!-- .element class="fragment" -->
* Some examples are SyntaxError, TypeError and NameError exceptions. <!-- .element class="fragment" -->
@@@

###Errors - continued ...

* A \# is a code comment. These are not evaluated by Python

```python
# SyntaxError - Doesn't conform to the rules of Python.
# This statement isn't meaningful to the computer
> 4spam)eggs(garbage) + 10

# NameError - Using a name that hasn't been defined yet.
> a = 5
> print b

# TypeError - Using an object in a way that its type does not support
> 'string1' / 'string2'
```
@@@

###Let's Develop It
* We'll practice what we've learned in the shell
* Review the slides on your computer and practice entering anything you didn't fully understand before
* Ask the teacher or a TA for any help
Note: Let's develop it: 5 minutes.
@@@

###User Input
To obtain user input, use 'input()'. This will become a string

We use float() to make it a number

```python
input_value = input("Enter a radius:")
radius = float(input_value)
area = 3.14159 * radius * radius
print('The area of a circle with radius', input_value, 'is', area)
```
@@@

###Let's Develop It
Write your own program that uses input and does something else with the value

You can use float() to treat the input as a number if you need a number, or you can use the input directly if you need a string

Note: Let's develop it: 10 minutes
@@@

###Any Questions?
