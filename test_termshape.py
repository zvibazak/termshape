import pytest
from termshape.termshape import *

string = str(print_square(5))
assert (string == """* * * * *
*       *
*       *
*       *
* * * * *
""")
