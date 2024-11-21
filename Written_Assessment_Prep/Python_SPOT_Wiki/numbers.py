'''
What does this return and why? What concept does this cover?
'''

def convert_to_int(string):
    try:
        converted_integer = int(string)
        return converted_integer
    except ValueError:
        return "That string cannot be converted to an integer"

print(convert_to_int("hello"))

print(convert_to_int("5"))

''' 11/20/24
The function takes the argument and tries to explicitly coerce it into an int
If the argument can be coered into an int, it is returned

If the argument cannot be coerced into an int due to a ValueError, the function
returns a string

The function uses a try/except block. If the try block runs without errors, then
the except block does not run. If any code in the try block is run and an
exception of type ValueError occurs, the except block is run
'''


'''
What does this return and why? What concept does this cover?
'''

def division(number1, number2):
    numerator = number1
    denominator = number2

    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        return "The denominator cannot be zero"

print(division(5, 0))

'''
The function takes two arguments and divides one by the other. It uses a try
except block to catch ZeroDivisionErrors. If there is a ZeroDivisionError, the 
code in the except block runs

If the division is successful, the function will return the result as a float

If the division fails for any other reason other than a ZeroDivisionError, 
Python will not run any code beyond that line
'''


'''
What does this print and why, what concept does this demonstrate?
'''

def addition(number1, number2):
    number1 += number2

x = 1
y = 2

addition(x, y)
print(f"x is {x}, y is {y}")

'''
The function takes two arguments and performs augmented assignment addition. In 
this case, number1 becomes the value of itself plus number2. But because number1
is an integer and is therefore immutable, variable x is unchanged by the 
function


'''

'''
What does this print and why? What concept does this cover? How could you
refactor this to remove the space?
'''
print(2 + 3 * 4, 4 * (3 + 2))
'''
this will print 14 20. the comma separates different expressions inside the 
print function

This can be refactored to remove the space by interpolating the expressions in
a Python f string
print(f'{2 + 3 * 4}{4 * (3 + 2)}') 

another way of removing the space is to specify the sep= parameter to be an 
empty string ''

the main concept here is operator precedence and the use of commas to separate 
print expressions
'''

