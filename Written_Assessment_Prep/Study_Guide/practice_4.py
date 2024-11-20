'''
Practice problem 3: What does the following code do and why?
'''

a = "Hello"

if a:
    print("Hello is truthy")
else:
    print("Hello is falsy")


''' First attempt: 00:01:40
variable a is assigned to the value of "Hello". Variable a is truthy because it is a nonempty string
Therefore, it passes the if statement condition on line 7.
Python prints the string "Hello is truthy"
Because the if body executed, Python does not run the body of the else statement
'''
