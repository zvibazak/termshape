import pytest
from termshape.termshape import *

string = get_square(5)
assert (string == """\
* * * * *
*       *
*       *
*       *
* * * * *
""")
