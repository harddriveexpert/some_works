# Unique In Order (https://www.codewars.com/kata/54e6533c92449cc251001667)

# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

# For example:

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]



import re

def unique_in_order(iterable):
    value = []
    if type(iterable) is str:
        new_text = re.findall(r'\w',iterable)
    else:
        new_text = iterable
    c = len(new_text)
    for i in range(c):
        if i == c-1:
            value.append(new_text[i])
        elif new_text[i] != new_text[i+1]:
            value.append(new_text[i])
    return value