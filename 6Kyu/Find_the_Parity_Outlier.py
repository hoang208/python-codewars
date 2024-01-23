'''
You are given an array (which will have a length of at least 3, but could be very large) containing integers.
The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N.
Write a method that takes the array as an argument and returns this "outlier" N.
Examples
    [2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)
    [160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)
'''

# My Answer
def find_outlier(integers):
    if (integers[0] % 2 == 1 and integers[1] % 2 == 1) or (integers[1] % 2 == 1 and integers[2] % 2 == 1):
        return [num for num in integers if num % 2 == 0][0]
    return [num for num in integers if num % 2 == 1][0]

# Best Practice answers worth remembering
def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]

def find_outlier(integers):
    parity = [n % 2 for n in integers]
    return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]