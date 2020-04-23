# how to represent text data in Python
print("A data type is a particular kind of data item, as defined by the values it can take or the operations that can be performed on it.")
print('#' * 99)
print("Wondering how to deal with text in Python? Well, the string datatype is used to represent text in Python")
print("str (short for String) is a datatype for immutable ordered sequence of characters (any typeable symbol on the keyboard- that includes space, tab, punctuation marks e.t.c)")
print('#' * 79)
print("immutable means once a string object has been declared you cannot alter or change it without creating a new object")
print("ordered means that each character in the string has an index (an integer value that denotes it's position) and can be referenced using that index")
print('#' * 79)
print("Strings are created by wrapping any character(s) in quotes. Both single (') and double (\") quotes can be used")
print("When you have to represent quotes inside the string declaration, use the backslash (\) character to escape the quotes so that Python does not misinterpret the qoutes as the end of the string declaration like shown below:")
print('#' * 79)
greeting = 'Hello world, how\'re ya\'ll doing?'
print("The assignment greeting = 'Hello world, how\\'re ya\\'ll doing?' when printed out will display:", greeting)
reported_speech = "He said, \"There is nothing I can do\""
print('The assignment reported_speech = "He said, \\"There is nothing I can do\\"" when printed out will display:', reported_speech)
print('#' * 79)
print("The '+' and '*' operators can be used on strings to join (append) and repeat strings respectively")
print("Printing 'Hello there, ' + 'hope you are enjoying Python so far' will display:", 'Hello there, ' + 'hope you are enjoying Python so far')
print('#' * 79)
print("Printing 'Repeat' * 20 will display:", 'Repeat' * 20)
print('#' * 79)
print("As you can see above, Python is completely literal when dealing with strings. You have to explicitly add spacing and punctuations if you want them included in your string like below:")
print('#' * 79)
print("'Repeat ' * 20 which now includes a space will display:",'Repeat ' * 20)
print('#' * 79)
print("A few functions  that operate on strings are:")
print("len() returns the number of characters in a string. It begins counting from 1 and includes every character even spaces, tabs, new line characters and punctuation marks e.g len('Hello   world') returns:", len('Hello   world'))
print('#' * 79)
print("Methods are special type of functions that belong to specific objects (depending on their data type) and are called (invoked) using the dot(.) notation e.g")
print("upper() method returns the string in uppercase e.g 'hello world'.upper() will return:", 'hello world'.upper())
print("title() method returns the string with all first letters capitalized e.g 'hello world'.title() will return:", 'hello world'.title())
print("lower() method returns the string in lower case e.g 'ABCDEFGHIJK'.lower() will return:", 'ABCDEFGHIJK'.lower())
print('#' * 79)
print("The first argument in a method function is the object itself that is calling the method. Some methods have extra arguments like the ones below:")
print("count() returns how many occurences of the particular sequence of characters occur in the object it is called on e.g 'she sells sea shells by the sea shore'.count('sea') will output",'she sells sea shells by the sea shore'.count('sea'))
print('#' * 79)
print("find() returns the first occurence (as an index) of a substring in a string object e.g 'she sells sea shells by the sea shore'.find('s') will return:", 'she sells sea shells by the sea shore'.find('s'))
print("rfind() returns the last occurence (as an index) of a substring in a string object e.g 'she sells sea shells by the sea shore'.rfind('sh') will return:", 'she sells sea shells by the sea shore'.rfind('sh'))
print('#' * 79)
print("split() method is a string method that returns a list that contains words from the input string. It takes two additional arguments 'sep' and 'maxsplit'.")
print("The sep (separator) argument is used to specify how the string should be split so as to get the elements (words) which form the list. By default the whitespace is the sep argument. NOTE: THE SEP CANNOT BE AN EMPTY STRING")
print("maxsplit argument provides the maximum number of splits. It gives maxsplit+1 number of elements in the list returned with the remaining string being returned as the last element in the list")
s = "GitHub is built for collaboration. Set up an organization to improve the way your team works together, and get access to more features."
print("For example:")
print("Given a string, s = \"GitHub is built for collaboration. Set up an organization to improve the way your team works together, and get access to more features.\", you can use a comma as the seperator s.split(',') to get the list:\n {}".format(s.split(',')))
print("You can also use a whitespace as the separator and specify the maximum number of splits as follows: s.split(' ', 6) to get \n{}".format(s.split(' ', 6)))
print('#' * 79)
print("format() method is used to replace any number of '{}' placeholders put in a string e.g 'Hey {}, {}'.format('first name', 'last name') will display: ", 'Hey {}, {}'.format('first_name', 'last name'))
print('#' * 79)
print("You can get any character or set of characters from a string by indexing and dicing as shown below:")
print("Indexing (using [] and an integer denoting the index you want) gets you one character at a time. Slicing (using subscripts separated by :(a colon) gets you a subset of characters from the string at a go")
print("You can get the first character in a string like this print('hello world[0]') >>>", 'hello world'[0])
print("You can get the last character in a string like this print('hello world[-1]') >>>", 'hello world'[-1])
print("You can get the first three characters in a string like this print('hello world[0:3]') >>>", 'hello world'[0:3])
print("You can get the last three characters in a string like this print('hello world[-3:]') >>>", 'hello world'[-3:])
print('#' * 79)
print("Python and programming in general uses zero-based indexing i.e it counts starting from zero and not one. This is explicable in the sense that we consider how far a character is from the beginning of the string and the first character is 0 characters away from the start, the second is 1 character away and so on...")
print("Counting from the end, the last character is -1, the second last is -2 and so on...")

print('#' * 79)

escape_characters = {
    "\\'": 'single quote',
    '\\"': 'double quote',
    '\\n': 'new line',
    '\\t': 'tab',
    '\\\\': 'backslash'
}
print("An escape character helps you use characters in a string that would otherwise be impossible to put in. It begins with a backslash followed by the character you want to escape")
for key, value in escape_characters.items():
    print("The {} escape character prints as {}".format(key,value))


print('#' * 79)
