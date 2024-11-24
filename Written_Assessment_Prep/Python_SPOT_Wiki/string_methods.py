'''
What are string methods?

String methods are the string object's built-in functions. These functions allow
the user to manipulate strings
'''

'''
How do you identify a method versus a function?

a method can be thought of as a function that belongs to an object. A method can
be identified by its invocation. a method is preceded by the variable assigned 
to the object's instance, and by a period. for example, a_string.strip() is
the a_string object's method invocation. strip() is the method.
'''


'''
What does this code do and why? What concept does this demonstrate?
'''
mashup = 'thIs is How we type careLEssly'
cleaned = mashup.capitalize()
print(cleaned)
'''
mashup is variable that is assigned to a string. it is an instance of a string
object

cleaned is a variable assigned to the value returned by mashup's capitalized()
method. Capitalize returns a string object that contains all of the characters
of mashup, except the first letter of the string is capitalized and all others
are lowercase
'''

'''
What does this print and why? What concept does this demonstrate?
'''
stuff = 'tHIS iS bACKWARDS'
str1 = stuff.swapcase()
str2 = stuff.upper()
str3 = stuff.lower()
print(stuff)
print(str1)
print(str2)
print(str3)
'''
str1 is a variable that points to the value of a string that is derived from
the value of stuff. the value of str1 would be the swapped case of every
character in stuff

str2 points to the value of a string that contains all of the characters in
stuff in uppercase

str3 points to the value of a string that contains all of the characters in 
stuff in lowercase
'''

'''
What do these print and why?
'''
s1 = "Hello"
print(s1.isalpha())
s2 = "Hello World"
print(s2.isalpha())
s3 = "Hello!"
print(s3.isalpha())
s4 = "Hello123"
print(s4.isalpha())
s5 = ""
print(s5.isalpha())
s6 = "こんにちは"
print(s6.isalpha())
s7 = "HelloWorld"
print(s7.isalpha())
words = ["apple", "banana", "cherry"]
print(all(word.isalpha() for word in words))
'''
isalpha is a string method that returns True if all the characters in the string 
are alphabetical and False otherwise. alpha returns a boolean

s1: True
s2: False
s3: False
s4: False
s5: False
s6: False # True because japanese characters count as Lo (other letters) in the
unicode class. isalpha returns true when all characters are part of Lo, Lt, Lu,
Ll, and Lm classes
s7: True
all(word): True
'''

'''
What does this print and why?
'''
string1 = "HelloWorld"
string2 = "12345"
string3 = "Hello World"

result1 = string1.isalpha()
result2 = string2.isalpha()
result3 = string3.isalpha()

print("Is '{}' alphabetic?".format(string1), result1)
print("Is '{}' alphabetic?".format(string2), result2)
print("Is '{}' alphabetic?".format(string3), result3)
'''
# True. All characters are alphabetic
# False. These are numeric characters, not alphabetic ones
# False. Spaces are not alphabetical

The print statements use the value returned by the string method to print the
string to the console. The format method interpolates its argument inside of the
braces in the string. Arguments separated by a comma are by default separated by
a space in the printed string
'''

'''
What do these print and why?
'''
s1 = "123abc"
print(s1.isdigit())
s2 = "123$%^"
print(s2.isdigit())
s3 = ""
print(s3.isdigit())
s4 = "12345"
print(s4.isdigit())
'''
# False. characters 'abc' are not digits
# False: the speical characters '$%^' are not digits
# False: empty strings are not digits
# True: all of the characters in the string are digits
'''

'''
What do these print and why?
'''
print("Hello World".isalnum())
print("Hello@World".isalnum())
print("".isalnum())
print("Hello123".isalnum())
'''
isalnum returns true if all characters are alphabetic or numeric and False
otherwise
# False: spaces are not alphabetic or numeric
# False: @ is not alphabetic or numeric
# False: Empty strings are not alphabetic or numeric
# True: all characters are alphanumeric
'''

'''
What do these print and why?
'''
name = 'HELLO'

if name.isupper():
    print("WORLD")
else:
    print("world")
'''

'''

'''
8. What do these print and why?
'''
def punctuation_type(str):
    if str.upper():
        print('This is all caps')
    elif str.lower():
        print('This is all lowercase')
    else:
        print('Neither')

str1 = 'HELLO'
str2 = 'yolo'
str3 = 'My Name Is: '

punctuation_type(str1)
punctuation_type(str2)
punctuation_type(str3)
'''

'''