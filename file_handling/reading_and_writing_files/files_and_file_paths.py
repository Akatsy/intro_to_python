print("Variables store data when a program is running")
print("Files persist data after a program has stopped running")
print("File's content - Think of it as a single string value potentially gigabytes in size")

print('' * 99)

print("A file has two key properties:")
print("1. filename - this is the name of the file (usually written as one word) - Additionally (optional in some OS like Linux) the part of the filename after the last period character is called the file's extension and tells you the file's type i.e what kind of file it is e.g .py specifies it is a python file")
print("2. path - This specifies the location of a file on the computer")

print('' * 99)

print("Operating systems differ on how they handle filenames and paths as shown below:")
print("This is a file named hello.py located on the Desktop of different OS under a folder called programs")
print(r"Windows - C:\Users\mutwiri-2\Desktop\programs\hello.py")
print(r"Linux - /home/mutwiri-2/Desktop/programs/hello.py")
print(r"MacOs - /Users/mutwiri-2/Desktop/programs/hello.py")

print('' * 99)

print(r"On Windows, the path begins from C:\ which is called the root folder i.e the folder that contains all other folders.")
print("Users, mutwiri-2, Desktop and programs are all folders (or directories) and hello.py is the name of the file. That means hello.py is a file located inside the programs folder which is itself located inside the Desktop folder located inside mutwiri-2 folder which is located inside the Users folder which is then located in the root folder.")

print('' * 99)

print("On Linux and MacOs, path begins from / (root folder) as shown above")

print('' * 99)

print("Additional volumes like USB flash drives will appear differently on various OS")
print(r"Windows - Appear as new lettered root drives e.g D:\ or F:\ ")
print(r"MacOs - Appear as new folders under the /Volumes folder")
print(r"Linux - Appear as new folders under the /mnt ('mount') folder")

print('' * 99)

print("Windows paths are written using backslashes as the separator between folders names. Linux and MacOs use forward slashes as the path separator between folder names")
print("For your program to work on all operating systems, write your Python scripts to handle both cases")

print('' * 99)

print("The Path() function in the pathlib module when passed string values of individual file and folder names in a path will return a string with a file path using the correct path separators")
from pathlib import Path
print(Path('Desktop', 'Programs', 'hello.py'))
print(str(Path('Desktop', 'Programs', 'hello.py')))
print(type(Path('Desktop', 'Programs', 'hello.py')))

print("Calling Path() on Windows returns a WindowsPath object while Linux returns a PosixPath object (Posix is a set of standards for Unix-like operating systems.)")
print("You can pass the object returned to the str() function to get a simple text string of the path")
print("By using the statement 'from pathlib import Path' we avoid having to call pathlib.Path everywhere Path appears in our code")

print('' * 99)

print("Path objects are passed to file-related functions e.g below is a code snippet to join names from a list to the end of a folder's name:")
file_list = ['index.html', 'index.css', 'img/img1.jpg']
for filename in file_list:
    print(Path(r'/home/mutwiri2/Desktop/webpage', filename))

print('' * 99)

print("On Windows, the backslash is used as a separator for directories thus it cannot be used on a filename. On Linux and MacOs, however the backslash can be used in a filename")
print("For this reason, it is usually a good idea to use forward slashes in your Python code and the pathlib module will ensure that it always works on all operating systems")

print('' * 99)

print("The / operator normally used for division can be used to combine Path objects and strings")
print("The pathlib module solves the problem of joining paths correctly on all operating systems your code is running on by simply using the '/' operator without having to write a large amount of code to handle all exceptions that might be raised if we were to use other string operations like the append (+) operator or the join() method to join paths")

print('' * 99)

print("When using the / operator for joining paths, one of the first two values must be a Path object")
print("Python evaluates the / operator from left to right and evaluates to a Path object so either the first or second leftmost value must be a Path object for the entire expression to evaluate to a Path object")
print("If you get a TypeError: unsupported operand type(s) for /: 'str' and 'str' it means you have not put a Path object on the left side of the operator")
print("The / operator replaces the older os.path.join() function")

print('' * 99)