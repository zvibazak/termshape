# -*- coding: utf8 -*-

"""Termshape

Termshape is a minimalistic Python package, that only prints basic
shapes on terminal. It does not have any dependencies.
"""

__author__ = "zvibazak"
__version__ = "0.0.2"
__license__ = "MIT"

DEFAULT_CHARACTER = '*'

def plot(canvas):
    """Plots a 2d canvas, using `canvas` as a 2d array."""
    
    res = ''
    for row in [' '.join(row) for row in canvas]:
        res += row + '\n'
    return res


def make_shape(list_x, list_y, eqs, ch=DEFAULT_CHARACTER):
    """Creates a shape using `list_x` and `list_y`, the current
    character is only placed if one of the expressions in `eqs` is
    true, `ch` is the character used to create the shape.
    """
    
    canvas = [[' ' for _ in list_x] for _ in list_y]

    # calc min_x, min_y for range with negative values
    min_x = abs(min(list_x))
    min_y = abs(min(list_y))
    
    for x in list_x:
        index_x = x+min_x
        for y in list_y:
            index_y = len(list_y) - (y+min_y) - 1
          
            for eq in eqs:
                if eval(eq):
                    canvas[index_y][index_x] = ch

    return plot(canvas)


def get_square(size, ch=DEFAULT_CHARACTER):
    """Creates a square of `size`, using `ch` as the character to
    creates the shape.
    """
    
    return get_rectangle(size, size, ch)
    
    
def get_rectangle(width, height, ch=DEFAULT_CHARACTER):
    """Creates a rectangle of `width` and `height`, using `ch` as
    the character to creates the shape.
    """
    
    x = range(width)
    y = range(height)

    eq = ["x==0",
          "x=="+str(width-1),
          "y==0",
          "y=="+str(height-1)
         ]

    return make_shape(x, y, eq, ch)


def get_triangular(height, ch=DEFAULT_CHARACTER):
    """Creates a triangle of `height`, using `ch` as the character to
    creates the shape.
    """
    
    x = y = range(height)

    eq = ["x==0",
          "x=="+str(height)+"-y-1",
          "y==0"
         ]

    return make_shape(x, y, eq, ch)


def get_circle(radius, fpercent=0.05, ch=DEFAULT_CHARACTER):
    """Creates a circle of `radius`, using a fill percentage
    `fpercent`, using `ch` as the character to creates the shape.
    """
    
    size = radius + 1
    x = y = range(-size, size)

    # TODO calc best t
    eq = ["x**2 + y**2 >"
          + str(radius**2 - fpercent*(radius**2))
          + " and x**2 + y**2 <"
          + str(radius**2 + fpercent*(radius**2))
         ]

    return make_shape(x, y, eq, ch)
