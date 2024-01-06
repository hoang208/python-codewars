'''
Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.
Your task is to write a function maskify, which changes all but the last four characters into '#'.
Examples (input --> output):
    "4556364607935616" --> "############5616"
        "64607935616" -->      "#######5616"
                "1" -->                "1"
                    "" -->                 ""
    "Skippy" --> "##ippy"
    "Nananananananananananananananana Batman!" --> "####################################man!"
'''

# My Answer
def maskify(cc):
    return f"{'#'*(len(cc)-4)}{cc[-4:]}"

# Best Practice answers worth remembering
def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:]

def maskify(cc):
    l = len(cc)
    if l <= 4: return cc
    return (l - 4) * '#' + cc[-4:]