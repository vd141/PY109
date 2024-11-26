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
except UnboundLocalError as e:
    print(f"Error occurred: {e}")

def function3():
    global var
    var += 5
    print(var)

function3()
print(var)
'''
var is a variable that assigned to the value of 10 in the global scope

a function named function1 is defined, which, when invoked, assigns a local variable
named var that shadows the global variable. the value of that local variable is printed
to the console.

# Try block after function1 definition
the try block contains a statement that prints variable. if this statement executes
without throwing an exception, the except block does not run. here, the statement
to print var references var in the global scope, so the try block executes without errors

a function named function2 is defined, in which an augmented assignment addition
operation is done to the variable var. the agumented assignment expects a local
variable to be defined, except there is none. so the augmented assignment operation
throws an exception because it cannot access a locally defined variable

function 3 is invoked. in function3's body, the global keyword indicates that the
var global variable will be referenced. all operations done on var inside this function
will affect the global var's value. here, an augmented assignment addition operation is
performed on var. this adds 5 to the global var's value and reassigns the global var
to the sum. the function then prints out the global var value
# 15
# 15
'''


'''
5. What does this print and why?
'''
var = 10

def function1():
    print(var)

function1()

def function2():
    var = 20
    print(var)

function2()
print(var)
'''
function 1 prints var from the global scope

function 2 prints var from the local scope. the var in the local scope shadows
the var in the global scope. 
# 10
# 20
# 10
'''


'''
6. What does this print and why?
'''
def function1():
  x = 10

  def function2():
      y = 20
      print(x)
  
  function2()
  
  print(x)

function1()
print(x)
print(y)
'''
function 2 is defined within function 1, so it has access to the namespace of
the variables assigned in function 1. function 2, when invoked, will print the
value of x as assigned in the first body line of function 1

the print invocation within function1() will also print the value of variable x

the variable assignments are only found within the enclosing function's namespace
and cannot be accessed globally, so the print(x) and print(y) invocations after
the function1 invocation throw exceptions because x and y do not exist in the global scope
'''


'''
7. What does this print and why?
'''
var = 10

def access():
    print(var)
'''
the access function, when invoked, prints out the value of var, which exists in
the global scope

this code does not print anything because access() is not invoked
'''