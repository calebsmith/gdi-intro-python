![Girl Develop It Logo](../images/gdi_logo_badge.png)

###Intro to Python
####Section 2
@@@

###This Session
* Boolean Expressions and Conditionals <!-- .element: class="fragment" -->
* Lists and Loops <!-- .element: class="fragment" -->
@@@

###Boolean Expressions
Compare values and return True or False. These are *Boolean expressions*

* Test for equality by using ==

```python
> a = 5
> b = 5
> print(a == b)
=> True
> # Combine comparison and assignment
> c = a == b
> print(c)
=> True
```

Note: Block 1 - 25 Minutes
@@@

###Comparison Operators

The following chart shows the various Boolean operators

Expression | Tests
-----------|-----------------
a == b     | a is equal to b
a != b     | a does not equal b
a < b      | a is less than b
a > b      | a is greater than b
a <= b     | a is less than or equal to b
a >= b     | a is greater than or equal to b
@@@

### Comparison Examples

```python
> a = 3
> b = 4
> print(a != b)
=> True
> print(a <= 3)
=> True
> print(a >= 4)
=> False
```
@@@

###Conditionals

* Conditional - different coderuns depending on comparison
* We achieve this using **if** statements

```python
if x == 5:
    print('x is equal to 5')
```
@@@

###Else

Often useful to run a different block if the statement is false. Use **else**

```python
if x == 5:
    print('x is equal to 5')
else:
    print('x is not equal to 5')
```
@@@

###Indentation

The line that begins a new block ends with a colon.

**blocks** begin when text is indented and end when unindented

Let's look at the previous example again with a few minor changes and examine the meaning of its indentation

```python
if x == 5:
    print('x is equal to 5'
    a = 1
    print('Still in the x == 5 block')
else:
    print('x is not equal to 5')
    a = 2
print('Outside of if and else blocks. This will run regardless'
print('Value of a is', a)
```
@@@

###Chained conditionals
Conditionals can be **chained**

```python
if x > 5:
    print('x is greater than 5')
elif x < 5:
    print('x is less than 5')
else:
    print('x is equal to 5')
```
@@@

###Nested conditionals
Conditionals can also be **nested**

```python
if x > 5:
    print('x is greater than 5')
    if x > 10:
        print('...it is also greater than 10')
    print('Done evaluating the x > 10 block')
print('Done evaluating the x > 5 block')
```
@@@

###Let's Develop It
Write a program that uses if statements to determine what to do given some user input

Example:
```python
health = 100
print("A vicious warg is chasing you.")
print("Options:")
print("1 - Hide in the cave.")
print("2 - Climb a tree.")
input_value = input("Enter choice:")
if input_value == '1':
    print('You hide in a cave.')
    print('The warg finds you and injures your leg with its claws')
    health = health - 10
elif input_value == '2':
    print('You climb a tree.')
    print('The warg eventually looses interest and wanders off')
print("Game under construction. Come back later")
```
Note: Let's develop it: 15 minutes
@@@

###Iteration
The repeated execution of a set of statements is called **iteration**

One way to acheive this, is with the **while** loop.
```python
x = 10
while x > 0:
    print(x)
    x = x - 1
print('Done')
```

The while statement takes a boolean expression.
While it is True, the block is repeated

Note: Block 2 - 25 minutes
@@@

###break

A loop can terminate at any point with a **break**

```python
while True:
    name = raw_input("What is your name (type 'quit' to quit)? ")
    if name == 'quit':
        break
    print("Hello,", name)
```
@@@

###While loops example
Consider the following example that uses iteration to derive a factorial

```python
input_value = raw_input('Enter a positive integer:')
n = int(input_value)
result = 1
while n > 1:
    result = result * n
    n = n - 1
print("The factorial of " + input_value + " is: ", result)
```
@@@

###For loops

* Looping through a collection can be accomplished with a **for** loop

First we need a collection. We create a **list** of numbers to loop over.

```python
numbers = [1, 3, 8]
for number in numbers:
    print("The current number is: ", number)
```
@@@

###For loops in detail

```python
numbers = [1, 3, 8]
for number in numbers:
    print("The current number is:", number)
```

The for loop has three parts:

* The collection to loop over - numbers
* The name to give each element - number
* The block of statements to execute with the element - The two print statements
@@@

###An Example

```
numbers = [1, 3, 8]
print(len(numbers))
```

```
numbers = [1, 3, 8]
counter = 0
for number in numbers:
    counter = counter + 1
print(counter)
```

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
    if input_value == 'quit':
        # insert code to leave the loop here
    ... (put more code here) ...
print("The final sum is", result)
```

Note: Let's Develop It - 15 minutes
@@@


###Functions

- A named unit of code that performs a specific task

- To use a function, call it with ()

We have already called print, input, type, int, float, and len

```python
> print(type(3))
=> <type 'int'>
> numbers = [1, 2, 3]
> print(len(numbers))
=> 3
```

Note: Block 3 - 30 Minutes
@@@

###Function calls

```python
# Repeating the previous example for reference
> a = 3
> print(type(a))
=> <type 'int'>
```

A function can take **arguments**

In the example above, the variable `a` is passed as an argument to the function `type`

A function call can be an argument to another function call.

```python
# Some more function call examples
> str(int(3.2))
=> '3'
```
@@@

###Function definition

The following example is a **function definition**. This allows us to create our own functions

```python
def print_greeting(name):
    print("Hi", name)
    print("How are you")
```

The function definition has the following parts

* The <strong>def</strong> keyword signifies we are defining a function
* The name of the function being defined - `print_greeting`
* The parameters in parentheses - `name`
* The function <strong>body</strong>
@@@

###Function returns

A function can also **return** a value

```
def plus_5(x):
    return x + 5

y = plus_5(4)
```

* Allows for calling a function for a value (rather than printing)
* No return? -> Returns the value *None*

Notes: substitution method
@@@

###Functions with no arguments

A function does not have to take arguments, as in the following example:

```python
def newline():
    print('')

newline()
# prints an empty line. None is returned
```

This is useful when the function is intended to always do the same thing
@@@

###Scope

The **scope** of a variable is the area of code where it is valid

Variables defined within a function can not be used elsewhere.

```python
def get_average(a, b):
    total = a + b
    return total / 2.0

avg = get_average(10, 20)
```

Note: Draw a diagram with bubbles
@@@

###Let's Develop It

* Create some functions that draw shapes with a turtle

[http://www.skulpt.org/](http://www.skulpt.org/)

```
# Put this at the top
import turtle

tina = turtle.Turtle()

forward = lambda n: tina.forward(n)
left = lambda n: tina.left(n)
right = lambda n: tina.right(n)
```

@@@

###Example

```
def draw_square():
    forward(30)
    right(90)
    forward(30)
    right(90)
    forward(30)
    right(90)
    forward(30)
    right(90)

draw_square()
```
@@@

###Questions?
