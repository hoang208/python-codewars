'''
In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).
Example: (input --> output)
    "ATTGC" --> "TAACG"
    "GTAT" --> "CATA"
'''

# My Answer
def DNA_strand(dna):
    ans=[]
    for char in dna:
        if char == "A":
            ans.append("T")
        if char == "T":
            ans.append("A")
        if char == "C":
            ans.append("G")
        if char == "G":
            ans.append("C")
    return ''.join(ans)


# Best Practice answers worth remembering
import string
def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG","TAGC"))

def DNA_strand(dna):
    pairs = {'A':'T','T':'A','C':'G','G':'C'}
    return ''.join([pairs[x] for x in dna])