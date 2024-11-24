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
the conditional statement checks if all the charactes in the string that is
assigned to the variable name are uppercase. True if so, False if otherwise
If the conditional statement returns true, Python prints world in all uppercase
and world in all lowercase if otherwise

This code willp print "WORLD"
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
The function takes a string as an argument and evaluates the returned value of
string's upper method. the if conditional checks for Truthy or Falsy values.
the str.upper() method returns a fully uppercase instance of its parent object.
regardless of the case of the values themselves, the value returned by str.upper()
will be Truthy if it is a nonempty string and Falsy otherwise

For each of the values pointed to by str1, str2, and str3, the conditional will
evaluate them as Truthy

The function invocations will print 'This is all caps' three times
'''

'''
What do these print and why?
'''
str1 = "    "
str2 = "  Hello   "
str3 = "Hello World"

print(str1.isspace())
print(str2.isspace())
print(str3.isspace())

sentence = "Hello     World!   How are you?   "
word_count = sum(1 for word in sentence.split() if word.isspace())
print("Number of words in the sentence:", word_count)
'''
the isspace() method checks if all of the characters in the string are spaces.
If there are non space characters in the string, the method will return False.
It will return True if otherwise

The code will print True, False, False

word_count stores the value that sum() returns from its argument. sum()'s argument
is a generator object that is created as a result of the generator expression
'''

'''
What do these print and why?
'''
s = "   Hello, World!   "
print(s.strip())
print(s.strip(" !"))
'''
the strip method returns a string without leading or trailing whitespace
when strip is given arguments, it removes the leading and trailing characters in
that string
'''

'''
What do these print and why?
'''
s = "www.example.com"
print(s.lstrip('wcmo.'))
'''
the lstrip method removes the leading whitespace characters from the string.
in this case, it removes the characters 'w' and '.'

'c', 'm', 'o' are not removed from the s string because they are not leading
characters in the string
'''

'''
What do these print and why?
'''
s = 'impatient'
print(s.rstrip('tp'))
print(s.rstrip('p'))
'''
the argument of the first print statement is the return value of s''s rtsrip
method. the rstrip method removes the characters 't' and 'p' from the string, if
they are trailing characters

the second print statement prints the return value of the rstrip method when the
trailing p characters are removed

# impatien
# impatient
'''

'''
What do these print and why?
'''
s = "Hello, World!"
print(s.replace("Hello", "Hi"))
print(s.replace("o", "0"))
'''
the first print statement prints the returned value of the s string's replace 
method. the method invocation replaces "Hello" in the s strign with "Hi"

the second print statement prints the returned value of the s sting's replace
method. the method invocation replaces all 'o' characters in the s string with
a '0'

# Hi, World!
# Hell0, W0rld!
'''

'''
What do these print and why?
'''
sentence = "This is a sample sentence."
words = sentence.split()
print(words)

csv_data = "John,Doe,30,New York"
fields = csv_data.split(",")
print(fields)

sentence = "This is a sample sentence."
words = sentence.split(maxsplit=2)
print(words)
'''
sentence is a variable that is assigned to the value of the string literal
words is assigned to the returned value of sentence's split method. the split 
string method returns a list of all strings separated by spaces in the original
string

when the split method is given a string argument, it returns a list of all strings sep
arated by the argument's value

when the split method is given an explicit maxsplit value, it performs a maximum
of that many splits, from left to right of the parent string

# ['This', 'is', 'a', 'sample', 'sentence']
# ['John', 'Doe', '30', 'New York']
# ['This', 'is', 'a sample sentence']
'''

'''
What does this print and why?
'''
str1 = "hello world"
str2 = str1.capitalize()
print("Original string:", str1)
print("Capitalized string:", str2)
'''
the string method capitalize() returns a string where the element at index 0 of 
the string is capitalized. All remaining characters are lowercase

this code prints
# Original string: hello world
# Capitalized string: Hello world
'''