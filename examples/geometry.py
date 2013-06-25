#!/usr/bin/python
"""
Suitable for hacking after class 2.

This program demostrates using some functions to solve geometric formulas.

It takes 4 arguments which are takens as two pairs of {x, y} coordinates.

The program outputs the area of a rectangle formed by those points as two of
its corners as well as the length of the line that intersects those two points
"""

import sys
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


if __name__ == '__main__':
    if len(sys.argv) == 5:
        x1, y1, x2, y2 = map(int, sys.argv[1:5])
        print_area_and_hypotenuse(x1, y1, x2, y2)
    else:
        print __doc__
        print ''
        print 'This program requires exactly 4 number arguments'

