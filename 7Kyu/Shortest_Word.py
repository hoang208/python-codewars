'''
Simple, given a string of words, return the length of the shortest word(s).
String will never be empty and you do not need to account for different data types.
'''

# My Answer
def find_short(s):
    return len(min((word for word in s.split(" ")), key=len))

# Best Practice answers worth remembering
def find_short(s):
    return min(len(x) for x in s.split())