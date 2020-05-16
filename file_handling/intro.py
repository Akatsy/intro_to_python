print("All kinds of files have a similar structure on a computer i.e they are just strings of characters that encode some information")
print("The specific file format often indicated by the extension of the file name e.g .py, .txt, .jpg, .htm, .csv e.t.c will indicate how those characters are organized")
print("These characters in a file are interpreted by the programs we use to interact with them e.g an image editing program will interpret the information of a digital photograph file and display the image. If we edit the image, then we are using the program to change characters in the file")

print('#' * 99)

print("In Python, we can read a file's characters directly")
print("Opening files in Python gives us a common programmatic interface to all kinds of files without the need for a GUI which means we can automate tasks involving files with Python programs")

print('#' * 99)

print(r'''
This is how to read information from a file into Python:
1. Open the file using the built in function open()
>>>f = open('/path/to/file.txt', 'r')

Open takes in a string with the path to the file as the first parameter, and another string as the second parameter that specifies the mode we want to open the file in - 'r' is for 'read mode' meaning we just want to access the contents of the file and not modify anything. (If not specified the mode defaults to read)
open() returns a file object which is a Python object through which Python interacts with the file itself.
Once we have opened a file and created a file object, we can use the read method to access the contents of this file.

2. The file object's read() method takes the text contained in a file and puts it into a string and returns that string
>>>file_data = f.read()
>>>print(file_data)

3. When you have finished with a file, you should close it using the file object's close() method
>>>f.close()
''')

print('#' * 99)

print("Always remember to close files that you have opened once you no longer need them because if you open a lot of files without closing them, you can run out of file handles and you will not be able to open any new files")
print("Exactly how many files you can open before running out of handles will depend on your OS")

print('#' * 99)

print("The file is a long stream of characters and the file object can look at only one character at a time")

print('#' * 99)

# example of reading information from a file
f = open('/home/mutwiri2/Desktop/intro_to_python/file_handling/if')
f_text = f.read()
f.close()
print(f_text)

print('#' * 99)

print(r'''
You can also write to a file in which case, you change the contents of a file. To write to a file, take the following steps:
1. open the file in write ('w') mode
>>>f = open('/home/mutwiri2/Desktop/intro_to_python/file_handling/some_file.txt', 'w')
NOTE: IF THE FILE DOES NOT EXIST PYTHON WILL CREATE IT FOR YOU.
    BE CAREFUL BECAUSE WHEN YOU OPEN A FILE IN WRITE MODE, ANYTHING CONTAINED PREVIOUSLY WILL BE DELETED.
    IF YOU JUST WANT TO ADD TO AN EXISTING FILE, USE THE append ('a') MODE INSTEAD OF write ('w')
>>>f = open('/home/mutwiri2/Desktop/intro_to_python/file_handling/some_file.txt', 'a')

2. Once you have opened the file, you can use the write() method to add content to it
>>>f.write('Content added to file')
or append to it if in append mode
>>>f.write('Content appended to file')

3. Finally, always remember to close the file with close() method
>>>f.close()
    
''')

print('#' * 99)

# write and append to a file example
f = open('/home/mutwiri2/Desktop/intro_to_python/file_handling/some_file.txt', 'w')
f.write('Content added to file with write()')
f.close()
f = open('/home/mutwiri2/Desktop/intro_to_python/file_handling/some_file.txt', 'a')
f.write('Content added to file with append()')
f.close()
f = open('/home/mutwiri2/Desktop/intro_to_python/file_handling/some_file.txt')
f_text = f.read()
f.close()
print(f_text)

print('#' * 99)

print(r'''
Python provides a special syntax that autocloses a file for you because it is easy to forget to close a file once you have operated on it
The with keyword allows you to open a file, do operations on it and automatically close it after the indented code is executed
>>>with open('some_file.txt', 'r') as f:
        file_data = f.read()
    print(file_data)

Once you have left the indented block of code, the file is closed and you are not able to interact with it. However, the data we had read into the variable file_data is not lost and can be accessed outside the with block
''')

print('#' * 99)

print(r'''
Assuming a file object is stored in a variable f:
To read the file’s contents, we call f.read(size), which reads some quantity of data and returns it as a string (in text mode) or bytes object (in binary mode).
size is an optional numeric argument.
When size is omitted or negative, the entire contents of the file will be read and returned; it’s your problem if the file is twice as large as your machine’s memory.
Otherwise, at most size characters (in text mode) or size bytes (in binary mode) are read and returned.
If the end of the file has been reached, f.read() will return an empty string ('')

If you pass an integer argument to read(), it will read up to that number of characters, output them and then keep the window at that position ready to read on.
''')
with open('/home/mutwiri2/Desktop/intro_to_python/file_handling/if') as f:
    print(f.read(2))
    print(f.read(8))
    print(f.read(16))

print('#' * 99)


with open('/home/mutwiri2/Desktop/intro_to_python/file_handling/if') as f:
    print(f.read(-1))

print('#' * 99)
