'''
This time no story, no theory. The examples below show you how to write function accum:
Examples:
    accum("abcd") -> "A-Bb-Ccc-Dddd"
    accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
    accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
'''

# My Answer
def accum(s):
    count=-1
    ans=""
    for char in s:
        count+=1
        ans=ans + char.upper() + (char.lower() * count) + "-"
    return ans[:-1]

# Best Practice answers worth remembering
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))