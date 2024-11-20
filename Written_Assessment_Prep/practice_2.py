'''
Practice problem 1: What does this code print and why?
'''

def replace(string, value):
    while True:
        break

    string = value

greet = 'Hey!'
replace(greet, 'Hello')
print(greet)

''' First attempt at explanation
On line 11, greet is a variable that is assigned to the value of 'Hey!' in the global scope.
On line 12, the replace function is called, which takes the value pointed to by greet and 'Hello' as arguments
    In the replace function, the while loop does not affect the values
    In the final line of the function, the local variable string is assigned to the value of the value variable: 'Hello!'
    However, the local variable string is not accessible in the outer scope. And it also does not reassign greet because greet is an immutable data type (string)
    Line 12 ultimately does not affect anything in the global scope
On line 13, Python prints 'Hey!', taking the value that greet points to in the global scope
'''