'''
Interview: likely no code will be needed. All about verbalizing concepts. Not 
able to test code either. Very similar written exams in terms of difficulty.
Interviews are 30 minutes with 5 questions

If the question asks for the concept being demonstrated, explicitly say what it is. (answer the question)


Will points be deducted in interviews if we don't answer the question fully the
first time? Will the interviewer prompt us to answer the whole question if we 
only answer part of it? Interviewer will prompt

In written exams, be sure you answer the whole question! This is a common 
pitfall.

In the interview
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

# def shout(text):
#     global exclamation_marks
#     exclamation_marks = '!!!'
#     return text.upper() + exclamation_marks

# print(shout('hello') + exclamation_marks)

###########################################
greeting = "Hello"

def greet(greeting):
    greeting += " world"
    print(greeting)

greet(greeting)
print(greeting)
# talk about shadowing!

##############################################
text = 'Hello! I am Eloise.'

def swap(s):
    for char in s:
        s.replace(char, char.upper())
    return s

print(swap(text))
print(text)
# string immutability is the concept here

# new problem
letters = ['a', 'b', 'c', 'd']

def reverse_list1(lst):
    return lst[::-1]

def reverse_list2(lst):
    return lst.reverse()

reverse_list1(letters) # ?
reverse_list2(letters) # ?


# what is happening here? What concept is being demonstrated?
text = 'Hello! I am helen.'

def swap(s):
    for char in s:
        text = s.replace(char, char.upper())
    return text

print(swap(text))
print(text)

# what is happening here? what concept is being demonstrated?
greeting = ["Hello"]

def greet():
    greeting += ["world"]
    print(greeting)

greet()
print(greeting)


# what is happening here? What concept is being demonstrated?
players = [
  {'name': "Joe", 'age': 25},
  {'name': "Andy", 'age': 31},
  {'name': "Ralph", 'age': 18},
  {'name': "Mark", 'age': 28},
]

player = players[0]
# print(player)
player = 25
print(players)

players[0]['age'] # 25
new_list = []

for player in players:
    # new_list.append(player['age'])
    player = player['age']


# print(players)

'''
what are two ways to check if an object is a certain type?
'''

'''
how do we center the following title in a 40-character wide table
'''
title = "Flintstone Family Members"

'''
Two ways to determine whether a dict contains a key?
'''

'''
given these two dicts, how do we update ages with the entries in additional_ages

ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}
additional_ages = {'Marilyn': 22, 'Spot': 237}
'''

'''
what are three ways to remove all of the elements from a list?
'''

'''
What will the following code output?
'''
print([1,2,3] + [4,5])

'''
What will the following code output?
'''
my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1)



'''
the following function unecessarily uses two return statements to return boolean
values. can you rewrite this function so that it only has one return statement and 
does not explicitly use either True or False?
'''
def is_color_valid(color):
    if color == "blue" or color == "green":
        return True
    else:
        return False
    
