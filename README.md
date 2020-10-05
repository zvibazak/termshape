# termshape
Tremshape is a minimalistic Python packgage, that only prints basic 
shapes on terminal. 
It does not have any dependencies.

### Explain:
The print_* functions has (x,y) ranges, and some equations and print the lines.

### Example:
```python
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
print_square(5)
```
```
* * * * *
*       *
*       *
*       *
* * * * *
```

* Print a rectungle:
```python
print_rect(10,5)
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

* Print a triangle:
```python
print_triangle(10)
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
