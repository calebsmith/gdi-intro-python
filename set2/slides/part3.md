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
Funtions can also call other funtions

One an use this to break up tasks into small piece that rely on others to do their work

```python
from math import sqrt

def absolute_difference(value_a, value_b):
    return abs(value_a - value_b)

def find_width_height(x1, y1, x2, y2):
    width = absolute_difference(x1, x2)
    height = absolute_difference(y1, y2)
    return width, height

def get_hypotenuse(a, b):
    return sqrt(a ** 2 + b ** 2)

def get_area_rectangle(width, height):
    return width * height

def print_area_and_hypotenuse(x1, y1, x2, y2):
    width, height = find_width_height(x1, y1, x2, y2)
    area = get_area_rectangle(width, height)
    hypotenuse = get_hypotenuse(width, height)
    print 'Area of the rectangle is:'
    print area
    print 'The diagonal of the rectangle is:'
    print hypotenuse
```
@@@

###Function Composition
**Function composition** is when the output of one funtion ats as the input of another

```python
from math import sqrt

def find_width_height(x1, y1, x2, y2):
    return abs(x1 - x2), abs(y1 - y2)

def get_hypotenuse(a, b):
    return sqrt(a ** 2 + b ** 2)

def print_hypotenuse(x1, y1, x2, y2):
    print 'The diagonal of the rectangle is:'
    print get_hypotenuse(find_width_height(x1, y1, x2, y2))

# f(g(x))
# is the same as:
#     y = g(x)
#     f(y)
```

@@@


###Method Calls

A **method** is like a function but it is "bound" to an object.

For example, the integers and strings we've been using have methods attached to them

We can use the dir() function to see the methods of an object and help() to see what they do.
```python
a = 4
print dir(a)

name = 'caleb'
sentence = 'the quick brown fox did the thing with the thing'
print dir(name)

print name.capitalize()
print sentence.count('the')

help(name.upper)
```
@@@

###Let's Develop It

Open a Python shell and define a string varaible

Use 'dir(string_variable)' and the help() function to explore the various methods

Hint: Like functions, some methods take arguments and others don't

Hint: Use help() on a method. It will tell you the arguments to use and the expected behavior

Hint: Don't be afraid of errors. They seem to be in a foreign language but they are there to help you. Read them carefully.
```python
# Example
name = 'beth'
dir(name)
help(name.capitalize)
name = name.capitalize()
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
to_dos = []
to_dos.append('buy soy milk')
to_dos.append('install git')
print to_dos
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
```
@@@


###Indexing

An element can also be obtained from a list through **indexing**

This allows us to obtain an element without iterating through the entire collection if we just want one value.

To index on a collection, follow it immediately with `[index]`. (index here is a number, variable or expression)

```python
numbers = [10, 20, 30]
print numbers[0]
```
@@@

###Indexing continued

Lists and other collections in Python are <strong>zero indexed</strong>. This means that the number 0 refers to first element in the list.

```python
to_dos = [
    'install git', 'read email', 'make lunch',
]
print to_dos[0]
print to_dos[1]

print to_dos[-1]
```

Negative numbers mean "go back from the end this many". e.g. -1 is the last element, -2 is the penultimate

An IndexError results if an index exceeds the length of the list minus 1
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

Dictionaries aren't literally just for definitions. They represent a group of mappings. A mapping might be: menu items -> costs.

We can also index on dictionaries.

The most common indexes are strings, but they can be whatever type the keys are.

```python
menu = {
    'tofu': 4,
}

tofu_cost = menu['tofu']
```

Indexing on a key that doesn't exist results in a KeyError

If you aren't certain a key is present, you can use the 'get' method...
@@@


###Dictionary Methods

Some of the most essential methods are 'keys', 'values' and 'items'

```python
menu = {
    'tofu': 4,
    'pizza': 8,
    'baguette': 3,
}

print menu.keys()
print menu.values()
print menu.items()
print menu.get('pizza')
print menu.get('water')
print menu.get('juice', 5)
```

'get' will return None if the key isn't present or a default value if provided.
@@@


###Tuples

**Tuples** are like lists, but they are **immutable**. They are particularly good at storing collections of a fixed and predictable size. Use '()' to define tuples

An x, y coordinate pair, or the RGB values of a color are good candidates for tuples.

```python
point = (0, 1)
x = point_a[0]
y = point_a[1]

# or, even better

point = (0, 1)
x, y = point_a
```
@@@

###Tuple Example

Remember the geometry functions earlier? Some of these can be simplified using tuples

```python
def find_width_height(point_a, point_b):
    x_a, y_a = point_a
    x_b, y_b = point_b
    return abs(x_a - x_b), abs(y_a - y_b)

point_a = (5, 0)
point_b = (10, 4)
dimensions = find_width_height(point_a, point_b)
```

N.B. - In the example, the function returns a tuple. In the context of a return, or an assignment, the parenthesis around a tuple are not strictly required
@@@

###Sets
**Sets** are unordered collections whose elements are unique. Therefore, adding a value to a set that already has it, does nothing.

Sets can be created with comma separated elements enclosed in '{}' in Python 2.7 or greater. Very often, one will make a list and use the set() function

```python
set_a = set([0, 3, 7])
set_b = set([0, 4, 7])

# .add() is like .append() but for sets
print set_a.add(4)

# or in 2.7
set_a = {0, 3, 7} # and so on
```

Sets have nice methods for reasoning about their relationship to other sets. (Think Venn Diagram)
@@@


###The in operator

The `in` operator is used to determine if an element is in a given collection

For dictionaries, the keys are searched for the element.

```python
color = (255, 255, 0)
if 0 in color:
    print '0 is in the color'

menu = {'tofu': 4}
print 'tofu' in menu

names = ['Mary', 'Martha', 'George']
george_present = 'George' in names
```
