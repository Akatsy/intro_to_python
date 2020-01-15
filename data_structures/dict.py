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
print("When you declare a variable and assign it an empty set of curly braces, it is assigned the type dict e.g n = {} and type(n) will give; ", type(n))
print("When you declare a variable and assign it to the constructor dict() like this m = dict(), it is assigned the type dict and type(m) will give; ", type(m))
print('#' * 79)
print("The key(sorrounded by square brackets, []) in a dict can be used to access a value, change a value or add a new object to a dict as follows:")
print("we can print out the value of the brand in our list above like this thisdict['brand'] to get", thisdict['brand'])
print('#' * 79)
thisdict['brand']='mercedes'
print("we can change the value of the brand in our list above like this thisdict['brand']='mercedes' and printing out the value, we get: {}".format(thisdict))
print('#' * 79)
thisdict['make']='c200'
print("we can add a new object to our list above like this thisdict['make']='c200' and printing out the dict we see our new object: {}".format(thisdict))
print('#' * 79)
print("There are a few methods that are useful for operating on lists:")
print("The get() method looks up to see if a key exists in the dict and if it does, returns the value of that key. If it does not exist, it returns the keyword None(by default) or another user defined response: e.g")
print('#' * 79)
cc = thisdict.get('cc', 'The carrying capacity does not exist')
print("We can look for a key 'cc' in our existing dict and if it does not exist print a message 'The carrying capacity does not exist' like this cc = thisdict.get('cc', 'The carrying capacity does not exist') and printing out the variable cc 'print(cc)' that stores the return value we get:",cc)
print('#' * 79)
print("The get() method is a better way to acces a value from a key in a dict than using just the square brackets and the key value like; thisdict['cc'] which returns an error if the key does not exist. Errors cause programs to break which is bad, so if you anticipate that a key might not exist, it is better to use the get() method which returns None or a custom message.")
print('#' * 79)
print("The dict data structure supports the membership operators 'in' and 'not in' which return a bool value of whether a key exists in the dict or not e.g:")
print("'year' in thisdict returns {} and 'cc' not in thisdict returns {}".format('year' in thisdict, 'cc' not in thisdict))
print('#' * 79)
print("Compound data structures can be formed by combining collections of data together. Collections of data are any of the data structures(containers of data) i.e lists, tuples, sets and dicts")
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