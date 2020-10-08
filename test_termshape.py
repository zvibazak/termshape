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
	string0 = get_numbers(0,2)
	assert (string0 == """\
* * *
*   *
*   *
*   *
* * *
""")

	string1 = get_numbers(1,2)
	assert (string1 == """\
    *
    *
    *
    *
    *
""")

	string2 = get_numbers(2,2)
	assert (string2 == """\
* * *
    *
* * *
*    
* * *
""")

	string3 = get_numbers(3,2)
	assert (string3 == """\
* * *
    *
* * *
    *
* * *
""")

	string4 = get_numbers(4,2)
	assert (string4 == """\
*   *
*   *
* * *
    *
    *
""")

	string5 = get_numbers(5,2)
	assert (string5 == """\
* * *
*    
* * *
    *
* * *
""")

	string6 = get_numbers(6,2)
	assert (string6 == """\
* * *
*    
* * *
*   *
* * *
""")

	string7 = get_numbers(7,2)
	assert (string7 == """\
* * *
    *
    *
    *
    *
""")

	string8 = get_numbers(8,2)
	assert (string8 == """\
* * *
*   *
* * *
*   *
* * *
""")

	string9 = get_numbers(9,2)
	assert (string9 == """\
* * *
*   *
* * *
    *
* * *
""")

	stringPI = get_numbers(31415926,3)
	assert (stringPI == """\
* * * *          *    *     *          *    * * * *    * * * *    * * * *    * * * *
      *          *    *     *          *    *          *     *          *    *      
      *          *    *     *          *    *          *     *          *    *      
* * * *          *    * * * *          *    * * * *    * * * *    * * * *    * * * *
      *          *          *          *          *          *    *          *     *
      *          *          *          *          *          *    *          *     *
* * * *          *          *          *    * * * *    * * * *    * * * *    * * * *
""")

def test_get_lines():
    string = get_lines(10, 10, [(0, 0), (9, 9), (0, 9), (9, 0), (0, 0)])
    assert (string == """\
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
""")