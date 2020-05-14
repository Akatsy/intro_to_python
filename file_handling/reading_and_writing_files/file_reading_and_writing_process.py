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
