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

'''