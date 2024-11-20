'''
Practice problem 1: What does this code do and why?
'''

greeting = 'Hello'

def greet():
    greeting = 'Hi'
    return greeting

greet()
print(greeting)


''' Attempt 1: 00:02:40 - Learned how to explain a variable that is not assigned to a function's output/return value
The variable greeting is assigned to hte value of 'Hello' in the global scope
a Function called greet sets a local variable named greeting to the value of 'Hi'
this value is returned

the function is invoked, but a variable is not assigned to the output of the function (aka its return value).
The function invocation effectively does nothing to affect the value of the gloal greeting variable

the variable greeting from the global scope that was assigned to the value of 'Hello' on line 5 is printed
'''