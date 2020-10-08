# -*- coding: utf8 -*-

"""Termshape

Termshape is a minimalistic Python package, that only prints basic
shapes on terminal. It does not have any dependencies.
"""

__author__  = "zvibazak"
__version__ = "1.1.0" 
__license__ = "MIT"

DEFAULT_CHARACTER = '*'
DEFAULT_BGCHARACTER = ' '

def _validate_positive_params(*args):
    for arg in args: 
        if not isinstance(arg, int) or arg <= 0:
            raise TypeError("Only positive integers are allowed")


def plot(canvas):
    """Plots a 2d canvas.
    
    Positional arguments:
        canvas - 2d array for the canvas.
    """
    
    res = ''
    for row in [' '.join(row) for row in canvas]:
        res += row + '\n'
    return res


def make_shape(list_x, list_y, feqs, beqs, *, fg=DEFAULT_CHARACTER, bg=DEFAULT_BGCHARACTER):
    """Creates a shape using expressions lists for foreground character-
    s and background characters.
    
    Positional arguments:
        list_x - array for x coordinates.
        list_y - array for y coordinates.
        feqs   - list of expressions for foreground characters.
        beqs   - list of expressions for background characters.

    Keyword arguments:
        fg - foreground character.
        bg - background character.

    Expressions lists:
        For each character, the expressions list of background charact-
        ers is evaluated, if ones results in true, the background char-
        acter is placed in the current position, the same thing for fo-
        reground characters, except that is placed the foreground char-
        acter.

        An expression can use the variables 'x' and 'y' for the current
        position.
    """
    
    canvas = [[' ' for _ in list_x] for _ in list_y]

    # calc min_x, min_y for range with negative values
    min_x = abs(min(list_x))
    min_y = abs(min(list_y))
    
    for x in list_x:
        index_x = x + min_x
        for y in list_y:
            index_y = len(list_y) - (y + min_y) - 1
          
            for eq in beqs:
                if eval(eq):
                    canvas[index_y][index_x] = bg

            for eq in feqs:
                if eval(eq):
                    canvas[index_y][index_x] = fg

    return plot(canvas)


def get_square(size, *, fg=DEFAULT_CHARACTER, bg=DEFAULT_BGCHARACTER):
    """Creates a square.

    Positional arguments:
        size - size of the square.

    Keyword arguments:
        fg - foreground character.
        bg - background character.
    """
    
    return get_rectangle(size, size, fg=fg, bg=bg)
    
    
def get_rectangle(width, height, *, fg=DEFAULT_CHARACTER, bg=DEFAULT_BGCHARACTER):
    """Creates a rectangle.

    Positional arguments:
        width  - width of the rectangle.
        height - height of the rectangle.

    Keyword arguments:
        fg - foreground character.
        bg - background character.
    """
    
    _validate_positive_params(width, height)

    width = int(width)
    height = int(height)

    x = range(width)
    y = range(height)

    feqs = {
        "x == 0",
        f"x == {width-1}",
        "y == 0",
        f"y == {height-1}"
    }

    beqs = {
        "x > 0",
        f"x < {width-1}",
        "y > 0",
        f"y < {height-1}"
    }

    return make_shape(x, y, feqs, beqs, fg=fg, bg=bg)


def get_triangular(height, *, fg=DEFAULT_CHARACTER, bg=DEFAULT_BGCHARACTER):
    """Creates a triangle.

    Positional arguments:
        height - height of the triangle.

    Keyword arguments:
        fg - foreground character.
        bg - background character.
    """

    _validate_positive_params(height)
    
    height = int(height)

    x = y = range(height)

    feqs = {
        "x == 0",
        f"x == {height}-y-1",
        "y == 0"
    }

    beqs = {
        f"x < {height}-y-1"
    }

    return make_shape(x, y, feqs, beqs, fg=fg, bg=bg)


def get_circle(radius, fpercent=5, *, fg=DEFAULT_CHARACTER, bg=DEFAULT_BGCHARACTER):
    """Creates a circle.

    Positional arguments:
        radius - radius of the circle.

    Keyword arguments:
        fpercent - fill percentage of the circle.
        fg       - foreground character.
        bg       - background character.
    """

    _validate_positive_params(radius, fpercent)

    radius = int(radius)
    fpercent = int(fpercent)

    fpercent /= 100
    size = radius + 1
    x = y = range(-size, size)

    feqs = {
        (f"x**2 + y**2 > {radius**2 - fpercent * (radius**2)}"
        f"and x**2 + y**2 < {radius**2 + fpercent * (radius**2)}")
    }

    beqs = {
        f"x**2 + y**2 < {radius**2 - fpercent * (radius**2)}"
    }

    return make_shape(x, y, feqs, beqs, fg=fg, bg=bg)


def get_points(width, height, points, *, fg=DEFAULT_CHARACTER, bg=DEFAULT_BGCHARACTER):
    """Creates a shape of points.

    Positional arguments:
        width  - width of the shape.
        height - height of the shape.
        points - array of points, each point a tuple (x, y).

    Keyword arguments:
        fg - foreground character.
        bg - background character.
    """

    _validate_positive_params(width, height)

    points = list(points)

    x = range(width)
    y = range(height)

    feqs = {
        f"(x, y) in {points}"
    }

    beqs = {
        f"(x, y) not in {points}"
    }

    return make_shape(x, y, feqs, beqs, fg=fg, bg=bg)

def get_number(number, size, *, fg=DEFAULT_CHARACTER):
    """Creates a shape of numbers.

    Positional arguments:
        number - number to print.
        size - size of the shape.
        
    Keyword arguments:
        fg - foreground character.
    """

    _validate_positive_params(number+1,size)

    width = int(size+1)
    height = int(size*2+1)

    x = range(width)
    y = range(height)

    #https://en.wikipedia.org/wiki/Seven-segment_display
    l = [
        f"y == {size*2} and x<={size}", #A
        f"x == {size} and y>{size} and y<={size*2}", #B
        f"x == {size} and y<={size}", #C
        f"y == 0 and x<={size}", #D
        f"x == 0 and y<={size}", #E
        f"x == 0 and y>{size} and y<={size*2}", #F
        f"y == {size} and x<={size}", #G
    ]

    numbers = [
        {l[0],l[1],l[2],l[3],l[4],l[5]     }, #0
        {     l[1],l[2]                    }, #1
        {l[0],l[1],     l[3],l[4],     l[6]}, #2
        {l[0],l[1],l[2],l[3],          l[6]}, #3
        {     l[1],l[2],          l[5],l[6]}, #4
        {l[0],     l[2],l[3],     l[5],l[6]}, #5
        {l[0],     l[2],l[3],l[4],l[5],l[6]}, #6
        {l[0],l[1],l[2]                    }, #7
        {l[0],l[1],l[2],l[3],l[4],l[5],l[6]}, #8
        {l[0],l[1],l[2],l[3],     l[5],l[6]}, #9
    ]

    res = ""

    for digit in str(number): 
        feqs = numbers[int(digit)]
        
        s_digit = make_shape(x, y, feqs, [], fg=fg)
        if res:
            new_res = ""
            for i,j in zip(res.split("\n"),s_digit.split("\n")):
                if i and j:
                    new_res += i+"    "+j+'\n'
            res=new_res
        else:
            res = s_digit

    return res
