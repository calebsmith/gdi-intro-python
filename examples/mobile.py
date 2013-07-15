#!/usr/bin/python
"""
Supplements class 4 material.

The classes in this module demonstrate a simple example of using inheritance
and composition
"""

from __future__ import print_function


class Mobile(object): 
    """
    An object with an x, y position, and methods for moving
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_up(self):
        self.y = self.y - 1

    def move_down(self):
        self.y = self.y + 1

    def move_left(self):
        self.x = self.x - 1

    def move_right(self):
        self.x = self.x + 1

    def __repr__(self):
        return "<Mobile at position (" + str(self.x) + "," + str(self.y) + ")>"


class BoundedMobile(Mobile):
    """
    An object with an x, y position, and methods for moving
    The x, y position must be within bounds

    N.B. This class inherits from Mobile and demonstrate how to override methods
    """

    def __init__(self, x, y, x_limit, y_limit):
        """
        Takes the arguments x, y, x_limit, and y_limit, where x and y represent
        the current position of the mobile, while x_limit and y_limit represent
        the upper bounds of the grid they reside on. (0, 0 is assumed as lower
        bounds).
        """
        self.x = x
        self.y = y
        self.x_limit = x_limit
        self.y_limit = y_limit

    def move_up(self):
        # call the move_up method from the parent class (Mobile)
        super(BoundedMobile, self).move_up()
        if self.y < 0:
            self.y = 0

    def move_down(self):
        # call the move_up method from the parent class (Mobile)
        super(BoundedMobile, self).move_down()
        if self.y > self.y_limit:
            self.y = self.y_limit

    def move_left(self):
        # call the move_up method from the parent class (Mobile)
        super(BoundedMobile, self).move_left()
        if self.x < 0:
            self.x = 0

    def move_right(self):
        # call the move_up method from the parent class (Mobile)
        super(BoundedMobile, self).move_right()
        if self.x > self.x_limit:
            self.x = self.x_limit


class Grid(object):
    """
    A grid represents a gameboard or other grid pattern that holds mobiles
    in each tile. Multiple mobiles can exist on the same tile.
    """

    def __init__(self, x_limit, y_limit):
        self.x_limit = x_limit
        self.y_limit = y_limit
        self.mobiles = {}

    def add_mobile(self, x, y):
        """
        Given x, y, create a BoundedMobile instance and place it in the x, y
        position in the grid
        """
        # Create a bounded mobile at the position x, y
        mob = BoundedMobile(x, y, self.x_limit, self.y_limit)
        # Obtain the list of mobiles in the position x, y
        mobs = self.mobiles.get((x, y), [])
        # Add the new mobile to that list of mobiles
        mobs.append(mob)
        self.mobiles[(x, y)] = mobs

    def display_mobiles(self):
        """
        Prints the number of mobiles at each position that's occupied
        """
        for (x, y), mobiles in self.mobiles.iteritems():
            print("Position " + str(x) + ", " + str(y) + " has " + str(len(mobiles)))

    def display_grid(self):
        """
        Prints a display of the grid with the number of mobiles in each position
        """
        for y in xrange(0, self.y_limit):
            print('-' * self.x_limit * 3 + 1)
            current_row = '|'
            for x in xrange(0, self.x_limit):
               num_mobiles_in_tile = len(self.mobiles.get((x, y), []))
               spacer = ' ' if num_mobiles_in_tile < 10 else ''
               display_value = spacer + str(num_mobiles_in_tile)
               current_row += display_value + '|'
            print(current_row)
        print('-' * self.x_limit * 3 + 1)

    def __repr__(self):
        return "<Grid with upper bounds (" + str(self.x_limit) + "," + str(self.y_limit) + ")>"

