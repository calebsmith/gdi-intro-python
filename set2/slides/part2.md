![Girl Develop It Logo](../images/gdi_logo_badge.png)

###Intro to Python
####Section 2
@@@

###Review

* Arithmetic
* Variables
* Data types
* Text editor, command line, and python shell
@@@


###What we will cover today
* Boolean Expressions and Conditionals <!-- .element: class="fragment" -->
* Loops <!-- .element: class="fragment" -->
* Functions <!-- .element: class="fragment" -->
@@@

###Boolean Expressions
We can tell the computer to compare values and return True or False. These are called *Boolean expressions*

* Test for equality by using ==. (This is not the same as using =)
* Test for greater than and less than using > and <
```python
>>> a = 5
>>> b = 5
>>> print a == b
True
>>> print a < 3
False
>>> # Combine comparison and assignment
>>> c = a == b
>>> print c
True
```

Note: Block 1 - 25 Minutes
@@@

###Boolean Expressions continued

The following chart shows the various Boolean operators

Expression | Tests
-----------|-----------------
a == b     | a is equal to b
a != b     | a does not equal b
a < b      | a is less than b
a > b      | a is greater than b
a <= b     | a is less than or equal to b
a >= b     | a is greater than or equal to b

```python
>>> a = 3
>>> b = 4
>>> print a != b
True
>>> print a <= 3
True
>>> print a >= 4
False
```
@@@

###Conditionals

When we want different code to execute dependending on certain criteria, we use a **conditional**
We achieve this using **if** statements
```python
if x == 5:
    print 'x is equal to 5'
```
We often want a different block to execute if the statement is false. This can be accomplished using **else*
```python
if x == 5:
    print 'x is equal to 5'
else:
    print 'x is not equal to 5'
```
@@@

###Indentation

In Python, **blocks** begin when text is indented and ends when it returns to the previous indentation level.

The line that begins a new block ends with a colon.

Let's look at the previous example again with a few minor changes and examine the meaning of its indentation</p>

```python
if x == 5:
    print 'x is equal to 5'
    a = 1
    print 'Still in the x == 5 block'
else:
    print 'x is not equal to 5'
    a = 2
print 'Outside of the if or else blocks. This will run regardless of the value of x'
print "Value of a is", a
```
@@@

###Chained conditionals
Conditionals can also be **chained**

Chained conditionals use **elif** as an additonal check after the preceeding `if` predicate was False.
```python
if x > 5:
    print 'x is greater than 5'
elif x < 5:
    print 'x is less than 5'
else:
    print 'x is equal to 5'
```
@@@

###Nested conditionals
Conditionals can also be **nested**

Nested conditionals occur inside of other conditionals and are indented yet again. When each code block is complete, it is unindented
```python
if x > 5:
    print 'x is greater than 5'
    if x > 10:
        print '...it is also greater than 10'
    print 'Done evaluating the x > 10 block'
print 'Done evaluating the x > 5 block'
```
@@@

###Let's Develop It
Write a program that uses if statements to determine what to do given some user input

The code below is an example:
```python
health = 100
print "A vicious warg is chasing you."
print "Options:"
print "1 - Hide in the cave."
print "2 - Climb a tree."
input_value = raw_input("Enter choice:")
if input_value == '1':
    print 'You hide in a cave.'
    print 'The warg finds you and injures your leg with its claws'
    health = health - 10
elif input_value == '2':
    print 'You climb a tree.'
    print 'The warg eventually looses interest and wanders off'
print "Game under construction. Come back later"
```
Note: Let's develop it: 15 minutes
@@@

###Iteration
It is often useful to perform a task and to repeat the process until a certain point is reached.

The repeated execution of a set of statements is called **iteration**

One way to acheive this, is with the **while** loop.
```python
x = 10
while x > 0:
    print x
    x = x - 1
print 'Done'
```
The while statement takes a boolean expression, and as long as it evaluates to True, the code block beneath it is repeated.

This creates a **loop**. Without the `x = x - 1` statement, this would be an **infinite loop**

Note: Block 2 - 25 minutes
@@@

###While loops continued

A loop can also terminate at any point with a **break** statement

An infinite loop can be created using an expression that is always True.

This is most commonly done with the constant True.

```python
while True:
    name = raw_input("What is your name (type 'quit' to quit)? ")
    if name == 'quit':
        break
    print "Hello,", name
```
@@@

###While loops example
Consider the following example that uses iteration to derive a factorial

(A factorial of a number is equal to that number * every positive integer less than that number. E.g. The factorial of 4 is `4 * 3 * 2 * 1`, which equals 24
```python
input_value = raw_input('Enter a positive integer:')
n = int(input_value)
result = 1
while n > 1:
    result = result * n
    n = n - 1
print "The factorial of " + input_value + " is:"
print result
```
N.B. - This implementation does not work for negative numbers. Why? <!-- .element class="fragment" -->
@@@

###For loops
It is also useful to loop through a collection of elements, visiting each one to do some work, then stopping once all elements are processed.

This can be accomplished with a **for** loop

First, we need a collection. We create a **list** of numbers to loop over. This is called `numbers` in the following example
```python
numbers = [1, 3, 8]
for number in numbers:
    print "The current number is:"
    print number
```
@@@

###For loops continued
Let's examine the example carefully
```python
numbers = [1, 3, 8]
for number in numbers:
    print "The current number is:"
    print number
```
The for loop has three parts:

* The collection to loop over - numbers
* The name to give each element when the loop begins again - number
* The block of statements to execute with the element - The two print statements
@@@

###Let's Develop It
* Write a program that takes numbers from user input and adds thems all
together for a final result.
* This program should stop taking input, display the answer and exit when the user types "quit".
* Hint:
```python
result = 0
while True:
    input_value = raw_input("Enter a number:")
    ... (put more code here) ...
print "The final sum is", result
```

Note: Let's Develop It - 15 minutes
@@@


###Functions

Also known as "procedures"

- A named unit of code that performs a specific task

When one uses a function, one makes a function **call**

We have already made a function call when using the type, int, or float functions

```python
>>> a = '3'
>>> print type(a)
<type 'str'>
>>> a = float(a)
>>> print type(a)
<type 'float'>
```

Note: Block 3 - 40 Minutes
@@@

###Function calls

```python
# Repeating the previous example for reference
>>> a = 3
>>> print type(a)
<type 'int'>
```

A function can take **arguments** (sometimes called **parameters**)

In the example above, the variable `a` is passed as an argument to the function `type`

A function call can be an argument to another function call.

```python
# Some more function call examples

>>> str(int(3.2))
'3'
```
@@@

###Function definition

The following example is a **function definition**. This allows us to create our own functions

```python
def print_greeting(name):
    print "Hi", name
    print "How are you"
```

The function definition has the following parts

* The <strong>def</strong> keyword signifies we are defining a function</li>
* The name of the function being defined - `print_greeting`</li>
* The arguments in parentheses - `name`</li>
* The function <strong>body</strong>, which is a block of indented code that executes when the function is called. - `print "Hi", name...`</li>
@@@

###Function returns</h3>

A function can also **return** a value

To do this, one uses the **return** keyword
```
def plus_5(x):
    return x + 5

y = plus_5(4)
```

* This allows us to call a function to obtain a value for later use. (Not the same as printing the value)</li>
* In this example, the function call `plus_5(4)` evaluates to 9, and y is set to this value</li>
* To determine what a function will return, use the <strong>substitution method</strong>.</li>
* If return is not used, the function returns <strong>None</strong></li>
@@@

###Functions with no arguments

A function does not have to take arguments, as in the following example:

```python
def newline():
    print ''

newline()
# prints an empty line. Nothing is returned
```

This is useful when the function does some work but doesn't need any parameters. i.e. The function is intended to always do the same thing
@@@

###Functions with more than one argument

A function can also take more than one argument separated by commas. For example:

```python
def get_birthday_greeting(name, age):
    return "Happy birthday to " + name + " who just turned " + str(age) + "!"

greeting = get_birthday_greeting("Virginia", 16)
print greeting
# Happy birthday to Virginia who just turned 16!
```
@@@

###Scope

The **scope** of a variable is the area of code in which a variable is still valid and can be used.

Variables defined within a function can not be used elsewhere.

```python
def get_average(a, b):
    total = a + b
    return total / 2.0

avg = get_average(10, 20)

print avg
# 15
print a
# NameError
print total
# NameError
```

Note: Draw a diagram with bubbles
@@@

###Import statements

The **import** statement allows us to use Python code that is defined in one file in a different file, or inside of the shell.

The **from** keyword allows us to only import parts of a Python file

```python
# In knights.py
def shrubbery():
    print "I am a shrubber"

def ni(number):
    print "Ni!" * 3
```

```python
# Run a Python shell in the same directory as knights.py and enter the following
import knights

knights.shrubbery()
knights.ni()

# or
from knights import shrubbery, ni
shrubbery()
ni()
```
@@@


###Let's Develop It
* Write a game that displays a board and allows a player to move on the board.

* The beginning of this program has been started and is available here as
[game1.py](http://calebsmith.github.io/gdi-intro-python/examples/game1.py)

* More instructions can be found in the game1.py file

* You'll also need to download the board.dat file to the same folder.
 [board.dat](http://calebsmith.github.io/gdi-intro-python/examples/board.dat)

* If you are stuck ask the teacher or a TA for help.

Note: Let's Develop It 25 minutes
@@@


###Let's Develop It
* Improve our adventure game by preventing the player from walking through
walls

* The beginning of this program has been started and is available here as
[game2.py](http://calebsmith.github.io/gdi-intro-python/examples/game2.py)

* You'll also need to download the board.dat file to the same folder.
 [board.dat](http://calebsmith.github.io/gdi-intro-python/examples/board.dat)

* If you are stuck ask the teacher or a TA for help.

* If you finish early, consider adding a feature of your own or helping your
 neighbor

Note: Let's Develop It 30 minutes
@@@

###Questions?
