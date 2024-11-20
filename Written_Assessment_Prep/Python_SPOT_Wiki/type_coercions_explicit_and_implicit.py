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