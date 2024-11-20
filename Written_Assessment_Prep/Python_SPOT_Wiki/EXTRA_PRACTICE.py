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