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
```

@@@

```
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

###Future Resources

<table>
    <tr>
        <td>[Python.org Documentation](http://docs.python.org/2/)</td>
        <td>Official Python Documentation</td>
    </tr>
    <tr>
        <td>[Think Python Interactive](http://interactivepython.org/courselib/static/thinkcspy/index.html)</td>
        <td>Online Book with Live Code Runner</td>
    </tr>
    <tr>
        <td>[Dive Into Python](http://www.diveintopython.net/toc/index.html)</td>
        <td>Online and print book with exercises.</td>
    </tr>
    <tr>
        <td>[Learn Python the Hard Way](http://learnpythonthehardway.org/book/)</td>
        <td>Online and print book with exercises</td>
    </tr>
    <tr>
        <td>[Google's Python Class](https://developers.google.com/edu/python/)</td>
        <td>Video lectures coupled with exercises</td>
    </tr>
    <tr>
        <td>[New Coder](http://newcoder.io/tutorials/)</td>
        <td>Ideas for larger projects and resources.</td>
    </tr>
    <tr>
        <td>[Girl Develop It](http://girldevelopit.com/)</td>
        <td>Local workshops, events, and coding sessions</td>
    </tr>
</table>
@@@


###Let's Develop It

* Write some list processing code to examine some civic data from Code For Durham
[https://github.com/codefordurham/Durham-Data](https://github.com/codefordurham/Durham-Data)

Use this exampe [http://repl.it/rVS](http://repl.it/rVS)

@@@

### Example queries

* How many establishments are locally owned?
* How many have a street address listed
* How many opened more than 5 years ago? (more advanced. Lookup datetime module)

```
import datetime

datetime.datetime.strptime(datetime_string, "%Y-%m-%d %H:%M:%S")
```

Note:
[{'Closing_Date': '17-FEB-2010',
'County': '32',
'Emergency_Number': '0',
'Hours_Of_Operation': '0',
'Lat': '35.936793999999999',
'Local_Yn': 'NO',
'Lon': '-78.883798999999996',
'Opening_Date': '2008-01-23 00:00:00',
'Premise_Address1': '3415 S. ALSTON AVE',
'Premise_Address2': '0',
'Premise_City': 'DURHAM',
'Premise_Email': '0',
'Premise_Fax': '(919) 806-2280',
'Premise_Name': 'SCARBOROUGH NEWTON DAY CARE AC',
'Premise_Phone': '(919) 237-2936',
'Premise_State': 'NC',
'Premise_Zip': '27713',
'Risk': '0',
'Seats': '0',
'Smoking_Allowed': 'N/A',
'Status': 'DELETED',
'Website': '0'},
{'Closing_Date': '0',
'County': '32',
'Emergency_Number': '(770) 329-3149',
'Hours_Of_Operation': '0',
'Lat': '36.084066',
'Local_Yn': 'NO',
'Lon': '-78.910973999999996',
'Opening_Date': '2013-06-03 00:00:00',
'Premise_Address1': '3820 N ROXBORO ROAD',
'Premise_Address2': '0',
'Premise_City': 'DURHAM',
'Premise_Email': 'charlesctaylor@hotmail.com',
'Premise_Fax': '(919) 237-2800',
'Premise_Name': "ZAXBY'S",
'Premise_Phone': '(919) 251-9650',
'Premise_State': 'NC',
'Premise_Zip': '27704',
'Risk': '3',
'Seats': '66',
'Smoking_Allowed': 'N/A',
'Status': 'ACTIVE',
'Website': '0'},
{'Closing_Date': '31-DEC-2011',
'County': '32',
'Emergency_Number': '0',
'Hours_Of_Operation': '0',
'Lat': '35.985455999999999',
'Local_Yn': 'NO',
'Lon': '-78.86994',
'Opening_Date': '2010-06-21 00:00:00',
'Premise_Address1': '2618 HARVARD AVE.',
'Premise_Address2': '0',
'Premise_City': 'DURHAM',
'Premise_Email': '0',
'Premise_Fax': '0',
'Premise_Name': 'GREATER NEW BIRTH',
'Premise_Phone': '0',
'Premise_State': 'NC',
'Premise_Zip': '27703',
'Risk': '0',
'Seats': '0',
'Smoking_Allowed': 'N/A',
'Status': 'DELETED',
'Website': '0'},
{'Closing_Date': '19-JUL-1995',
'County': '32',
'Emergency_Number': '0',
'Hours_Of_Operation': '0',
'Lat': '35.987189999999998',
'Local_Yn': 'NO',
'Lon': '-78.926501999999999',
'Opening_Date': '1990-07-01 00:00:00',
'Premise_Address1': '2000 CHAPEL HILL ROAD',
'Premise_Address2': '0',
'Premise_City': 'DURHAM',
'Premise_Email': '0',
'Premise_Fax': '0',
'Premise_Name': 'STEAK OUT',
'Premise_Phone': '0',
'Premise_State': 'NC',
'Premise_Zip': '27707',
'Risk': '4',
'Seats': '0',
'Smoking_Allowed': 'N/A',
'Status': 'DELETED',
'Website': '0'},
{'Closing_Date': '09-DEC-2013',
'County': '32',
'Emergency_Number': '0',
'Hours_Of_Operation': '0',
'Lat': '35.996704000000001',
'Local_Yn': 'NO',
'Lon': '-78.915999999999997',
'Opening_Date': '2000-07-31 00:00:00',
'Premise_Address1': '1121 CHAPEL HILL ST',
'Premise_Address2': '0',
'Premise_City': 'DURHAM',
'Premise_Email': '0',
'Premise_Fax': '(919) 401-6654',
'Premise_Name': 'ALL MY CHILDREN CHILD CARE CTR',
'Premise_Phone': '(919) 401-6654',
'Premise_State': 'NC',
'Premise_Zip': '27701',
'Risk': '0',
'Seats': '0',
'Smoking_Allowed': 'N/A',
'Status': 'DELETED',
'Website': '0'},
{'Closing_Date': '15-APR-1997',
'County': '32',
'Emergency_Number': '0',
'Hours_Of_Operation': '0',
'Lat': '35.997864999999997',
'Local_Yn': 'NO',
'Lon': '-78.914809000000005',
'Opening_Date': '1997-02-17 00:00:00',
'Premise_Address1': '1106 W CHAPEL HILL RD',
'Premise_Address2': '0',
'Premise_City': 'DURHAM',
'Premise_Email': '0',
'Premise_Fax': '0',
'Premise_Name': 'MCCLAINS CATERING',
'Premise_Phone': '0',
'Premise_State': 'NC',
'Premise_Zip': '27705',
'Risk': '4',
'Seats': '0',
'Smoking_Allowed': 'N/A',
'Status': 'DELETED',
'Website': '0'},
{'Closing_Date': '0',
'County': '32',
'Emergency_Number': '0',
'Hours_Of_Operation': '0',
'Lat': '35.935673999999999',
'Local_Yn': 'NO',
'Lon': '-78.933695',
'Opening_Date': '1994-07-27 00:00:00',
'Premise_Address1': '4818 S ROXBORO ST',
'Premise_Address2': '0',
'Premise_City': 'DURHAM',
'Premise_Email': '0',
'Premise_Fax': '0',
'Premise_Name': 'HOPE VALLEY FARMS SWIM AND RACQUET',
'Premise_Phone': '0',
'Premise_State': 'NC',
'Premise_Zip': '27713',
'Risk': '0',
'Seats': '0',
'Smoking_Allowed': 'N/A',
'Status': 'ACTIVE',
'Website': '0'},
{'Closing_Date': '30-JUN-2000',
'County': '32',
'Emergency_Number': '0',
'Hours_Of_Operation': '0',
'Lat': '36.057966999999998',
'Local_Yn': 'NO',
'Lon': '-78.929029',
'Opening_Date': '1994-12-12 00:00:00',
'Premise_Address1': '3808 GUESS ROAD',
'Premise_Address2': '0',
'Premise_City': 'DURHAM',
'Premise_Email': '0',
'Premise_Fax': '0',
'Premise_Name': 'FOOD LION DELI 420',
'Premise_Phone': '0',
'Premise_State': 'NC',
'Premise_Zip': '27705',
'Risk': '4',
'Seats': '0',
'Smoking_Allowed': 'N/A',
'Status': 'DELETED',
'Website': '0'},
{'Closing_Date': '13-SEP-2010',
'County': '32',
'Emergency_Number': '0',
'Hours_Of_Operation': '0',
'Lat': '36.093411000000003',
'Local_Yn': 'NO',
'Lon': '-78.900698000000006',
'Opening_Date': '1990-07-01 00:00:00',
'Premise_Address1': '3101 PETTY ROAD SUITE 1700',
'Premise_Address2': '0',
'Premise_City': 'DURHAM',
'Premise_Email': '0',
'Premise_Fax': '0',
'Premise_Name': 'UNIVERSITY CLUB',
'Premise_Phone': '0',
'Premise_State': 'NC',
'Premise_Zip': '27707',
'Risk': '4',
'Seats': '120',
'Smoking_Allowed': 'N/A',
'Status': 'DELETED',
'Website': '0'},
{'Closing_Date': '0',
'County': '32',
'Emergency_Number': '0',
'Hours_Of_Operation': '0',
'Lat': '36.092751',
'Local_Yn': 'NO',
'Lon': '-78.911361999999997',
'Opening_Date': '2003-10-21 00:00:00',
'Premise_Address1': '5600 N ROXBORO RD',
'Premise_Address2': '0',
'Premise_City': 'DURHAM',
'Premise_Email': '0',
'Premise_Fax': '0',
'Premise_Name': 'ENO POINTE ASSISTED LIVING',
'Premise_Phone': '0',
'Premise_State': 'NC',
'Premise_Zip': '27704',
'Risk': '1',
'Seats': '0',
'Smoking_Allowed': 'NO',
'Status': 'ACTIVE',
'Website': '0'},
{'Closing_Date': '31-DEC-2008',
'County': '32',
'Emergency_Number': '0',
'Hours_Of_Operation': '0',
'Lat': '35.981825000000001',
'Local_Yn': 'NO',
'Lon': '-78.922820000000002',
'Opening_Date': '2008-08-27 00:00:00',
'Premise_Address1': 'WALLACE WADE STADIUM',
'Premise_Address2': 'DUKE UNIVERSITY',
'Premise_City': 'DURHAM',
'Premise_Email': '0',
'Premise_Fax': '0',
'Premise_Name': 'BLUE DEVIL CONCESSIONS STAND #6',
'Premise_Phone': '0',
'Premise_State': 'NC',
'Premise_Zip': '27708',
'Risk': '2',
'Seats': '0',
'Smoking_Allowed': 'N/A',
'Status': 'DELETED',
'Website': '0'},
{'Closing_Date': '31-MAY-2011',
'County': '32',
'Emergency_Number': '0',
'Hours_Of_Operation': '0',
'Lat': '36.085065999999998',
'Local_Yn': 'NO',
'Lon': '-78.909974000000005',
'Opening_Date': '2000-01-03 00:00:00',
'Premise_Address1': '2201 N ROXBORO ROAD',
'Premise_Address2': '0',
'Premise_City': 'DURHAM',
'Premise_Email': '0',
'Premise_Fax': '0',
'Premise_Name': 'MI PEQUENO HONDURAS',
'Premise_Phone': '0',
'Premise_State': 'NC',
'Premise_Zip': '27704',
'Risk': '4',
'Seats': '54',
'Smoking_Allowed': 'N/A',
'Status': 'DELETED',
'Website': '0'},
{'Closing_Date': '09-FEB-2000',
'County': '32',
'Emergency_Number': '0',
'Hours_Of_Operation': '0',
'Lat': '36.030867999999998',
'Local_Yn': 'NO',
'Lon': '-78.831056000000004',
'Opening_Date': '1990-07-01 00:00:00',
'Premise_Address1': 'P.O. BOX 12168, RTP',
'Premise_Address2': '0',
'Premise_City': 'RTP',
'Premise_Email': '0',
'Premise_Fax': '0',
'Premise_Name': "RADISSON GOVERNOR'S INN",
'Premise_Phone': '0',
'Premise_State': 'NC',
'Premise_Zip': '27709',
'Risk': '0',
'Seats': '0',
'Smoking_Allowed': 'N/A',
'Status': 'DELETED',
'Website': '0'},
{'Closing_Date': '0',
'County': '32',
'Emergency_Number': '0',
'Hours_Of_Operation': '0',
'Lat': '35.954732',
'Local_Yn': 'NO',
'Lon': '-78.993808999999999',
'Opening_Date': '2007-10-18 00:00:00',
'Premise_Address1': '5318 NEW HOPE COMMONS EXT',
'Premise_Address2': 'STE 200',
'Premise_City': 'DURHAM',
'Premise_Email': '0',
'Premise_Fax': '0',
'Premise_Name': 'PAPA JOHNS',
'Premise_Phone': '0',
'Premise_State': 'NC',
'Premise_Zip': '27707',
'Risk': '2',
'Seats': '0',
'Smoking_Allowed': 'N/A',
'Status': 'ACTIVE',
'Website': '0'},
{'Closing_Date': '24-MAY-2007',
'County': '32',
'Emergency_Number': '0',
'Hours_Of_Operation': '0',
'Lat': '35.910961999999998',
'Local_Yn': 'NO',
'Lon': '-78.937600000000003',
'Opening_Date': '2000-07-10 00:00:00',
'Premise_Address1': '211 WEST HWY 54',
'Premise_Address2': '0',
'Premise_City': 'DURHAM',
'Premise_Email': '0',
'Premise_Fax': '0',
'Premise_Name': 'EL INCA CAFE',
'Premise_Phone': '0',
'Premise_State': 'NC',
'Premise_Zip': '27713',
'Risk': '4',
'Seats': '0',
'Smoking_Allowed': 'N/A',
'Status': 'DELETED',
'Website': '0'},
{'Closing_Date': '0',
'County': '32',
'Emergency_Number': '0',
'Hours_Of_Operation': '0',
'Lat': '35.967227000000001',
'Local_Yn': 'NO',
'Lon': '-78.945802',
'Opening_Date': '2005-01-10 00:00:00',
'Premise_Address1': '4037 CHAPEL HILL BLVD',
'Premise_Address2': '0',
'Premise_City': 'DURHAM',
'Premise_Email': '0',
'Premise_Fax': '0',
'Premise_Name': 'TARGET FOOD AVE T1872',
'Premise_Phone': '0',
'Premise_State': 'NC',
'Premise_Zip': '27707',
'Risk': '2',
'Seats': '46',
'Smoking_Allowed': 'N/A',
'Status': 'ACTIVE',
'Website': '0'},
{'Closing_Date': '30-MAR-2011',
'County': '32',
'Emergency_Number': '0',
'Hours_Of_Operation': '0',
'Lat': '36.014111',
'Local_Yn': 'NO',
'Lon': '-78.889160000000004',
'Opening_Date': '2011-03-17 00:00:00',
'Premise_Address1': '2000 AVONDALE DR',
'Premise_Address2': '0',
'Premise_City': 'DURHAM',
'Premise_Email': '0',
'Premise_Fax': '0',
'Premise_Name': 'DURHAM PLAZA CARNIVAL',
'Premise_Phone': '(973) 476-4439',
'Premise_State': 'NC',
'Premise_Zip': '27704',
'Risk': '0',
'Seats': '0',
'Smoking_Allowed': 'N/A',
'Status': 'DELETED',
'Website': '0'},
{'Closing_Date': '0',
'County': '32',
'Emergency_Number': '0',
'Hours_Of_Operation': '0',
'Lat': '35.920237999999998',
'Local_Yn': 'NO',
'Lon': '-78.927933999999993',
'Opening_Date': '1996-01-30 00:00:00',
'Premise_Address1': '5800 TATTERSALL',
'Premise_Address2': '0',
'Premise_City': 'DURHAM',
'Premise_Email': '0',
'Premise_Fax': '0',
'Premise_Name': 'INNESBROOK APTS',
'Premise_Phone': '0',
'Premise_State': 'NC',
'Premise_Zip': '27713',
'Risk': '0',
'Seats': '0',
'Smoking_Allowed': 'N/A',
'Status': 'ACTIVE',
'Website': '0'},
{'Closing_Date': '30-JUN-2000',
'County': '32',
'Emergency_Number': '0',
'Hours_Of_Operation': '0',
'Lat': '35.900207999999999',
'Local_Yn': 'NO',
'Lon': '-78.898662000000002',
'Opening_Date': '1990-07-01 00:00:00',
'Premise_Address1': '1908 MEREDITH DR',
'Premise_Address2': '0',
'Premise_City': 'DURHAM',
'Premise_Email': '0',
'Premise_Fax': '0',
'Premise_Name': 'FOOD LION   885',
'Premise_Phone': '0',
'Premise_State': 'NC',
'Premise_Zip': '27713',
'Risk': '4',
'Seats': '0',
'Smoking_Allowed': 'N/A',
'Status': 'DELETED',
'Website': '0'},
{'Closing_Date': '27-JUN-2005',
'County': '32',
'Emergency_Number': '0',
'Hours_Of_Operation': '0',
'Lat': '35.939000999999998',
'Local_Yn': 'NO',
'Lon': '-78.935270000000003',
'Opening_Date': '1990-07-01 00:00:00',
'Premise_Address1': 'REGENCY PLAZA',
'Premise_Address2': '0',
'Premise_City': 'DURHAM',
'Premise_Email': '0',
'Premise_Fax': '0',
'Premise_Name': 'KROGER 314 STEAMED SEAFOOD',
'Premise_Phone': '0',
'Premise_State': 'NC',
'Premise_Zip': '27707',
'Risk': '4',
'Seats': '0',
'Smoking_Allowed': 'N/A',
'Status': 'DELETED',
'Website': '0'}
]

@@@

### For more data:

Download [http://calebsmith.github.io/gdi-intro-python/examples/durham_establishments.csv](http://calebsmith.github.io/gdi-intro-python/examples/durham_establishments.csv)

```
from csv import DictReader

data = list(DictReader(open('durham_establishments.csv')))
```

@@@

### Questions?
