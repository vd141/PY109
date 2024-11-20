'''
1. Which variable is being coerced? Is it implicit or explicit coercion?
'''

x = 3.5
y = 5
z = x + y

''' 
Because one of the operands is a float, the integer operand is coerced into a 
float for the operation to work. The operation can only perform on addends of 
the same type. 

In this example, y is coerced from an integer to a float. This is done
implicitly.
'''
################################################################################

'''
What coercion is happening here? Is it implicit or explicit?
'''

a = 1
b = 2
print(a + b)

'''
This is an example of an int being coerced into a string. a and b are both 
integers, so the result of the operation in the parentheses is an int. The print
function prints out strings only, so the result of the operation, 3, is coerced
into a string

This is another example of an implicit coercion
'''