print(r'''
There are two types of files:
plain text files - These are files that contain only basic text characters.
binary files - These are all the other kinds of files that contain extra information like font, color, size e.t.c e.g word processing documents, PDFs, images, spreadsheets and executable programs among others
''')

print('#' * 99)

print(r'''
pathlib's read_text() method returns a string of the full contents of a text file
pathlib's write_text() creates a new text file (or overwrites an existing one) with the string passed to it. It returns a count of the number of characters written to the file
These path objects methods only provide basic interactions with files and are not the common way of writing to a file

''')
from pathlib import Path
p = Path('/home/mutwiri2/Desktop/intro_to_python/file_handling/reading_and_writing_files/try.txt')
written_count = p.write_text('Hello, World!')
print(written_count)
content = p.read_text()
print(content)

print('#' * 99)

print(r'''
The more common way of file reading and writing process involves the following steps:
1. call the open() function to return a File object
2. call the read() or write() method on the file object
3. close the file by calling the close() method on the File object
''')

print('#' * 99)

print(r'''
To open a file with the open() function, you pass it a string path indicating the file you want to open; it can be either an absolute or relative path. The open() function returns a File object.
>>>helloFile = open(Path.home() / 'hello.txt')
The open() function can also accept strings e.g
>>> helloFile = open('C:\\Users\\your_home_folder\\hello.txt')  # Windows
>>> helloFile = open('/Users/your_home_folder/hello.txt')   # MacOS

the above commands will open the file in “reading plaintext” mode, or read mode for short. When a file is opened in read mode, Python lets you only read data from the file; you can’t write or modify it in any way. Read mode is the default mode for files you open in Python. But if you don’t want to rely on Python’s defaults, you can explicitly specify the mode by passing the string value 'r' as a second argument to open(). So open('/Users/your_home_folder/hello.txt', 'r') and open('/Users/your_home_folder/hello.txt') do the same thing.

The call to open() returns a File object. A File object represents a file on your computer; it is simply another type of value in Python, much like the lists and dictionaries.  you store the File object in the variable helloFile. Now, whenever you want to read from or write to the file, you can do so by calling methods on the File object in helloFile.
''')

print('#' * 99)

print(r'''
If you want to read the entire contents of a file as a string value, use the File object’s read() method
>>> content = helloFile.read()
>>> content
'Hello, world!'


Alternatively, you can use the readlines() method to get a list of string values from the file, one string for each line of text
A list of strings is often easier to work with than a single large string value

''')
if_poem = open('/home/mutwiri2/Desktop/intro_to_python/file_handling/if')
poem_lines =  if_poem.readlines()
if_poem.close()
print(poem_lines)

print('#' * 99)

print(r'''
To write to a file, you need to open it in “write plaintext” mode or “append plaintext” mode, or write mode and append mode for short

Write mode will overwrite the existing file and start from scratch, just like when you overwrite a variable’s value with a new value. Pass 'w' as the second argument to open() to open the file in write mode

Append mode, on the other hand, will append text to the end of the existing file. You can think of this as appending to a list in a variable, rather than overwriting the variable altogether. Pass 'a' as the second argument to open() to open the file in append mode.

If the filename passed to open() does not exist, both write and append mode will create a new, blank file. 

After reading or writing a file, call the close() method before opening the file again

>>> greetings_file = open('greetings.txt', 'w')   
>>> greetings_file.write('Hello! hey! alloha!\n')
    20
>>> greetings_file.close()
>>> greetings_file = open('greetings.txt', 'a')
>>> greetings_file.write('How do you do? Hakuna matata?')
    29
>>> greetings_file.close()
>>> greetings_file = open('greetings.txt')
>>> content = greetings_file.read()
>>> greetings_file.close()
>>> print(content)
Hello! hey! alloha!
How do you do? Hakuna matata?

Note that the write() method does not automatically add a newline character to the end of the string like the print() function does. You will have to add this character yourself.

As of Python 3.6, you can also pass a Path object to the open() function instead of a string for the filename
''')

greetings_file = open('/home/mutwiri2/Desktop/intro_to_python/file_handling/reading_and_writing_files/greetings.txt', 'w')   
print(greetings_file.write('Hello! hey! alloha!\n'))
greetings_file.close()
greetings_file = open('/home/mutwiri2/Desktop/intro_to_python/file_handling/reading_and_writing_files/greetings.txt', 'a')
print(greetings_file.write('How do you do? Hakuna matata?'))
greetings_file.close()
greetings_file = open('/home/mutwiri2/Desktop/intro_to_python/file_handling/reading_and_writing_files/greetings.txt')
content = greetings_file.read()
greetings_file.close()
print(content)

print('#' * 99)

print(r'''
You can save variables in your Python programs to binary shelf files using the shelve module - this way your programs can restore data to variables from the HDD
To read and write data using the shelve module:
1. import the shelve module
2. call shelve.open() and pass it a filename and then store the returned value in a variable
3. You can make changes to the shelf value as if it were a dictionary
4. Call close() on the shelve value once done
''')

import shelve
shelf_file = shelve.open('/home/mutwiri2/Desktop/intro_to_python/file_handling/reading_and_writing_files/my_data')
likes = ['mercedes', 'Prado Tx', 'Lexus LX500', 'macbook', 'iphone', '80 inch screen', 'big derriere wife']
shelf_file['likes'] = likes
shelf_file.close()

print(shelf_file)
print(type(shelf_file))

print('#' * 99)

print(r'''
As of Python 3.7, you have to pass the open() shelve method filenames as strings - you cannot pass path objects
Windows creates 3 files - my_data.dat, my_data.bak, my_data.dir
MacOs and Linux create one file - my_data.db
The binary file my_data.db contains the data you stored in the shelf file
shelve module frees you from worrying about how to store your program's data to a file
Your program can use the shelve module to later reopen and retrieve the data from these shelf files
shelf values do not have to be opened in read or write mode - they can do both once opened
''')
shelf_file = shelve.open('/home/mutwiri2/Desktop/intro_to_python/file_handling/reading_and_writing_files/my_data')
print(shelf_file['likes'])
shelf_file.close()

print('#' * 99)

print(r'''
Just like dicts, shelf files have keys() and values() methods that will return list-like values of the keys and values in the shelf
The values returned are not true lists but we can pass them to list() to convert them to list values
''')

shelf_file = shelve.open('/home/mutwiri2/Desktop/intro_to_python/file_handling/reading_and_writing_files/my_data')
goals = ['Python', 'Javascript', 'CCNA', 'ethical hacker']
shelf_file['goals'] = goals
shelf_file.close()

shelf_file = shelve.open('/home/mutwiri2/Desktop/intro_to_python/file_handling/reading_and_writing_files/my_data')
print(list(shelf_file.keys()))
print(list(shelf_file.values()))
shelf_file.close()

print('#' * 99)
