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
print("You can place the letter r lowercase before the beginning quotation mark of a string to make it a raw string")
print("This is the path of your file in windows " + r'c:\\Users\Desktop\Mutwiri\Downloads')
print("This is the path of your file in windows {}".format(r'c:\\Users\Desktop\Mutwiri\Downloads'))
print("Because of the r, Python considers the backslash as part of the string and not the beginning of an escape character")
print("Raw strings are helpful if you are typing string values with a lot of backslashes for example a window's file path like above")
print('#' * 79)

print("For strings that span multiple lines in Python, you can use the multiline strings in Python. These begin and end with triple quotes (three single quotes or three double quotes). Any newline, tab or quotes in between the multiline string are considered part of the string. Escaping strings is not necessary inside the multiline strings")
print(""" 
This is a multiline string.
It spans multiple lines
You don't need to escape any "quotes" here either single or double
    A tab can be added
    A new line can be added
    Python indentation rules for blocks do not appply for multiline strings
""")
print("Multiline strings are also the preferred way to add long comments spanning multiple lines")
print('#' * 79)

print("Putting strings inside strings is a common operations in programming")
print("You can use the + concatenation operation")
name = "Kevin"
age = 25
print(name + " is " + str(age) + " years old.")
print('#' * 79)

print("The above is requires a lot of tedious typing. A better method is using String Interpolation where '%s' is used as a placeholder for the values to be put in then the values are put at the end of the string in order of how they should be put into the string")
print("%s is %s years old" %(name,age))

print('#' * 79)
print("Python 3.6 introduced f-strings which is an even easier way to put strings inside strings. They use {} (curly braces instead of %s) and the values are put directly inside the curly braces. Like r-strings, f-strings have to begin with the f character before the starting quotation mark, otherwise they will be interpreted as being part of the string")
print(f'{name} is {age} years old')
print('#' * 79)

print("upper() and lower() methods do not change the original string. They return a new string value where all the letters have been converted to either uppecase or lowercase. Any non-letter character remains unchanged.")
print("These methods are especially useful when you want to make a case-insensitive comparison. Just simply convert all letters in the target string you want to compare to a similar case with your reference string and compare")
# a small program to do a case-insesitive comparison
feeling = input("How are you feeling? ")
if feeling.lower() == 'great':
    print('I am feeling great too')
else:
    print(f'Why are you feeling {feeling.lower()}?')

print('#' * 79)

print("islower() and isupper() methods return a Boolean True value if there is at least one letter in the string and all the letters are lowercase or uppercase respectively, otherwise it returns False e.g:")
print('12345i'.islower())
print('12345i'.isupper())
print('9023234'.islower())
print('abCdefgh'.islower())
print('pythoniscool'.islower())
print('ASKMEHOW'.isupper())

print('#' * 79)

print("isX() string methods are useful methods that begin with 'is' and return a boolean value that describes the nature of the string")
print()
print("1. isalpha() - returns True if the string consists of only letters and is not empty - otherwise returns False")
print('kevinisaboy'.isalpha())
print('kevin is a boy'.isalpha())
print('kevin2isaboy'.isalpha())


print('#' * 79)

print("2. isdecimal() returns True if the string only consists of numeric characters and is not empty, otherwise returns False")
print("12345".isdecimal())
print("k24".isdecimal())
print("1 2 3 4 5".isdecimal())

print('#' * 79)

print("3. isalnum() returns True if the string consists only of letters and numeric characters and is not blank, otherwise returns False")
print("secr3t".isalnum())
print("hello".isalnum())
print("45".isalnum())
print("123_sed".isalnum())

print('#' * 79)

print("4. isspace() returns True if the string only consists of spaces, tabs, newline characters and is not blank, otherwise returns False")
print("\n".isspace())
print("\t".isspace())
print(" ".isspace())
print("Kevin\ncome here".isspace())


print('#' * 79)

print("5. istitle() method returns True if the string consists of words whose first letter is uppercase and all other letters in the word are lowercase and the string is not blank, otherwise returns False")
print("12345 Is A Title String".istitle())
print("12345".istitle())
print("Is NOt Title".istitle())

print('#' * 79)

print("The isX() methods are useful when you need to validate user input")
# a program to validate different user input using isX() methods

while True:
    name = input("Please input your names (First letter must be capital): ")
    if not name.istitle():
        print("Please capitalize the first letter of each name")
    else:
        print(f"Your name is {name}")
        break
while True:
    age = input("What is your age? ")
    if age.isdecimal():
        print(f"Your age is {age}")
        break
    else:
        print("Please enter a number for your age")
while True:
    password = input("Set up a password (numbers and letters only): ")
    if not password.isalnum():
        print("Please use only letters and numbers")
    else:
        print("Password set up successfully")
        break

print('#' * 79)

print("startswith() and endswith() string methods return True if the string they are called on starts with or ends with the string passed to the methods. They are a good alternative to the '==' operator if you just want to check just the equality of the first or last parts of a string rather than the whole string. It is a case sensitive comparison")

print('Hello world.'.startswith("Hello"))
print('Hello world.'.startswith("hello"))
print('Hello world.'.startswith("Hell"))
print('Hello world.'.endswith("world."))
print('Hello world.'.endswith("world"))
print('Hello world.'.endswith("ld."))

print('#' * 79)

print("join() string method is called on a string, gets passed a list value (of strings) and returns a string")
print("The string returned is a concatenation of each string in the list value with the string join is called on between each element (string) of the list argument")
print("join() method is useful when you have a list of strings you need to be joined into a single string")

print('#' * 79)

print("split() method is called on a string and returns a list of strings")
print("By default the string it is called on is split whenever there is a whitespace character like space or tab. You can change this by passing an argument for the sep parameter (separator) - this is a string value that you want to be used as the split delimiter. The sep is not included in the strings in the returned list")
print()
print("A common use of split is to split a multiline string along the newline character")
letter = '''    
                Mutwiri Mwenda
                P.O BOX 2469
                Meru

    Dear Baby,
    Do not loose hope
    Do not give up on yourself
    I pray God keeps you safe
    
Yours truly,
Beau.
'''
print(letter.split('\n'))

print('#' * 79)
print("the partition() string method can be used to split a string. It is called on a string and passed another string (separator) as argument. The method looks for the string passed as argument in the string it is called on and returns a tuple of three strings - 1. the before, 2. the separator string and 3. the after")
print("Hello Python".partition(' '))

print('#' * 79)

print("If the separator string appears more than once in the string partition() is called on, only the first occurrence is used to split the string")
print("Hey there stranger".partition('er'))
print('#' * 79)

print("If the separator string does not exist in the string partition() is called on, the first string returned in the tuple (before) is the entire string and the other two (separator, after) are empty strings")
print("Programming is fun".partition('p'))

print("The partition() method is useful for splitting a string whenever you need the parts before, including, and after a particular separator string")

print('#' * 79)

print("You can justify text in Python using ljust(), rjust() and center() methods")
print("ljust() and rjust() return a padded version of the string they are called on. The first argument to rjust() and ljust() is an integer length of the string returned e.g calling 'hello'.rjust(10) means the returned string will be of length ten and since the string itself has a length of 5 the remaining length of 5 will be spaces added to the left of the string so the string is justified to the right")
print("Python".ljust(12))
print("Python".rjust(12))

print('#' * 79)
print('#' * 79)
print('#' * 79)
print('#' * 79)





