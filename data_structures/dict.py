# store mappings of keys to values using the dict data type 
print("Dictionaries are a data type for a mutable unordered mapping of unique keys to values")
print("The key has to be unique because it is used to access the value to print it out, or modify it")
print("The key has to be of an immutable data type like int, float, string, tuple and cannot be of a mutable data type like sets or lists")
print("Immutable data types are hashable which means their values do not change during their lifetime allowing Python to create hash values for them to uniquely identify them")
print('#' * 79)
print("The dict can be created as follows:")
thisdict = {'brand': 'Ford','model': 'Mustang','year': 1964}
print("By using curly braces '{}' to sorround a comma separated collection of key-value pairs delimited by a colon (:) as follows thisdict = {'brand': 'Ford','model': 'Mustang','year': 1964} and printing it out, you get\n", thisdict)
print('#' * 79)
n = {}
m = dict()
print("When you declare a variable and assign it an empty set of curly braces, it is assigned the type dict (instead of a set) e.g n = {} and type(n) will give; ", type(n))
print("When you declare a variable and assign it to the constructor dict() like this m = dict(), it is assigned the type dict and type(m) will give; ", type(m))
print('#' * 79)
print("The key (sorrounded by square brackets, []) in a dict can be used to access a value, change a value or add a new object to a dict as follows:")
print("we can print out the value of the brand in our list above like this thisdict['brand'] to get", thisdict['brand'])
print('#' * 79)
thisdict['brand']='mercedes'
print("we can change the value of the brand in our list above like this thisdict['brand']='mercedes' and printing out the value, we get: {}".format(thisdict))
print('#' * 79)
thisdict['make']='c200'
print("we can add a new object to our list above like this thisdict['make']='c200' and printing out the dict we see our new object: {}".format(thisdict))
print('#' * 79)
print("There are a few methods that are useful for operating on lists:")
print("The get() method looks up to see if a key exists in the dict and if it does, returns the value of that key. If it does not exist, it returns the keyword None (by default) or another user defined response: e.g")
print('#' * 79)
cc = thisdict.get('cc', 'The carrying capacity does not exist')
print("We can look for a key 'cc' in our existing dict and if it does not exist print a message 'The carrying capacity does not exist' like this cc = thisdict.get('cc', 'The carrying capacity does not exist') and printing out the variable cc 'print(cc)' that stores the return value we get the output:",cc)
print('#' * 79)
print("The get() method is a better way to acces a value from a key in a dict compared to using just the square brackets and the key value like; thisdict['cc'] which returns an error if the key does not exist. Errors cause programs to break which is bad, so if you anticipate that a key might not exist, it is better to use the get() method which returns None or a custom user defined value.")
print('#' * 79)
print("The dict data structure supports the membership operators 'in' and 'not in' which return a bool value of whether a key exists in the dict or not e.g:")
print("You can also check if a value exists (or not) in a dictionary using the membership operators and calling the values() method on the dictionary value e.g 'Ford' in thisdict.values()")
print("'year' in thisdict returns {} and 'cc' not in thisdict returns {}".format('year' in thisdict, 'cc' not in thisdict))
print('#' * 79)
print('#' * 99)
print("Compound data structures can be formed by combining collections of data together. Collections of data are any of the data structures (containers of data) i.e lists, tuples, sets and dicts")
print("As an example, we can have a dict where the value of each key is another dict like this:")
print('#' * 79)
cars = {
    'mercedes': {
        'model': 'c200',
        'make': 'sedan',
        'year': 2020,
        'cc': 2000
    },
    'BMW': {
        'model': 'x6',
        'make': 'SUV',
        'year': 2019,
        'cc': 3000
    }
}
print("An example of a compound data structure:", cars)
print("We can perform operations on the compound data structure as we would on the simple data structure e.g add a new object, change a value or get a value:")
print('#' * 79)
audi = {
    'model': 'Q7',
    'make': 'SUV',
    'year': 2018,
    'cc': 2500
}
cars['audi'] = audi
print("Our compound data structure with a new object added", cars)
print('#' * 79)
print("We can get a car's make as follows: cars.get('audi').get('make')-", cars.get('audi').get('make'))
print("Or we can use square brackets as follows: cars['audi']['make'] :", cars['audi']['make'])
print('#' * 79)
print('#' * 99)
print("An exercise to play around with data structures")
print('#' * 79)
verse = "if you can keep your head when all about you are losing theirs and blaming it on you if you can trust yourself when all men doubt you but make allowance for their doubting too   if you can wait and not be tired by waiting or being lied about  don’t deal in lies   or being hated  don’t give way to hating and yet don’t look too good  nor talk too wise"
print("Here is a string\n", verse)
print("The number of characters in the verse is:", len(verse))
print('#' * 79)
verse_list = verse.split()
print("Here is a list generated from the above string by using the string method split()\n", verse_list)
print("The number of elements in the list is:\n", len(verse_list))
print('#' * 79)
verse_set = set(verse_list)
print("Here is a set (collection of unique elements only) generated from the list above using the set() constructor:\n", verse_set)
print("The number of elements in the set is:\n",len(verse_set))
print('#' * 79)
verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
print("This is a dictionary created from the string above with each unique word and how many times it appeared on the string:\n",verse_dict)
print("The number of words in the dict is:\n", len(verse_dict))
print('#' * 79)
keys_list = verse_dict.keys()
print("Here is a list of keys generated from the dict by using the dict method keys()", keys_list)
print("There are {} keys in the dict".format(len(keys_list)))
print('#' * 79)
values_list = verse_dict.values()
print("Here is a list of values generated from the dict by using the dict method values()", values_list)
print("There are {} values in the dict".format(len(values_list)))
print('#' * 79)
print("Let's sort the values in the list in ascending and descending order and then print the maximum and minimum value using indices")
sorted_values_asc = sorted(values_list)
sorted_values_desc = sorted(values_list, reverse=True)
print("maximum value is:", sorted_values_asc[-1])
print("minimum value is:", sorted_values_asc[0])
print("Or we could just use the max and min list methods to get the same answers")
print("maximum value is:", max(values_list))
print("minimum value is:", min(values_list))

print('#' * 79)

# other useful dictionary methods

print("1. keys() - Returns a list containing the dictionary's keys")
print("The value returned is not a true list since you cannot modify it (like use append() or insert() on it). It is a list-like object that can be turned to a list by passing it to the list() method")
my_list = {1:'a', 2:'b',3:{4:'c', 5:'d'}}
print(my_list.keys())
print(type(my_list.keys()))
print(list(my_list.keys()))
print('#' * 79)

print("2. values() - Returns a list of all the values in the dictionary")
print("The value returned is not a true list since you cannot modify it (like use append() or insert() on it). It is a list-like object that can be turned to a list by passing it to the list() method")
my_list = {1:'a', 2:'b',3:{4:'c', 5:'d'}}
print(my_list.values())
print(type(my_list.values()))
print(list(my_list.values()))
print('#' * 79)

print("3. items() - Returns a list containing a tuple for each key value pair")
print("The value returned is not a true list since you cannot modify it (like use append() or insert() on it). It is a list-like object that can be turned to a list by passing it to the list() method")
my_list = {1:'a', 2:'b',3:{4:'c', 5:'d'}}
print(my_list.items())
print(type(my_list.items()))
print(list(my_list.items()))
print('#' * 79)
print("You can use the list-like objects returned in a for loop to print out the items. You can use the multiple assignment statement to assign the items() return value to different variables")
for key,value in my_list.items():
    print(key, value)

print('#' * 79)


print("4. clear() - Removes all the elements from the dictionary")
print("5. copy() - Returns a copy of the dictionary")
print("6. update() - Updates the dictionary with the specified key-value pairs")
print("7. pop() - Removes the element with the specified key")
print("8. popitem() - Removes the last inserted key-value pair")

print("Two dictionaries are equal if they contain the same key-value pairs: e.g {1:'a', 2:'b', 3:'c'} == {2:'b', 3:'c', 1:'a'} will result to:")
a = {1:'a', 2:'b', 3:'c'}
b = {2:'b', 3:'c', 1:'a'}
print(a == b)

print('#' * 99)
# a program to store friend's birthdays
birthdays = {'Kevin':'Dec 28', 'Naitore':'Jan 14', 'Angule':'Mar 3'}
while True:
    name = input("Enter friend's name (leave blank to quit): ")
    if name == '':
        break
    elif name in birthdays:
        print("{} is the birthday for {}".format(birthdays[name], name))
    else:
        print("Oops! I happen to be missing {}'s birthday".format(name))
        bday = input("When is their birthday? (enter month and date e.g Apr 2): ")
        birthdays[name] = bday
        print("Thankyou! Database Updated")
        print("{} is the birthday for {}".format(birthdays[name], name))


print('#' * 99)

# ORDERED DICTIONARIES IN PYTHON 3.7

print("While they’re still not ordered and have no “first” key-value pair, dictionaries in Python 3.7 and later will remember the insertion order of their key-value pairs if you create a sequence value from them")
print("For example, a list made from the following two dictionaries will match the sequence in which they were created in the dictionary")

got = {'genre':'thriller', 'seasons':8, 'rank':2}
suits = {'rank':6, 'seasons':9, 'genre':'drama'}
print(list(got))
print(list(suits))

print("The same will not work in Python versions before 3.7 i.e the list doesn’t match the insertion order of the dictionary’s key-value pairs when you run this code in say Python 3.5")
print("You shouldn’t rely on this behavior, as dictionaries in older versions of Python don’t remember the insertion order of key-value pairs")
print('#' * 99)
