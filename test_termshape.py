import pytest
from termshape.termshape import *

def test_get_square():
	string = get_square(5)
	assert (string == """\
* * * * *
*       *
*       *
*       *
* * * * *
""")

def test_get_rectangle():
	string = get_rectangle(10, 5)
	assert (string == """\
* * * * * * * * * *
*                 *
*                 *
*                 *
* * * * * * * * * *
""")

def test_get_circle():
	string = get_circle(10)
	assert (string == """\
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
                                           
""")

def test_get_triangular():
	string = get_triangular(10)
	assert (string == """\
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
""")

def test_get_rectangle_special_character():
	string = get_rectangle(10, 5, fg='$')
	assert (string == """\
$ $ $ $ $ $ $ $ $ $
$                 $
$                 $
$                 $
$ $ $ $ $ $ $ $ $ $
""")

def test_get_rectangle_background():
	string = get_square(10, bg='.')
	assert ("""\
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
""")
