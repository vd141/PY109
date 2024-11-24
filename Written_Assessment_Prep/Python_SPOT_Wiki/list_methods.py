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