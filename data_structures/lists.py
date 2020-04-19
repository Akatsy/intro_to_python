# use the list data structure (container) to group and organize objects (elements) of various data types 
print("Data structures are containers of data that organize and group different kinds of data types together in different ways")
print("All data structures are data types- Because data types are just a way to classify data- and data structures do that")
print("These containers give Python much more power to develop complex programs. The data structures in Python are: \n\t{} \n\t{} \n\t{} \n\t{}".format("1. lists", "2. tuples", "3. sets", "4. dictionaries" ))
print('#' * 79)
print("The list is one of the most common and basic data structure in Python.\n It is a data structure (data type) for a mutable ordered sequence of elements")
print("'mutable' means it can be altered / changed after being created without neccessarily creating a new object.\n 'ordered' means each element in a list has an index (an integer value that defines it's position in the list) and can be referenced / obtained using that index")
print('#' * 79)
print("Lists are created / defined using square brackets [] and can contain elements of any data type (integer, float, boolean, strings) or even another data structure (container of data e.g another list)")
list_of_random_things = [1, 2.5, 'hello', True, -5, -0.9, '\\', False]
print("This is a list comprising of objects of different data types: {}".format(list_of_random_things))
print('#' * 79)
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
print("Given a list of months like this; months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']: we can index into the list to get an individual month or slice the list to get a subsequence of the list as follows;")
print('#' * 79)
print("Get the first month using indexing as follows: months[0]- {}".format(months[0]))
print("Get the last month using indexing as follows: months[-1]- {}".format(months[-1]))
print("Get the first three months using slicing notation as follows: months[0:3]- {}".format(months[0:3]))
print('#' * 79)
print("Note that indexing starts from zero (counting from the beginning, the first index is zero and counting from the rear, index starts from -1) and the slicing uses a lower bound and an upper bound separated by a full colon(:) where the lower bound (lower index) is inclusive (included in the result) and the upper bound (upper index) is exclusive (excluded from the result)")
print('#' * 79)
print("Slicing using subscript notation has shortcuts as follows:\n\t{}, {}, \n\t{}, {}".format("If the lower bound is from the start of the list, you can ommit the 0 (start index) index and just give the upper bound e.g to print the first six months; months[:6]", months[:6], "If the upper bound is up to the end of the list, you can ommit the last index and just give the lower bound e.g to print the last six months; months[6:] or months[-6:]", months[-6:]))
print('#' * 79)
print("If you try accessing an index that does not exist, you wil get a list index error exception. However, if you try to slice using bounds that are of indexes that do not exist in the list (either upper or lower bounds), you will just get an empty list back and not an error")
print('#' * 79)
print("List is a type just like int, float, str thus calling the type() function on it will give you:", type(months)) 
print('#' * 79)
print("The data type closest to a list is the string as both share some commonalities:\n\t1.Both are an ordered sequence of elements- the list being a sequence of elements of various data types separated by commas and delimited using square brackets and the string being an ordered sequence of characters wrapped in quotation marks.\n\t2.Both support indexing i.e you can access any element using it's index in the string or list starting with index 0 from the front and -1 from the back.\n\t3.Both also support the len() function which returns the total number of elements in a list and the number of characters in a string including punctuations and spaces, new lines, tabs (simply any typeable character on the keyboard) counting from 1")
print('#' * 79)
print("The most notable difference between a string and list is that strings are immutable (cannot be changed once created unless by creating a new object) while lists are mutable (can be changed once created without having to create a completely new object)")
print('#' * 79)
print("Lists can be mutated (changed) in the following ways:")
print('#' * 79)
months.append('Pythoncember')
print("Using the append method which adds an element (one at a time) to the end of the list e.g we can add an 'imaginary' month to the end of our months list as follows months.append('Pythoncember') and printing the months list would reflect the new month:", months)
print('#' * 79)
months[0] = 'Jan'
print("Using the indexing notation, we can alter any index (valid index i.e an index that exists in the list) and assign it a new value e.g we can change the first month to a short form like so months[0] = 'Jan' and printing it out print(months) we see the change:", months)
print('#' * 79)
print("Using the del comand to delete any element by referencing it's index or delete multiple elements using the slicing notation or just delete the whole list by inputing it as the argument to the del function")
print('#' * 79)
months[:4] = ['Jan', 'Feb', 'Mar', 'Apr']
print("Using the slicing notation, we can alter any indices (valid indices i.e an index that exists in the list) or even indices that do not exist (Python will create new indices for them) and assign them a new value e.g we can change the first four months to a short form like so months[:4] = ['Jan', 'Feb', 'Mar', 'Apr'] and printing it out print(months) we see the change:", months)
print('#' * 79)
print("Note: When assigning values to variables, the variable is just a name for the value and the value is what gets stored in memory. (If you assign a value to a variable and then assign that variable to another variable, the value stored in that initial variable is what is stored in the new variable) thus there is a difference when we use two (or more) variables (names) to refer to the same value and alter one of them depending on whether that value is of a mutable or immutable type")
print('#' * 79)
print("If the type is immutable, then changing the value of one of the variables by reassigning does NOT change the value of the other variables that referenced the same value".upper())
print("If the type is mutable, then changing the value of one of the variables by reassigning changes the value of the other variables that referenced the same value".upper())
print('#' * 79)
print("Lists have a couple of methods that are helpful:")
print("len() returns the number of elements in the list e.g the len(months) is:", len(months))
print('#' * 79)
print("max() returns the largest element in the list. This is because it is defined using the greater than (>) operator. The result of this method is dependent on the contents of the list as follows:")
print("If the elements in the list are numbers, then max returns the largest number e.g max([20, 585, 67.90, -5, 456]) will return:", max([20, 585, 67.90, -5, 456]))
print('#' * 79)
print("If the elements in the list are a string, then max returns the string that would come last if the list was sorted alphabetically e.g max(['she', 'sells', 'sea','shells, 'by', 'the', 'sea', 'shore']) will return:", max(['she', 'sells', 'sea','shells', 'by', 'the', 'sea', 'shore']))
print('#' * 79)
print("min() returns the smallest element in the list. This is because it is defined using the less than (<) operator. The result of this method is dependent on the contents of the list as follows:")
print("If the elements in the list are numbers, then min returns the smallest number e.g min([20, 585, 67.90, -5, 456]) will return:", min([20, 585, 67.90, -5, 456]))
print('#' * 79)
print("If the elements in the list are a string, then min returns the string that would come first if the list was sorted alphabetically e.g max(['she', 'sells', 'sea','shells, 'by', 'the', 'sea', 'shore']) will return:", min(['she', 'sells', 'sea','shells', 'by', 'the', 'sea', 'shore']))
print('#' * 79)
print("While a list can have a mix and match of data types, the max and min methods are undefined for lists that consist of incomparable data types e.g int and strings will produce a TypeError")
print('#' * 79)
print("The join() method is a string method that takes a list of elements that must be strings as an argument and returns a string that is the elements of the list separated by a separator string. The separator string is supplied before the method and invokes (calls) the method using the dot operator e.g we can return our months list each month on a new line as follows '\\n'.join(months) :\n", '\n'.join(months))
print('#' * 79)
print("The split method is a string method that returns a list that contains the words from the input string. It is like a reverse of the join method e.g 'she sells sea shells by the sea shore'.split() will return: ", 'she sells sea shells by the sea shore'.split())
print('#' * 79)
print("The split method can take two more arguments, the maxsplit and the sep (separator). These define what string Python should use as the delimiter (space is the default) and the maximum number of splits (which returns the given number+1) elements in the list. The last element is what remains after the maxsplit is achieved)")
print('#' * 79)
print("The sorted() method returns a copy of the list with its elements arranged in ascending order. You can supply an extra argument to the method reverse=True to get the result in descending order e.g our months list -\n\t ascending: {}, \n\tdescending: {}".format(sorted(months), sorted(months, reverse=True)))
print('#' * 79)
print("The list() constructor returns a list in Python.")
print("The list() constructor takes a single argument - iterable (optional) - an object that could be a sequence (string, tuples) or collection (set, dictionary) or any iterator object")
print("The list() constructor returns a list. If no parameters are passed, it returns an empty list. If iterable is passed as a parameter, it creates a list consisting of iterable's items.")
print("For example:")
print("Printing an empty list - print(list() would print out: {}".format(list()))
print("Printing a list created from a string of vowels - print(list('aeiou') would print out: {}".format(list('aeiou')))

print('#' * 99)

# tuple unpacking / multiple assignment on lists
print("Tuple unpacking is a shorthand that lets you assign multiple variables with values in a list in one line of code. The number of variables must match the number of items in the list otherwise, Python throws an error")
print("For example consider the following and what is printed out:\nvowels = ['a','e','i','o','u']\nfirst,second,third,fourth,fifth = vowels\nprint(first,second,third,fourth,fifth,sep='\n')")
vowels = ['a','e','i','o','u']
first,second,third,fourth,fifth = vowels
print(first,second,third,fourth,fifth, sep='\n')

print('#' * 99)
# a program to enter any number of names to a list
a_list = []
while True:
    element = input("Enter a name {} or nothing to stop: ".format(len(a_list)+1))
    if element == '':
        break
    else:
        a_list.append(element)
print("The names entered are:")
for object in a_list:
    print(object)

print('#' * 99)

# random module functions that accept list for arguments
print("The random module has some functions that accept lists for arguments")
print("random.choice() returns a random item from the list supplied as an argument")
import string, random
alphabets = [letter for letter in string.ascii_letters]
print(random.choice(alphabets))

print('#' * 99)
print("random.shuffle() will re-order the items in a list. This function modifies a list in place rather than returning a new list")
random.shuffle(alphabets)
print(alphabets)

# add (concatenate) lists or replicate lists using the '+' and '*' operators
print('#' * 99)
print("We can add (concatenate) lists or replicate lists using the '+' and '*' operators")
alphabets += string.digits
print(alphabets)
alphabets *= 4
print(alphabets)

print('#' * 99)
# index() method to find index of a value in a list

print("List values have an index() method that can be passed a value, and if that value exists in the list, the index of the value is returned. If the value isn’t in the list, then Python produces a ValueError error")
print("When there are duplicates of the value in the list, the index of its first appearance is returned")

spam = ['hello', 'hi', 'howdy', 'alloha']
# spam.index('Hello') # gives a ValueError - 'Hello' not in list
print(spam.index('hi'))

print('#' * 99)

# insert() method to add an element to a list at any position
print("append() method adds the argument to the end of the list. The insert() method can insert a value at any index in the list. The first argument to insert() is the index for the new value, and the second argument is the new value to be inserted.")
a = [1,2,3]
a.insert(3,4)
print(a)
a.insert(1,0)
print(a)
a.insert(10,10)
print(a)

print('#' * 99)

# remove() method to remove a value from the list
print("The remove() method is passed the value to be removed from the list it is called on")
a = [1,2,3,4,5,4]
a.remove(4)
print(a)

print("Attempting to delete a value that does not exist in the list will result in a ValueError error")
print("The del statement is good to use when you know the index of the value you want to remove from the list. The remove() method is useful when you know the value you want to remove from the list")

print('sidenote : The del statement can also be used on a simple variable storing a value like int, string, float or boolean to delete it - think of it like unassignment operation.'.upper())

print('#' * 99)

# sorting values in a list using sort() method - different from sorted()
print("sort() uses “ASCIIbetical order” rather than actual alphabetical order for sorting strings. This means uppercase letters come before lowercase letters. Therefore, the lowercase a is sorted so that it comes after the uppercase Z")
print("For example:")
names = ['Ann', 'alice', 'Ben', 'Zippy', 'Candice']
names.sort()
print(names)

print("If you need to sort the values in regular alphabetical order, pass str.lower for the key keyword argument in the sort() method call like below")
names.sort(key=str.lower)
print(names)

print('#' * 99)

# print(sorted(names,key=str.lower)) - also applies to the sorted() function

# reverse a list using reverse() method
print("If you need to quickly reverse the order of the items in a list, you can call the reverse() list method")
print("for example:")
animals = ['cats','dogs','rats', 'snakes']
animals.reverse()
print(animals)

print('#' * 99)
