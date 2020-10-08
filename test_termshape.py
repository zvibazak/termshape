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
	assert (string == """\
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

def test_get_numbers():
	string0 = get_number(0,2)
	assert (string0 == """\
* * *
*   *
*   *
*   *
* * *
""")

	string1 = get_number(1,2)
	assert (string1 == """\
    *
    *
    *
    *
    *
""")

	string2 = get_number(2,2)
	assert (string2 == """\
* * *
    *
* * *
*    
* * *
""")

	string3 = get_number(3,2)
	assert (string3 == """\
* * *
    *
* * *
    *
* * *
""")

	string4 = get_number(4,2)
	assert (string4 == """\
*   *
*   *
* * *
    *
    *
""")

	string5 = get_number(5,2)
	assert (string5 == """\
* * *
*    
* * *
    *
* * *
""")

	string6 = get_number(6,2)
	assert (string6 == """\
* * *
*    
* * *
*   *
* * *
""")

	string7 = get_number(7,2)
	assert (string7 == """\
* * *
    *
    *
    *
    *
""")

	string8 = get_number(8,2)
	assert (string8 == """\
* * *
*   *
* * *
*   *
* * *
""")

	string9 = get_number(9,2)
	assert (string9 == """\
* * *
*   *
* * *
    *
* * *
""")

	stringPI = get_number(31415926,3)
	assert (stringPI == """\
* * * *          *    *     *          *    * * * *    * * * *    * * * *    * * * *
      *          *    *     *          *    *          *     *          *    *      
      *          *    *     *          *    *          *     *          *    *      
* * * *          *    * * * *          *    * * * *    * * * *    * * * *    * * * *
      *          *          *          *          *          *    *          *     *
      *          *          *          *          *          *    *          *     *
* * * *          *          *          *    * * * *    * * * *    * * * *    * * * *
""")