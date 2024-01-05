'''
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.
Examples input/output:
    XO("ooxx") => true
    XO("xooxx") => false
    XO("ooxXm") => true
    XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
    XO("zzoo") => false
'''

# My Answer
def xo(s):
    x="xX"
    o="oO"
    xcount=0
    ocount=0
    for c in s:
        if c in x:xcount+=1
        if c in o:ocount+=1
    if xcount == ocount:return True
    else: return False

# Best Practice answers worth remembering
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

def xo(s):
  exes = 0
  ohs = 0
  for c in s.lower():
    if c == 'x':
      exes += 1
    elif c == 'o':
      ohs += 1
  return exes == ohs