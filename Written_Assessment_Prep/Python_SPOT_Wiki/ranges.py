'''
Basic questions:

Is range primitive or non-primitive?
- Ranges are non-primitive

Is a range mutable or immutable?
- Immutable

Does range have a literal form or a type constructor?
- A type constructor

Is range a sequence or a collection?
- a sequence is an ordered collection. Ranges are ordered collections. Therefore,
  they are both sequences and collections.

What is the most common use of the range datatype?
- The range datatype is commonly used in for loops to determine the way in which the 
loop loops through a collection

Are ranges homogenous or heterogeneous?
- Homogenous as all of its elements are of one type (int)

Why are ranges considered lazy?
- The range object's do not create any element values until the program needs them.
'''


'''
What do these print and why? What concept does this demonstrate?
'''
print(range(0,10))
print(len(range(5, 15)))
print(my_range[1])
print(str(range(3, 7)))
print(list(range(12, 8, -1)))
print(list(range(5, 5, 1)))
print(5 in range(5))
print(5 not in range(5, 10))
'''
First line demonstrates that ranges are lazy sequences. Python will print information
about the range object to the console, but not the contents of the range

second line demonstrates that ranges are collections - which have a length

third line demonstrates that ranges are indexable

fourth line demonstrates that the range object can be coerced into a string

fifth line demonstrates that a range object can be used to create a list whose elements
are that range object's elements

sixt line demonstrates that empty lists can be created from empty range objects.
Here, the start number is 5. The stop number is 4 (5-1). The step is 1. There is
no positive step from 5 to 4, so the range is empty. a list is made from this empty
range, so the list itself is empty.

seventh line demonstrates that Python can search ranges for elements. It also demonstrates
that when the range constructor is given a single argument, the range spans the numbers
from 0 to argument - 1. Therefore, 5 is not in this range

eighth line demonstrates that Python can identify that a value does not exist in a range. 
When a range constructor is given two arguments, the first argument is the first element of
the range (inclusive). The second argument is the number after the last element of the range.
'''


'''
What does this code print and why? What concept does this demonstrate?
'''
example = range(0)
if example:
    print(list(example))
else:
    print(example)
'''
The variable example is assigned to an empty range object. This empty range object
is an empty collectible (Falsy), so it evaluates to False. The expression of the 
if statement evaluates to False, so the else block runs.
# print(range(0)) -> range(0, 0)
'''

'''
What does this code print and why? What concept does this demonstrate?
'''
def number_range(number):
    match number:
        case n if n < 0:
            print(f'{number} is less than 0')
        case n if n <= 50:
            print(f'{number} is between 0 and 50')
        case n if n <= 100:
            print(f'{number} is between 51 and 100')
        case _:
            print(f'{number} is greater than 100')
number_range(0)
number_range(25)
'''
This code demonstrates the match case statement. The match case statement evaluates its
expression (in this case, number) and compares its value to the value in each case and 
executes the block associated with the first matching case

in the first function invocation, 0 is the expression evaluated by the match statement.
This expression does not pass the first case, so Python compares it to the second case.
0 is indeed less than 50, so the block of teh second case executes

in the second function invocation, 25 is the expression evaluated by the match statement.
this expression does not pass the first ase, so Python compares it to the second case. 0 
is indeed less than 50, so the block of the second case executes
'''