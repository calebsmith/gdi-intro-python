![Girl Develop It logo](../images/gdi_logo_badge.png)
###Intro to Python
####Class 4
@@@

###Review

* Method calls

* Combining lists and dictionaries

* Builtins for collections

@@@

###Functions on Dictionaries

```python
character = {
    'x': 10,
    'y': 20,
    'health': 100,
}

def injure(character, damage):
    character['health'] = character['health'] - damage
    if character['health'] < 0:
        character['health'] = 0

def heal(character, amount):
    character['health'] = character['health'] + amount
    if character['health'] > 100:
        character['health'] = 100
```
Note:  Block 1  - Intro to Classes and OOP - 20 minutes
@@@

###Classes
A **class** creates a new type of object.

A class defines the attributes and methods of objects of that type

Classes are used to create new objects of that type

```python
class Character():

    def __init__(self, x, y, health):
        self.x = x
        self.y = y
        self.health = health
character = Character(10, 20, 100)
```
@@@

###A Sense of Self
The first argument to every method is **self**.

self contains the attributes and methods for the current object

```python
class Character():

    def __init__(self, x, y, health):
        self.x = x
        self.y = y
        self.health = health
character = Character(10, 20, 100)
```
@@@

###The __init__ Method
This method defines what the class should do when creating a new object.

```python
class Character():
    def __init__(self, x, y, health):
        self.x = x
        self.y = y
        self.health = health
character_a = Character(10, 20, 100)
character_b = Character(10, 20, 100)
```
To create a new Character, the syntax looks like a function call. These arguments are passed to the __init__ method

@@@

###Defining Methods
A class also defines **methods**, which are functions that operate on objects of that type

Assigning values to an attribute on self is how we **mutate** the object's state.

```python
# inside the character class

    def heal(self, amount):
        self.health = self.health + amount
        if self.health > 100:
            self.health = 100

    def injure(self, amount):
        self.health = self.health - amount
        if self.health < 0:
           self.health = 0

character = Character(10, 20, 100)
character.injure(10)
```
@@@

###Let's Develop It
* Complete our game by allowing you to pick up a sword, battle a dragon and
 obtain the treasure. If the player has no sword, the dragon wins, otherwise
 the player wins. When the player obtains the gold, they have beaten the game

* The beginning of this program has been started and is available here as
[game6.py](http://calebsmith.github.io/gdi-intro-python/examples/game6.py)

* You'll also need to download the board.dat file to the same folder.
 [board.dat](http://calebsmith.github.io/gdi-intro-python/examples/board.dat)

* If you are stuck ask the teacher or a TA for help.

* The finished game will look something like this:
[game7.py](http://calebsmith.github.io/gdi-intro-python/examples/game7.py)

* If you have extra time, consider making the player into a class as well

Note: Let's Develop It 30 minutes
@@@

###Inheritance
A class can **inherit** from another class.

A class that inherits from another is called the "child class" and obtains the methods and attributes of its "parent"

```python
class Mobile(object):
    """
    An object with an x, y position, and methods for moving
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_up():
        self.y = self.y - 1
    # ... methods for move_down, move_left, and move_right
```
Note:  Block 2 - Inheritance and Composition 20 Minutes
@@@

###Inheritance Continued
The move_up method is **overridden** in the child class below:

```python
class BoundedMobile(Mobile):
    """
    An object with an x, y position, and methods for moving
    The x, y position must be within bounds
    """

    def move_up():
        self.y = self.y - 1
        if self.y < 0:
            self.y = 0
```
See [mobile.py](http://calebsmith.github.io/gdi-intro-python/examples/mobile.py) for a more complete example.

@@@

###What's Super about Super
**super** is often helpful when writing methods that override the method of the parent class

```python
class BoundedMobile(Mobile):
    """
    An object with an x, y position, and methods for moving
    The x, y position must be within bounds
    """

    def move_up():
        super(BoundedMobile, self).move_up()
        if self.y < 0:
            self.y = 0
```
The call to super() takes the name of the child class, followed by self. This is followed by the method call and any arguments to pass to it

@@@

###Composition
Classes can also use the technique of **composition**

This simply means that a given object contains other objects within it.

This often leads to a clearer and simpler design

```python
class Grid(object):

    def __init__(self, x_limit, y_limit):
        self.x_limit = x_limit
        self.y_limit = y_limit
        self.mobiles = []

    def add_mobile(self, x, y):
        mob = BoundedMobile(x, y, self.x_limit, self.y_limit)
        mobs = self.mobiles.get((x, y), [])
        mobs.append(mob)
        self.mobiles[(x, y)] = mobs
```
@@@

###Composition Continued
Given the class on the previous slide, the following code creates mobiles within the grid object. (Complete code is available in the aforementioned [mobile.py](http://calebsmith.github.io/gdi-intro-python/examples/mobile.py))

```python
from mobile import Grid

grid = Grid(7, 7)
grid.add_mobile(1, 2)
grid.add_mobile(0, 1)
grid.add_mobile(0, 1)
grid.display_grid()
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
        <td>Ideas for slightly larger projects and resources to get you started. Projects include accessing API's, scraping pages, writing IRC bots, and others.</td>
    </tr>
    <tr>
        <td>[Girl Develop It](http://girldevelopit.com/)</td>
        <td>Local workshops, events, and coding sessions</td>
    </tr>
</table>
@@@

###Questions?
