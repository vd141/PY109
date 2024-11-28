'''
What is the output of this code and why? What is the concept covered here?
'''

str1 = "Hello, world!"
sub1 = str1[8:12]
print(sub1)
sub2 = str1[::-1]
print(sub2)
sub3 = str1[::2]
print(sub3)

'''
sub1 is assigned to the string that is made from the elements ranging from index 
8 to 12 in str1

sub2 is assigned to the string that is the reverse of the characters in str1

sub3 is assigned to the string that is comprised of every other character in
str1
'''

'''
What does this code do and why? What concept is this?
'''

print("Hello\nWorld")

'''
This string uses an escape character, which is the backslash \, combined with
n to tell python to print everything after \n to print to a new line
'''

'''
What does this code do and why? What concept is this?
'''
name = 'Alexander Graham Bell'
print(name[0])

'''
This code assigns a variable name to the string with value 'Alexander Graham 
Bell'. The next line prints the first element of that string, which is an 
example of string indexing. Indexes of strings start at 0 in Python.
'''