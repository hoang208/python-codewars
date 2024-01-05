'''
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.
Example: (Input --> Output)
    "Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)
    isIsogram "Dermatoglyphics" = true
    isIsogram "moose" = false
    isIsogram "aba" = false
'''

# My Answer
def is_isogram(string):
    for char in string:
        if string.lower().count(char) > 1:
            return False
    return True

# Best Practice answers worth remembering
def is_isogram(string):
    return len(string) == len(set(string.lower())) #Sets can't have duplicates