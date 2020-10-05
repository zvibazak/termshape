# termshape
Tremshape is a minimalistic Python packgage, that only prints basic 
shapes on terminal. 
It does not have any dependencies.

You're welcome to add any shapes!

### Explain:
The print_* functions has (x,y) ranges, and some equations and print the lines.

### Example:
```python
from tremshape import print_square
print_square(5,5)
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
from tremshape import print_square
print_square(5)
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
from tremshape import print_rect
print_rectangle(10,5)
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
from tremshape import print_circle
print_circle(10)
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

* Print a triangular:
```python
from tremshape import print_triangle
print_triangular(10)
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
