# # Valid Parentheses (https://www.codewars.com/kata/52774a314c2333f0a7000688)
# Write a function that takes a string of parentheses, and determines if the order of the parentheses is 
# valid. The function should return true if the string is valid, and false if it's invalid.

# Examples

# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true
# Constraints

# 0 <= input.length <= 100

# Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. 
# Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat 
# other forms of brackets as parentheses (e.g. [], {}, <>).


import re

def valid_parentheses(string):
    a = 0
    b = 0
    new_string = re.findall(r'\(|\)', string)
    if len(new_string) == 0:
        return True
    else:
        for i in range(len(new_string)):
            if new_string[i] == '(':
                a += 1
            elif new_string[i] == ')':
                b += 1
        if a != b:
            return False
        else:
            while len(new_string) != 0:
                print("OOOOO", len(new_string))
                for j in range(len(new_string)-1):
                    if new_string[j] == '(' and new_string[j+1] == ')':
                        del new_string[j + 1]
                        del new_string[j]
                        break
                    elif new_string[j] == ')' and new_string[j + 1] == '(' and len(new_string) < 3:
                        return False
                    elif new_string[j] == ')' and new_string[j + 1] == ')' and len(new_string) < 3:
                        return False
                    elif new_string[j] == ')' and new_string[j + 1] == ')' and len(new_string) < 3:
                        return False
            return True