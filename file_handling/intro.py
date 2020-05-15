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
# example of reading information from a file
f = open('/home/mutwiri2/Desktop/intro_to_python/file_handling/if')
f_text = f.read()
f.close()
print(f_text)