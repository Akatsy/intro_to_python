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
