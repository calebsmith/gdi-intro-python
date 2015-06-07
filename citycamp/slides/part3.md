![Girl Develop It Logo](../images/gdi_logo_badge.png)

###Intro to Python
####Section 3
@@@

###This Session

* More with functions
* Methods
* Lists and dictionaries
* Python built-in funtions

@@@

###More with Functions
Functions can call other functions

[http://www.skulpt.org/](http://www.skulpt.org/)

```
import turtle

tina = turtle.Turtle()

forward = lambda n: tina.forward(n)
left = lambda n: tina.left(n)
right = lambda n: tina.right(n)
penup = lambda: tina.penup()
pendown = lambda: tina.pendown()

def draw_circle():
    angle = 0
    while angle < 360:
        right(1)
        forward(1)
        angle = angle + 1
```

@@@

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

def draw_all():
    draw_square()
    penup()
    forward(100)
    pendown()
    draw_circle()

draw_all()
```

@@@

###Method Calls

A **method** is like a function but it is "bound" to an object.

E.g. integers and strings have methods attached to them

N.B. - Use dir() and help()

```python
> sentence = 'the quick brown fox did the thing with the other thing'
> print(dir(sentence))
# Lots of output
> print(sentence.capitalize())
=> 'The quick brown fox did the thing with the other thing'
> print(sentence.count('the'))
=> 4
> help(sentence.upper)
# Lots of output
```
@@@

###Let's Develop It

Open a Python shell and define a string varaible

Use 'dir(variable)' and the help() function to explore the various methods

Hint: Like functions, some methods take arguments and others don't

```python
# Example
name = 'beth'
dir(name)
help(name.capitalize)
cap_name = name.capitalize()
```

Note: 5 minutes
@@@

###Lists

A list is an ordered collection of elements

Defined using `[ ]` with elements separated by commas

```python
words = ['list', 'of', 'strings']
```

* can be all one type, or a mix

```python
words = [0, 'list', 'of', 3, 'strings', 'and', 'numbers']
```
Note: Block 2 - 30 Minutes
@@@

###List Methods

Lists have several methods, most important is append
```python
> to_dos = []
> to_dos.append('buy soy milk')
> to_dos.append('install git')
> print(to_dos)
=> ['buy soy milk', 'install git']
```
@@@


###Iteration

Lists are **iterable**.

```python
shipping_cost = 2.5
prices = [3, 4, 5.25]

costs = []
for price in prices:
    costs.append(price + shipping_cost)

for cost in costs:
    print(cost)

# Output
# 5.5
# 6.5
# 7.75
```
@@@


###Indexing

An element can be obtained from a list through **indexing**

To index on a collection, follow it immediately with `[index]`. (index here is a number, variable or expression)

```python
> numbers = [10, 20, 30]
> print(numbers[0])
=> 10
```

N.B - Python is zero indexed
@@@

###Indexing continued

```python
> to_dos = ['install git', 'read email', 'make lunch']
> print(to_dos[0])
=> 'install python'
> print(to_dos[1])
=> 'read email'
> print(to_dos[-1])
=> 'make lunch'
```

Negative numbers mean "go back from the end this many".

An IndexError results if an index is out of bounds
@@@


###Dictionaries

A **dictionary** is a collection of key/value pairs, defined with `{}`

```python
menu_categories = {
    'food': 'stuff you eat',
    'beverage': 'stuff you drink',
}
```

Think of words in a dictionary. The words are keys and the definitions are values.

This dictionary is indexed with strings 'food' and 'beverage' instead of integers
@@@


###Indexing on Dictionaries

Dictionaries represent a group of mappings. A mapping might be: menu items -> costs.

The most common indexes are strings, but this is not a required.

```python
menu = {
    'tofu': 4,
}

tofu_cost = menu['tofu']
# the tofu_cost variable is now equal to 4.
```

Indexing on a key that doesn't exist results in a KeyError
@@@


###Dictionary Methods

Some of the most essential methods are *get*, *keys*, *values* and *items*

```python
menu = {
    'tofu': 4,
    'pizza': 8,
    'baguette': 3,
}

>>> print menu.get('pizza')
8
>>> print menu.get('donuts', 5)
5
>>> print menu.keys()
['tofu', 'pizza', 'baguette']
>>> print menu.values()
[4, 8, 3]
>>> print menu.items()
[('tofu', 4), ('pizza', 8), ('baguette', 3)]
```
@@@

###The in operator

The `in` operator checks if an element is in a collection

For dictionaries, the keys are searched.

```python
> names = ['Alice', 'Bob', 'George']
> print('Sally' in color)
=> False

> menu = {'tofu': 4}
> print('tofu' in menu)
=> True
```
@@@

###Tuples

* **Tuples** are like lists, but are **immutable**.

* Good at storing a fixed size. Use `()` to define tuples

* An x, y coordinate pair, or the RGB values of a color are good candidates for tuples.

```python
point = (0, 1)
x = point_a[0]
y = point_a[1]

# or, even better

point = (0, 1)
x, y = point_a
# x is 0, y is 1
```
@@@

###Sets
**Sets** are unordered and their elements are unique.

Sets can be created with comma separated elements enclosed in `{}`

```python
> set_a = {0, 3, 7}
> set_b = {0, 4, 7}
> set_a.add(4)
> print(set_a)
=> set([0, 3, 4, 7])
> print(set_a.intersection(set_b))
=> set([0, 4, 7])
```

Sets have nice methods for reasoning about their relationship to other sets. (Think Venn Diagram)
@@@

### Short Break

@@@

### Combining data

@@@

###Lists of ... Lists

Lists can contain other lists

Such a structure is <strong>nested</strong>

The following is a list of lists:

```python
game_board = [
    ['O', 'X', ' '],
    [' ', 'X', ' '],
    [' ', ' ', ' '],
]

print(game_board[0][1])
# outputs: 'X'
```

Note:  Block 3 20 minutes
@@@


###Lists of Dictionaries

One of the most common and useful nested data structures is a list of dictionaries

```python
card_a = {
    'suit': 'spades',
    'number': 4,
}
card_b = {
    'suit': 'hearts',
    'number': 8,
}
hand = [card_a, card_b]

print('The hand contains:')
for card in hand:
    print('A', card['number'], 'of', card['suit'])
```
@@@


###Dictionary of Lists

A dictionary can also contain values that are collections such as lists.

```python
mary_to_dos = ['eat', 'work', 'pick up laundry', 'care for baby', 'sleep']
fran_to_dos = ['eat', 'work', 'call plumber', 'sleep']
baby_to_dos = ['eat', 'sleep']
all_to_dos = {
    'mary': mary_to_dos,
    'fran': fran_to_dos,
    'baby': baby_to_dos,
}
for name, to_dos in all_to_dos.items():
    print(name, 'needs to: ', to_dos)
# Changing this later can be accomplished with
all_to_dos['baby'].append('cry')
```

The to do lists can be indexed or modified by name

@@@

###Means of Combination

Lists, dictionaries, sets, tuples, and other collections are all a means of combination.

They can be freely combined to create the data structure needed for a particular problem

Eg. A list of dictionaries with lists

```python
tweets = [
    {
        'author': 'mary',
        'handle': '@hadalittlelamb',
        'date': '2013-01-22',
        'tweets_bodies': [
            'at Loco Pops enjoying a Raspberry Sage popsicle',
            'Learning Python is so much fun',
            'Running late to Code and Coffee. #overslept',
        ],
    },
]
```
@@@

###Builtins for collections

Python provides several functions that help us work with these collections.

<table class="fragment">
    <tr>
        <td>len()</td>
        <td>Given a collection, return its length</td>
    </tr>
    <tr>
        <td>range()</td>
        <td>Create a list of integers in the range provided.</td>
    </tr>
    <tr>
        <td>sorted()</td>
        <td>Given a collection, returns a sorted copy of that collection</td>
    </tr>
    <tr>
        <td>enumerate()</td>
        <td>Returns a list of (index, element) from the list</td>
    </tr>
    <tr>
        <td>zip()</td>
        <td>Given one or more iterables, returns a list of tuples with an element from each iterable</td>
    </tr>
</table>
@@@


###Some Builtins

```python
# Using len() - Determines length
> print(len([1, 2]))
=> 2
# range() - Quickly creates a list of integers
> print(list(range(5)))
=> [0, 1, 2, 3, 4]
> print(list(range(5, 10)))
=> [5, 6, 7, 8, 9]
> print(list(range(0, 10, 2)))
=> [0, 2, 4, 6, 8]
> print(list(range(9, 4, -1)))
=> [9, 8, 7, 6, 5]
# sorted() - Sort a given list
> grades = sorted([93, 100, 60])
> print(grades)
=> [60, 93, 100]
```

@@@

###Builtins Examples continued

```python
# enumerate() - Obtain the index and each element in a collection
> to_dos = ['work', 'sleep', 'work']
> print(list(enumerate(to_dos))
=> [(0, 'work'), (1, 'sleep'), (2, 'work')]
> for index, item in enumerate(to_dos):
...     print(index, item)
=> (0, 'work')
=> (1, 'sleep')
=> (2, 'work')
# zip()
> widths = [10, 15, 20]
> heights = [5, 8, 12]
> print(zip(widths, heights))
=> [(10, 5), (15, 8), (20, 12)]
> for width, height in zip(widths, heights):
...     print('Area is ', width * height)
=> ('Area is ', 50)
=> ('Area is ', 120)
=> ('Area is ', 240)
```
@@@

###Let's Develop It

@@@

###Questions?
