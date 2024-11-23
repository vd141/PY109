'''
Interview: likely no code will be needed. All about verbalizing concepts. Not 
able to test code either. Very similar written exams in terms of difficulty.
Interviews are 30 minutes with 5 questions
'''

'''
What is happening on line 7?
'''

month = "December"
day = int(input("What day is it? "))
print(f"Today is the {day} of {month}")

'''
Line 7 is a call to a print function, which is taking an f-string. An f-string 
allows string interpolation by coercing the value of the expression/variable in 
braces into a string
'''

'''
What is a primitive?

Primitive types are the most fundamental data types in a language. Almost all 
data in a language is built from primitives.

In Python, primitives are integers, floats, booleans, and strings
'''

'''
What is a literal?

A literal is any syntactic notation that lets you directly represent an object 
in source code:
    'Hello, world!'   # str literal
    3.141592          # float literal
    True              # bool literal
    {'a': 1, 'b': 2}  # dict literal
    [1, 2, 3]         # list literal
    (4, 5, 6)         # tuple literal
    {7, 8, 9}         # set literal

Not literals:
    range(10)         # Range of numbers: 0-9
    range(1, 11)      # Range of numbers: 1-10
    set()             # Empty set
    frozenset([1, 2]) # Frozen set of values: 1 and 2

'''

'''
Are integers and floats literals?

Yes
'''

'''
shallow and deep copy behavior
'''

'''
def add_player(players, name, info):
    players[name] = info

players = {
    "Bob": {"age": 32},
    "Alicia": {"age": 28},
    "Marcus": {"age": 25},
    "Phoebe": {"age": 27},
}


add_player(players, "Jacob", {"age": 18})

This would be an example of the players dict being shadowed inside of the 
add_player function
'''

'''
Know how to point out arguments and parameters in code
'''

'''
Make a distinction between inequality and comparison operator
'''

'''
evaluates as true vs. truthy

we refer to the things on both sides of a comparison operator as operands, not
arguments
'''

# print('a' and 2 < 3)
# print('' or [])
# print(0 and 2 < 3 or 'c' > 'a')
# print(0 or 2 < 3 and 'c' > 'a') is the same as print(0 or ((2 < 3) and 'c' > 'a'))


lst1 = [0, 1, 2, 3]
lst2 = lst1.pop(0) and lst1.pop()
print(lst2)

if lst2:
    print(1, lst2)
else:
    print(2, lst1)
# 2 [1, 2, 3]

# new problem
lst1 = [0, 1, 2, 3]
lst2 = lst1.reverse() or lst1.reverse()

if lst2:
    print(1, lst2)
else:
    print(2, lst1)