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
the first print statement prints out the returned value of the expression 
a < b < 30. This statement evaluates if b is greater than a and less than 30. 
Because the value of b (20) is greater than that of a (10) and less than 30, this
expression evaluates as True. Therefore, True is printed to the console.
# True


In the second print statement, the returned value of a > b or b == 20 is printed.
the operands are more tightly bound to the inequality operator than the or operator.
So a > b is evaluated first. the value of a is not greater than b, so a > b evaluates
to False. This makes the first operand of the or operator False. Because it is false,
the right hand side of the or operator is now evaluated. b == 20 is evaluated. This is True,
so the right hand side of the or operator evaluates to True. Because only one of the
operands of the or operator needs to be True for the or operation to return True, 
the entire expression that is evaluated as a print function argument returns a True.
Therefore, Python will print True for the second line.
# True
'''


'''
What do these print and why?
'''
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)
print(6 not in my_list)
'''
The expression 3 in my_list returns True if 3 is an element of my_list. 3 is indeed an
element of my_list, so the first print statement prints True
# True

The expression 6 not in my_list returns True if 6 is not an element in my_list.
6 is indeed not an element in my_list, so therefore the second print statement prints
True
# True
'''

'''
What do these print and why?
'''
temperature = 25
time_of_day = "morning"

if temperature < 30 and (time_of_day == "morning" or time_of_day == "afternoon"):
    print("It's a pleasant day!")
else:
    print("It's either too hot or not the right time of day.")
'''
If the expression inside the if statement evaluates as True, then the body of the if statement
will run. The body of the else statement will not run.

If the expression inside the if statement evaluates as False, then the body of the if statement
is not run. The body of the else statement will be run.

In the if statement's expression, the operands of the < operator are more tightly bound to it than
to the and operator. So temperature < 30 is evaluated first. This evaluates as True. The first operand
of the and statement is therefore True. The second operand of the and statement is the 
expression inside the parentheses. The operands of the equality operators are more tighly bound to them
than to the or operator. time_of_day == "morning" is evaluated as True. Since the or operator only requires
one of its operands to be True in order to return True, the or expression short circuits and returns True
Both of the operands of the and operator are True. So the body of the if statement will run.
# It's a pleasant day!
'''


'''
What does this print and why?
'''
num = 12

if num / 3 < 3 and num > 10:
    print("Hello")
elif num >= 8 and num < 6 or num > 4 and num < 16:
    print("Hello 2")
elif num % 4 == 0 or num < 7 and num < 10:
    print("Hello 3")
else:
    print("Buy")
'''
python will evaluate the if statement first. If the statement evaluates as True,
then the if body will run. All other elif and else bodies will be skipped. 

The first if statement evaluates as False because 12 / 3 (4.0) is greater than
3. Therefore, the right operand of the and operator evaluates as False. The and
operator is short-circuited in this case (no other operands of the and operator
are evaluated). Because the first if statement evaluates to False, Python moves 
on to evaluate the first elif statement. 

Python evaluates logical/inequality operators from left to right when the operators
share the same level of precedence. Inequality operators have a higher precedence
than logical operators. Therefore, the operands of inequality operators are more tightly 
bound to them than to logical operands.
Operands are more tighly bound to inequality operators, so num >= 8 is evaluated
first. This is evaluated as True because 12 is indeed greater than 8. The right
side of the and operator (num < 6) evaluates as False because 12 is greater than
6. Therefore, the entire and statement (num >= 8 and num < 6) is evaluated as False.
This then becomes the operand of the or operator. Because the first operand evaluates as 
False, Python evaluates the right side of the or operator (num > 4). This operator evaluates as True,
so the returned value of the or operator is True. That makes the left operand of the final logical operator
(and) True. Python then evaluates the right operand of the and operator (n < 16). This also evaluates to True.
Because both sides of the and operator evaluate to True, the entire elif statement evaluates to True. Python runs the
code inside this first elif block. 
# Hello 2
'''