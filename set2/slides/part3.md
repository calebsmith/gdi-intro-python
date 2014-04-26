![Girl Develop It Logo](../images/gdi_logo_badge.png)

###Intro to Python
####Section 3
@@@

###Review

* Conditionals - if, elif, else
* Loops - while, for
* Functions - calls, definitions, arguments, return

Note: Block 1 - 25 Minutes
@@@


###What we will cover today

* More functions
* Method calls
* Lists and dictionaries
* Python built-in funtions

@@@

###More with Functions
Functions can also call other functions

One can use this to break up tasks into small piece that rely on others to do their work

```python
def get_tip(bill_amount):
    return bill_amount * 0.20  # 20% tip for good service

def get_tax(subtotal):
    return subtotal * 0.0675  # 6.75% in Orange County, NC

def print_receipt(subtotal):
    tax = get_tax(subtotal)
    bill_amount = subtotal + tax
    tip = get_tip(bill_amount)
    total = bill_amount + tip

    print "Subtotal: $" + str(subtotal)
    print "Tax at " + str(orange_county_tax_rate * 100) + "%: $" + str(tax)
    print "Tip at " + str(tip_for_good_service * 100) + "%: $" + str(tip)
    print "Grand Total: $" + str(total)
```

@@@

###Function Composition
**Function composition** is when the output of one funtion serves as the input of another

```python
def increase(x):
    return x + 1

def decrease(x):
    return x - 1

def double(x):
    return 2 * x

print double(increase(5))
# 12

# This is the same as...
x = 5
y = increase(x)
print double(y)
# 12

print double(decrease(5))
# 8
print increase(decrease(5))
# 5
print double(double(5)):
# 20
```

@@@


###Method Calls

A **method** is like a function but it is "bound" to an object.

For example, the integers and strings we've been using have methods attached to them

We can use the dir() function to see the methods of an object and help() to see what they do.

```python
>>> sentence = 'the quick brown fox did the thing with the other thing'
>>> print dir(sentence)
# Lots of output
>>> print sentence.capitalize()
'The quick brown fox did the thing with the other thing'
>>> print sentence.count('the')
4
>>> help(sentence.upper)
# Lots of output
```
@@@

###Let's Develop It

Open a Python shell and define a string varaible

Use 'dir(string_variable)' and the help() function to explore the various methods

Hint: Like functions, some methods take arguments and others don't

Hint: Use help(varname.methodname) on a method. It will tell you the arguments to use and the expected behavior

Hint: Don't be afraid of errors. They are there to help you so read them carefully.

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

In Python, a list is defined using `[ ]` with elements separated by commas, as in the following example

```python
words = ['list', 'of', 'strings']
```

A list can, but doesn't have to be of all one type. A list of one type is **homogenous** as opposed to a list of multiple types, which is **heterogeneous**.

```python
# heterogenous list
words = [0, 'list', 'of', 3, 'strings', 'and', 'numbers']
```
Note: Block 2 - 30 Minutes
@@@

###List Methods

Lists have several methods, the most useful of which is `append`
A list can be created as an empty list and have values added to it with `append`
```python
>>> to_dos = []
>>> to_dos.append('buy soy milk')
>>> to_dos.append('install git')
>>> print to_dos
['buy soy milk', 'install git']
```

Therefore, lists are **mutable**

This means that a list can change values during the duration of a program
@@@


###Iteration

Lists and many other collections are **iterable**.

Once defined, we can iterate on them, performing an action with each element

```python
shipping_cost = 2.5
prices = [3, 4, 5.25]

costs = []
for price in prices:
    costs.append(price + shipping_cost)

for cost in costs:
    print cost

# Output
# 5.5
# 6.5
# 7.75
```
@@@


###Indexing

An element can also be obtained from a list through **indexing**

This allows us to obtain an element without iterating through the entire collection if we just want one value.

To index on a collection, follow it immediately with `[index]`. (index here is a number, variable or expression)

```python
>>> numbers = [10, 20, 30]
>>> print numbers[0]
10
```
@@@

###Indexing continued

Lists and other collections in Python are <strong>zero indexed</strong>. This means that the number 0 refers to first element in the list.

```python
>>> to_dos = ['install git', 'read email', 'make lunch']
>>> print to_dos[0]
'install git'
>>> print to_dos[1]
'read email'
>>> print to_dos[-1]
'make lunch'
```

Negative numbers mean "go back from the end this many". e.g. -1 is the last element, -2 is the penultimate

An IndexError results if an index is too high or low for the number of elements
@@@


###Dictionaries

A **dictionary** (sometimes called a "hashmap") is a collection of key/value pairs, defined with `{}`

```python
menu_categories = {
    'food': 'stuff you eat',
    'beverage': 'stuff you drink',
}
```

Think of words in a dictionary. The words are keys and the definitions are values.

This dictionary would be indexed with strings such as 'food' and 'beverage' instead of integers like in a list
@@@


###Indexing on Dictionaries

Dictionaries aren't literally for definitions. They represent a group of mappings. A mapping might be: menu items -> costs.

We can also index on dictionaries.

The most common indexes are strings, but this is not a hard requirement.

```python
menu = {
    'tofu': 4,
}

tofu_cost = menu['tofu']
# the tofu_cost variable is now equal to 4.
```

Indexing on a key that doesn't exist results in a KeyError

If you aren't certain a key is present, you can use the 'get' method...
@@@


###Dictionary Methods

Some of the most essential methods are *keys*, *values* and *items*

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

If a key isn't present, the get method will return a default value if provided, otherwise None
@@@

###The in operator

The `in` operator is used to determine if an element is in a given collection

For dictionaries, the keys are searched for the element.

```python
>>> color = (255, 255, 0)
>>> print(1 in color)
False

>>> menu = {'tofu': 4}
>>> print('tofu' in menu)
True
```
@@@

###Let's Develop It
* Improve our adventure game by adding a player inventory. The player should
 gain items they walk on them and they should be removed from the board.

* The beginning of this program has been started and is available here as
[game3.py](http://calebsmith.github.io/gdi-intro-python/examples/game3.py)

* You'll also need to download the board.dat file to the same folder.
 [board.dat](http://calebsmith.github.io/gdi-intro-python/examples/board.dat)

* If you are stuck ask the teacher or a TA for help.

Note: Let's Develop It 30 minutes
@@@

###Tuples

**Tuples** are like lists, but they are **immutable**. They are particularly good at storing collections of a fixed and predictable size. Use `()` to define tuples

An x, y coordinate pair, or the RGB values of a color are good candidates for tuples.

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
**Sets** are unordered collections whose elements are unique. Therefore, adding a value to a set that already has it, does nothing.

Sets can be created with comma separated elements enclosed in `{}` in Python 2.7 or greater. Very often, one will make a list and use the set() function

Sets have an *add* method, which like append for lists, adds an element to a set.

```python
>>> set_a = set([0, 3, 7])
>>> set_b = set([0, 4, 7])
>>> set_a.add(4)
>>> print(set_a)
set([0, 3, 4, 7])
>>> print(set_a.intersection(set_b))
set([0, 4, 7])
```

Sets have nice methods for reasoning about their relationship to other sets. (Think Venn Diagram)
@@@

###Lists of ... Lists

Lists can contain not only numbers or strings, but also other lists.

Such a structure is said to be  <strong>nested</strong>

The following is a list of lists:

This can be indexed successively.

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


###Nested Lists continued

A list can be appended to a list as well

```python
mary_to_dos = ['eat', 'work', 'pick up laundry', 'care for baby', 'sleep']
fran_to_dos = ['eat', 'work', 'call plumber', 'sleep']
baby_to_dos = ['eat', 'sleep']
all_to_dos = []
all_to_dos.append(mary_to_dos)
all_to_dos.append(fran_to_dos)
all_to_dos.append(baby_to_dos)
print(all_to_dos)

for to_dos in all_to_dos:
    for to_do in to_dos:
        print(to_do)
```
If we want to <strong>flatten</strong> the to do's into one list, use **extend**

What if we want the to do's to be unique?
@@@


###Lists of Dictionaries

One of the most common and useful nested data structures, is a list of dictionaries

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

A dictionary can also contain values that are themselves other collections, such as lists.

Let's revisit the group of to do lists and find a better representation:

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

Now the to do lists can be indexed or modified by name

@@@


###Means of Combination

Lists, dictionaries, sets, tuples, and other collections are all a means of combination.

They can be freely combined to create the data structure needed for a particular problem

Eg. A list of dictionaries with lists

```python
all_tweets = [
    {
        'author': 'mary',
        'handle': '@hadalittlelamb',
        'date': '2013-01-22',
        'tweets': [
            'at Loco Pops enjoying a Raspberry Sage popsicle',
            'Learning Python is so much fun',
            'Running late to Code and Coffee. #overslept',
        ],
    },
]
```
@@@

###Let's Develop It
* Improve our adventure game by allowing a player with a key to pass through a
 door

* The beginning of this program has been started and is available here as
[game4.py](http://calebsmith.github.io/gdi-intro-python/examples/game4.py)

* You'll also need to download the board.dat file to the same folder.
 [board.dat](http://calebsmith.github.io/gdi-intro-python/examples/board.dat)

* If you are stuck ask the teacher or a TA for help.

Note: Let's Develop It 30 minutes
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
>>> print(len([1, 2]))
2
# range() - Quickly creates a list of integers
>>> print(range(5))
[0, 1, 2, 3, 4]
>>> print(range(5, 10))
[5, 6, 7, 8, 9]
>>> print(range(0, 10, 2))
[0, 2, 4, 6, 8]
>>> print(range(9, 4, -1))
[9, 8, 7, 6, 5]
# sorted() - Sort a given list
>>> grades = sorted([93, 100, 60])
>>> print(grades)
[60, 93, 100]
```

@@@

###Builtins Examples continued

```python
# enumerate() - Obtain the index and each element in a collection
>>> to_dos = ['work', 'sleep', 'work']
>>> print(list(enumerate(to_dos))
[(0, 'work'), (1, 'sleep'), (2, 'work')]
>>> for index, item in enumerate(to_dos):
...     print(index, item)
(0, 'work')
(1, 'sleep')
(2, 'work')
# zip()
>>> widths = [10, 15, 20]
>>> heights = [5, 8, 12]
>>> print(zip(widths, heights))
[(10, 5), (15, 8), (20, 12)]
>>> for width, height in zip(widths, heights):
...     print('Area is ', width * height)
('Area is ', 50)
('Area is ', 120)
('Area is ', 240)
```

Note:  Let's develop it: 25 minutes
@@@

###Let's Develop It
* Complete our game by allowing you to pick up a sword, battle a dragon and
 obtain the treasure. If the player has no sword, the dragon wins, otherwise
 the player wins. When the player obtains the gold, they have beaten the game

* The beginning of this program has been started and is available here as
[game5.py](http://calebsmith.github.io/gdi-intro-python/examples/game5.py)

* You'll also need to download the board.dat file to the same folder.
 [board.dat](http://calebsmith.github.io/gdi-intro-python/examples/board.dat)

* If you are stuck ask the teacher or a TA for help.

Note: Let's Develop It 30 minutes
@@@

###Questions?
