[![PyPI version fury.io](https://badge.fury.io/py/termshape.svg)](https://pypi.org/project/termshape/)
[![codecov](https://codecov.io/gh/zvibazak/termshape/branch/main/graph/badge.svg)](https://codecov.io/gh/zvibazak/termshape)
![Tests](https://github.com/zvibazak/termshape/workflows/Python%20application/badge.svg)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/zvibazak/termshape.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/zvibazak/termshape/context:python)

# termshape
Termshape is a minimalistic Python package, that only prints basic 
shapes on terminal. 
It does not have any dependencies.

You're welcome to add any shapes!

## Installation 

```
pip install termshape
```

### Explanation:
The idea is to draw all the shapes as vectors, so you can set the size of any shape as you wish.
Each shape has equations that print it.
The ```get_*``` functions has (x,y) range and some equations, and from them it prints the shape.

### Example:
```python
from termshape import get_square
print(get_square(5))
```
so: 
`x-range` is between 0 and 4
`y-range` is between 0 and 4
and the equations are:
`x=0`, `y=0`, `x=5` and `y=5`.

See below the output.

## Usage

* Print a square:
```python
from termshape import get_square
print(get_square(5))
```
```
* * * * *
*       *
*       *
*       *
* * * * *
```

* Print a rectangle:
```python
from termshape import get_rectangle 
print(get_rectangle(10, 5))
```
```
* * * * * * * * * *
*                 *
*                 *
*                 *
* * * * * * * * * *
```

* Print a circle:
```python
from termshape import get_circle
print(get_circle(10))
```
```
                  * * * * *                
              *               *            
          *                       *        
        *                           *      
      *                               *    
                                           
    *                                   *  
                                           
  *                                       *
  *                                       *
  *                                       *
  *                                       *
  *                                       *
                                           
    *                                   *  
                                           
      *                               *    
        *                           *      
          *                       *        
              *               *            
                  * * * * *                
```

* Print a triangle:
```python
from termshape import get_triangular
print(get_triangular(10))
```
```
*                  
* *                
*   *              
*     *            
*       *          
*         *        
*           *      
*             *    
*               *  
* * * * * * * * * *
```

* Print a shape with custom character:
```python
from termshape import get_rectangle
print(get_rectangle(10, 5, fg='$'))
```
```
$ $ $ $ $ $ $ $ $ $
$                 $
$                 $
$                 $
$ $ $ $ $ $ $ $ $ $
```

* Print a shape with background:
```python
from termshape import get_rectangle
print(get_square(10, bg='.'))
```
```
* * * * * * * * * *
* . . . . . . . . *
* . . . . . . . . *
* . . . . . . . . *
* . . . . . . . . *
* . . . . . . . . *
* . . . . . . . . *
* . . . . . . . . *
* . . . . . . . . *
* * * * * * * * * *
```

* Print a shape with points:
```python
from termshape import get_points
points_array = [(0, 0), (0, 9), (9, 0), (9, 9)]
print(get_points(10, 10, points_array, bg='.'))
```
```
* . . . . . . . . *
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
* . . . . . . . . *
```

* Print numbers:
```python
from termshape import get_number
print(get_number(31415926,3))
```
```
* * * *          *    *     *          *    * * * *    * * * *    * * * *    * * * *
      *          *    *     *          *    *          *     *          *    *      
      *          *    *     *          *    *          *     *          *    *      
* * * *          *    * * * *          *    * * * *    * * * *    * * * *    * * * *
      *          *          *          *          *          *    *          *     *
      *          *          *          *          *          *    *          *     *
* * * *          *          *          *    * * * *    * * * *    * * * *    * * * *
```

* Print a custom shape using lines:
```python
from termshape import get_lines
lines = [(0, 0), (9, 9), (0, 9), (9, 0), (0, 0)]
print(get_lines(10, 10, lines))
```
```
* * * * * * * * * *
  *             *  
    *         *    
      *     *      
        * *        
        * *        
      *     *      
    *         *    
  *             *  
* * * * * * * * * *
```
