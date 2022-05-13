# Break camelCase (https://www.codewars.com/kata/5208f99aee097e6552000148)

# Complete the solution so that the function will break up camel casing, using a space between words.

# Example

# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""


import re

def solution(s):
    return ' '.join(re.findall(r'[A-Z][a-z]+|[a-z]+', s))