'''
The function concat creates a new object from s1 and s2, but does not assign the 
resulting value to a variable. It merely returns s1. So the print function will 
print out the original text value.
'''
#1
text = 'Hello, there!'

def concat(s1, s2):
    s1 + s2
    return s1

print(concat(text, '!!'))
print(text)

'''
The concat function performs and augmented assignment addition operation on s1.
s1 is reassigned to the value containing the concatenation of s1 and s2. s1 is
then returned. In the first print() call, the concatenation is printed.

The second print call takes the global text variable as the argument. Because 
text is immutable and because there is no global keyword inside the function,
the augmented assignment inside the function does not affect the global text 
variable. Therefore, the second call to print() prints out the original text 
value
'''
#2
text = 'Hello, there!'

def concat(s1, s2):
    s1 += s2
    return s1

print(concat(text, '!!'))
print(text)

'''
The function add_player references the players dict from the global scope. 
Dicts are immutable, and the add_player function is resassigning the element at
index name to a new value, info. "Jacob" is not a key in the dictionary before
add_player() is run, therefore the add_player() function is adding a new key
value pair to the players dictionary. Print() will print out the updated 
dictionary with Jacob's name and age in it
'''
#3
def add_player(name, info):
    players[name] = info

players = {
    "Bob": {"age": 32},
    "Alicia": {"age": 28},
    "Marcus": {"age": 25},
    "Phoebe": {"age": 27},
}

add_player("Jacob", {"age": 18})
print(players)

'''
add_plyer takes a reference to a players dict, which is mutable. It takes the 
arguments "Jacob" and a literal dict {"age": 18}. Because those do not exist in 
the dictionary at the time of the add_player invocation, the key value pair is 
added to the dict. Because players is being mutated inside the function, the
global players is also mutated.
'''
#4
def add_player(collection, name, info):
    collection[name] = info

players = {
    "Bob": {"age": 32},
    "Alicia": {"age": 28},
    "Marcus": {"age": 25},
    "Phoebe": {"age": 27},
}

add_player(players, "Jacob", {"age": 18})
print(players)