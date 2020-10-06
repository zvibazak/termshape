# -*- coding: utf8 -*-

"""Termshape

Termshape is a minimalistic Python package, that only prints basic
shapes on terminal. It does not have any dependencies.
"""

__author__ = "zvibazak"
__version__ = "1.0.0"
__license__ = "MIT"

DEFAULT_CHARACTER = '*'
DEFAULT_BGCHARACTER = ' '

def validate_positive_params(*args):
    for arg in args: 
        if not isinstance(arg, int) or arg<=0:
            return False
    return True 

def plot(canvas):
    """Plots a 2d canvas, using `canvas` as a 2d array."""
    
    res = ''
    for row in [' '.join(row) for row in canvas]:
        res += row + '\n'
    return res


def make_shape(list_x, list_y, feqs, beqs, ch=DEFAULT_CHARACTER, bgc=DEFAULT_BGCHARACTER):
    """Creates a shape using `list_x` and `list_y`, the current
    character is only placed if ones of the expressions in `feqs` or
    `beqs` is true, if the expression is in `feqs`, the foreground
    character is placed, if the expression is in `beqs`, the background
    character is used, `ch` is the foreground character, and `bgc` is
    the background character.

    The `beqs` expression list is evaluated first.
    """
    
    canvas = [[' ' for _ in list_x] for _ in list_y]

    # calc min_x, min_y for range with negative values
    min_x = abs(min(list_x))
    min_y = abs(min(list_y))
    
    for x in list_x:
        index_x = x+min_x
        for y in list_y:
            index_y = len(list_y) - (y+min_y) - 1
          
            for eq in beqs:
                if eval(eq):
                    canvas[index_y][index_x] = bgc

            for eq in feqs:
                if eval(eq):
                    canvas[index_y][index_x] = ch

    return plot(canvas)


def get_square(size, ch=DEFAULT_CHARACTER, bgc=DEFAULT_BGCHARACTER):
    """Creates a square of `size`, using `ch` as the foreground
    character and `bgc` as the background character.
    """
    
    return get_rectangle(size, size, ch, bgc)
    
    
def get_rectangle(width, height, ch=DEFAULT_CHARACTER, bgc=DEFAULT_BGCHARACTER):
    """Creates a rectangle of `width` and `height`, using `ch` as the
    foreground character and `bgc` as the background character.
    """
    
    if not validate_positive_params(width, height):
        raise TypeError("Only positive integers are allowed")

    x = range(width)
    y = range(height)

    feqs = ["x==0",
            f"x=={width-1}",
            "y==0",
            f"y=={height-1}"
           ]

    beqs = ["x>0",
            f"x<{width-1}",
            "y>0",
            f"y<{height-1}"
           ]

    return make_shape(x, y, feqs, beqs, ch, bgc)


def get_triangular(height, ch=DEFAULT_CHARACTER, bgc=DEFAULT_BGCHARACTER):
    """Creates a triangle of `height`, using `ch` as the foreground
    character and `bgc` as the background character.
    """

    if not validate_positive_params(height):
        raise TypeError("Only positive integers are allowed")
    
    x = y = range(height)

    feqs = ["x==0",
            f"x=={height}-y-1",
            "y==0"
           ]

    beqs = [f"x<{height}-y-1"]

    return make_shape(x, y, feqs, beqs, ch, bgc)

def get_circle(radius, fpercent=0.05, ch=DEFAULT_CHARACTER, bgc=DEFAULT_BGCHARACTER):
    """Creates a circle of `radius`, using a fill percentage
    `fpercent`, using `ch` as the foreground character and `bgc` as
    the background character.
    """

    if not validate_positive_params(radius):
        raise TypeError("Only positive integers are allowed")

    size = radius + 1
    x = y = range(-size, size)

    feqs = [f"x**2 + y**2 > {radius**2 - fpercent * (radius**2)} and x**2 + y**2 < {radius**2 + fpercent * (radius**2)}"]

    beqs = [f"x**2 + y**2 < {radius**2 - fpercent * (radius**2)}"]

    return make_shape(x, y, feqs, beqs, ch, bgc)
