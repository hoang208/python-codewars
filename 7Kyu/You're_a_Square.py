'''
Given an integral number, determine if it's a square number:
    In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.

The tests will always use some integral number, so don't worry about that in dynamic typed languages.
Examples
    -1  =>  false
    0  =>  true
    3  =>  false
    4  =>  true
    25  =>  true
    26  =>  false
'''

# My Answer
import math

def is_square(n):
    if (n >= 0):
        sr=int(math.sqrt(n))
        if (sr*sr) == n:
            return True
    return False

# Best Practice answers worth remembering
import math
def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0;

def is_square(n):    
    return n >= 0 and (n**0.5) % 1 == 0