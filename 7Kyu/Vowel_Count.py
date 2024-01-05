'''
Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels for this Kata (but not y).
The input string will only consist of lower case letters and/or spaces.
'''

# My answer
def get_count(sentence):
    vowels="aeiou"
    count=0
    for letter in sentence:
        if letter in vowels:
            count= count + 1
    return count

# Best Practice answers worth remembering
def getCount(s):
    return sum(c in 'aeiou' for c in s)