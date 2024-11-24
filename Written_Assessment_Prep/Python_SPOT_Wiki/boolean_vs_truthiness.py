'''
In Python, what values are considered Falsy and Truthy?
Falsy values are
empty collectibles e.g.: empty lists[], empty tuples (), etc.
empty strings: ''
the number 0 represented as a float or integer
None
False

Truthy values are any data types that are not those

Truthy/Falsy values are said to evaluate to True/False
'''

'''
What do these print and why?
'''
truthy_values = [1, 2, 3, "hello", [1, 2, 3], {"a": 1}, True, 0, "", [], {}, None, False]

print('Values:')
for value in truthy_values:
    if value:
        print(f"{value} is truthy")
    else:
        print(f"{value} is falsy")
'''
this code will print {value} is truthy" is the value is truthy and "{value} is falsy"
if it is falsy

1, 2, 3, "hello", [1,2,3], {"a": 1}, and True are truthy and evaluate to True
0, "", [], {}, None, and False are Falsy and evaluate to False
'''

'''
What do these print and why?
'''
x = 5
y = 10
z = 15

print(x > 0 and y < 20)
print(not x == y)
print(x < y and y < z)
print(x > y or y > z)
print(not (x > y))
'''
Operands are more tightly bound to the comparison operator than they are to the 
logical operator. Therefore, x > 0 will be evaluated first. x is assigned to a
value of 5, and 5 is greater than 0, so x > 0 returns True. y is assigned to the 
value of 10, and 10 is less than the value of 20, so the expression y < 20
returns True. Both operands of the and operator are True, so the entire
expression evaluates as True. Python prints True
# True


x and y are more tightly bound to the inequality operator ==, so x == y is
evaluated first. x is assigned to the value of 5 and y is assigned to the value
of 10. 5 is not the same value is 10, so the expression x == y evaluates to False.
the not operator inverts this boolean, so the print function prints a value of
True coerced to a string
# True


x < y is the first expression to be evaluated. This expression returns true
because the value of x (5) is less than the value of y (10). y < z is the next
expression to be evaluated. y < z evaluates to True because the value of y (10)
is less than the value of z (15). Both operands of the and logical operator 
evaluate to True, so the argument that is passed ito the print function is the
boolean True. The print function coerces the boolean True to a string and prints
that string to the console.
# True

x > y is the first expression to be evaluated. Because the value of x(5) is less
than the value of y (10), the expression evaluates to False. Because the first
operand of the and operator evaluates to False, Python short circuits (doesn't
evaluate the right side expression of the and operator) and the result of the
logical expression is False. False is the print function's argument. The print
function coerces that value into a string and prints that string to the console.
# False

x > y is the first expression to be evaluated. x > y evaluates to False for the 
reason stated in the last line of code. the not logical operator inverses this
boolean. The argument of the print function is therefore True. The print function
prints out True
# True
'''

'''
What do these print and why?
'''
a = 10
b = 20

print(a < b < 30)
print(a > b or b == 20)
'''

'''