'''
1. What does this print and why?
'''
name = 'John'

def greet():
    print(f"Hello, {name}!")

greet()
'''
the greet function is invoked. the greet function takes no arguments and prints
an f-string that interpolates the value of a global variable. the global variable
can be accessed within the function's scope because the global variable is being
referenced
'''

'''
2. What does this print and why?
'''
def assign():
    var = 20
    print(var)

assign()
'''
the assign function is invoked. the assign function assigns a local variable var
to the value of 20, then prints the value of that local variable
'''


'''
3. What does this print and why?
'''
try:
    print(var)
except NameError as e:
    print("Error occurred")
'''
This try-except block attempts to print the value of a variable named var. var 
has not been assigned to a value in this case, so Python throws an exception.
The except statement catches that exception and executes its body, which is an
invocation of the print function to print the string "Error occurred"
'''

'''
4. What does this print and why?
'''
var = 10

def function1():
    var = 20
    print(var)

function1()

try:
    print(var)
except NameError:
    print("Error occurred")

def function2():
    var += 5
    print(var)

try:
    function2()
except UnboundLocalError:
    print("Error occurred")

def function3():
    global var
    var += 5
    print(var)

function3()
print(var)
'''

'''