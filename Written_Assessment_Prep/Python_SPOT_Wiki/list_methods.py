'''
What does this print and why?
'''
my_list = [1, 2, 3, 4, 5]
length_of_list = len(my_list)
print("Length of the list:", length_of_list)
'''
The list contains 5 integer objects. The len() function returns the integer number
of objects contained in the list.
# Length of the list: 5
'''

'''
What does this print and why?
'''
lst_one = [0, 1, 2, 3]
lst_two = lst_one.append(4)
if lst_two:
    print(lst_two)
else:
    print(lst_one)
'''
lst_one is a variable that is assigned to a list
lst_two is a variable that is assigned to the return value of lst_one's append method (None)
lst_two is therefore Falsy (evaluates to False)
lst_one's append method does mutate lst_one (appends a value of 4). The variable 
    lst_one now points to a list [0, 1, 2, 3, 4]

the because lst_two evaluates to True, the block of the if statement does not execute
The else block executes instead

Python prints lst_one, which is
# [0, 1, 2, 3, 4]
'''


'''
What does this print and why?
'''
my_list = [1, 2, 3, 4, 5]
ele = my_list.pop()
print("Popped element:", ele)
print("List after popping:", my_list)
ele1 = my_list.pop(1)
print("Popped element at index 1:", ele1)
print("Modified list after popping at index 1:", my_list)
'''
my_list is a variable that points to a list of integers
ele is a variable that points to the value of the popped element. the pop method
removes the last element of the list (if given no arguments) and returns that 
element
the pop method mutates its parent object
# Popped element: 5
# List after popping: [1, 2, 3, 4]

ele1 is a variable that stores the returned value of the pop method. the pop
method takes the index of the element to be removed, mutates the parent object
by removing it, and returning the removed element. Here, ele1 stores the element
at index 1 of the list: 2. 
# Popped element at index 1: 2
# Modified list after popping at index 1: [1, 3, 4]
'''


'''
What does this print and why?
'''
elements = [0, 1 , 2, "Dima"]
print(elements.reverse())
print(elements)
'''
elements is a heterogenous list (contains different types of values as elements)
the reverse method, when invoked, mutates the parent object by reversing the order
of its elements. The reverse method returns a None value
'''


'''
What does this print and why?
'''
ages = {
    "dimo": 31,
    "olena": 32,
    "tetiana": 28
}

def get_val_of_dima(info):
    try:
        info['dimo']
        return info['dimo']
    except KeyError:
        return "Typo"

print(get_val_of_dima(ages))
'''
ages is a variable that points to a dict object with three key-value pairs
the get_val_of_dima function takes the reference to the ages dict as an argument
and tries to access the value of the 'dimo' key in the dict. if it can access the value,
it returns the value.

If accessing the value of 'dimo' throws a KeyError exception, the function returns
the string "Typo"

# 31
'''


'''
What does this print and why?
'''
my_dict = {'a': 1, 'b': 2, 'c': 3}
keys = my_dict.keys()
print(keys)
for key in keys:
    print(key)
'''
the keys dictionary method returns a dict-view object that is a sequence of the
dictionary keys

the dict view object is iterable. the for loop prints each key in the dict view
object
'''


'''
What does this print and why?
'''
my_dict = {'a': 1, 'b': 2, 'c': 3}
values = my_dict.values()
print(values)
for value in values:
    print(value)
'''
the dictionary values method returns a dict-view object which is a sequence of
the dictionary values

the sequence is iterable. it is used in the for loop statement to display each
value
'''


'''
what does this print and why/
'''
my_dict = {'a': 1, 'b': 2, 'c': 3}
items = my_dict.items()
print(items)
for key, value in items:
    print(key, value)
'''
the items dictionary method returns a dict view method that contains each of the
dictionary's key-value pairs stored as a tuple

the for loop prints the key value and corresponding value value to the console
'''