'''
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
For example, if we run 9119 through the function, 811181 will come out, because 9^2 is 81 and 1^2 is 1. (81-1-1-81)
Note: The function accepts an integer and returns an integer.
'''

# My Answer
def square_digits(num):
    num_str=str(num)
    new_num=""
    for digit in num_str:
        new_digit=int(digit) ** 2
        new_num += str(new_digit)
    return int(new_num)

# Best Practice answers worth remembering
def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)

def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))