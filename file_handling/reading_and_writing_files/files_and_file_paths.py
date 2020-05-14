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

print("Every program that runs on your computer has a current working directory and any filenames or paths that do not begin with the root folder are assumed to be under the current working directory")
print("You can get the cwd as a string value  with the Path.cwd() function and you can change it using the os.chdir() function")
print(Path.cwd())
import os
os.chdir('/home/mutwiri2/Desktop')
print(Path.cwd())
os.chdir('/home/mutwiri2')
print(Path.cwd())
os.chdir('/home/mutwiri2/Desktop/intro_to_python')
print(Path.cwd())


print('' * 99)

print("Python will display an error if you try to change to a directory that does not exist")
print("There is no pathlib function to change the cwd because changing the cwd while a program is running can lead to subtle bugs")
print("os.getcwd() is the older way of getting the cwd as a string")

print('' * 99)

print("All users have a folder for their own files on the computer called the home directory / home folder. The home folders are located in a set place depending on the OS")
print(r'''
    Windows - C:\Users
    MacOs - /Users
    Linux - /home
''')

print("You can get a Path object for the home folder by calling Path.home()")
print(Path.home())
print("home folder is an ideal place to keep the files that your Python programs will be working with as your scripts will have permission to read and write the files under your home directory")

print('' * 99)

print('''
    There are two ways to specify a path:
    i. Absolute path - Always begins at the root folder
    ii. Relative path - Relative to the program's current working directory

    Additionally, there are two other folders - the dot (.) and dot-dot (..) folders which are not real folders but specified names that can be used in file paths
    dot (.) - means 'this directory' and is optional to be added before a relative path
    dot-dot (..) - means the "parent directory i.e the directory inside which that path is in"

''')

print('' * 99)

print(r'''
    Your program can create new folders (directories) using the os.makedirs() function
    os.makedirs() will create any neccessary intermediate folders in order to ensure that the full path exists
    e.g 
    >>> import os
    >>> os.makedirs('C:\\img\\backgrounds\\patterns')

    In the code above, os.makedirs() would create all the folders and subfolders if they did not exist to make sure that full path exists
''')

# os.makedirs('/home/mutwiri2/Desktop/does/this/work?') # uncomment to make directories
# os.removedirs('/home/mutwiri2/Desktop/does/this/work?')  # uncomment to remove the above created folders

print('' * 99)

print(r'''
    To make a directory from a Path object, call the mkdir() method
    >>> from pathlib import Path
    >>> Path(r'C:\Users\mutwiri2\Webpage\').mkdir()

    Note that mkdir() method can only make one directory at a time and it will not make several subdirectories at once like the os.makedirs() function
''')

# Path('/home/mutwiri2/Desktop/try').mkdir() # uncomment to create non-existing directory
# Path('/home/mutwiri2/Desktop/try').rmdir() # uncomment to remove existing directory


print('' * 99)

print("Calling the is_absolute() method on a Path object will return True if it represents an absolute path or False if it represents a relative path")
print(Path.cwd().is_absolute())
print(Path('webpage/img').is_absolute())


print('' * 99)

print(r'''
To get an absolute path from a relative path, you can put 'Path.cwd()/' infront of the relative path since when we say 'relative path' we almost always mean a path that is relative to the current working directory
>>>Path('my/relative/path')
WindowsPath('my/relative/path')
>>>Path.cwd()/Path('my/relative/path')
WindowsPath('C:/Users/mutwiri2/AppData/Local/Programs/Python/Python37/my/relative/path')
''')

print(Path.cwd() / Path("my/relative/path"))

print('' * 99)

print(r'''
To get an absolute path from a relative path that is not thw cwd, you can put that path infront of the relative path e.g to get an absolute path from the home directory:
>>>Path('my/relative/path')
WindowsPath('my/relative/path')
>>>Path.home()/Path('my/relative/path')
WindowsPath('C:/Users/mutwiri2/my/relative/path')
''')

print(Path.home() / Path("my/relative/path"))

print('' * 99)

print(r'''
The os.path module has useful functions when it comes to relative and absolute paths
    1. Calling os.path.abspath(path) will return a string of the absolute path of the argument. This is an easy way to convert a relative path into an absolute one
    2. Calling os.path.isabs(path) will return True if the argument is an absolute path and False if it is a relative path.
    3. Calling os.path.relpath(path, start) will return a string of a relative path from the start path to path. If start is not provided, the current working directory is used as the start path.

''')

print('' * 99)

print(os.path.isabs('.'))
print(os.path.abspath('.'))
print(os.path.isabs(os.path.abspath(',')))

print('' * 99)

print(os.path.relpath("/home/mutwiri2"))
print(os.path.relpath("/home/mutwiri2", "/etc/pwd"))

print("\nWhen the relative path is within the same parent folder as the path, but is within subfolders of a different path, such as 'C:\\Windows' and 'C:\\spam\\eggs', you can use the “dot-dot” notation to return to the parent folder")

print('' * 99)

print(r'''
Given a Path object, you can extract the file path's different parts as strings using several Path object attrinbutes
The parts of a file path include:
1. the anchor - This is the root folder of the file system
2. the drive (on Windows OS only) - The single letter that often denotes a physical HDD or other storage device - (does not include the first backslash)
3. the parent - the folder that contains the file - evaluates to a Path object not a string like the other attributes
4. the name of the file - made up of; stem (or base name) and the suffix (or extension)

To extract each attribute from the file path:
>>>p = Path('C:/Users/mutwiri2/spam.txt')
>>>p.anchor
'C:\\'
>>>p.parent
'WindowsPath('C:/Users/mutwiri2) # This is a path object not a string
>>>p.name
'spam.txt'
>>>p.stem
'spam'
>>p.suffix
'.txt'
>>>p.drive
'C:'
''')

print('' * 99)

# parts of a file path on Linux
p = Path.cwd()/ Path('file_handling/reading_and_writing_files/files_and_file_paths.py')
print(p)
print(p.anchor) # root folder of the system
print(p.parent) # folder that contains the file
print(p.name) # name of the file
print(p.stem) # base name
print(p.suffix) # extension
print()
p = Path.cwd()/ Path('file_handling/if')
print(p)
print(p.anchor) # root folder of the system
print(p.parent) # folder that contains the file
print(p.name) # name of the file
print(p.stem) # base name
print(p.suffix) # extension
print(type(p.suffix)) # empty suffix

print('' * 99)

print("The parents attribute which is different from the parent attribute evaluates to the ancestor folders of a Path object with an integer index")
p = Path.cwd()
print(p)
print(p.parents[0])
print(p.parents[1])
print(p.parents[2])
print(p.parents[3])
# print(p.parents[4]) - gives an index error if there is no ancestor

print('' * 99)

print(r'''
os.path.dirname(path) returns a string of everything that comes before the last slash in the path argument
os.path.basename(path) returns a string of everything that comes after the last slash in the path argument
>>>example_path = 'C:\\Windows\\System32\calc.exe
>>>os.path.dirname(example_path)
'C:\\Windows\\System32'
>>>os.path.basename(example_path)
'calc.exe'
''')

example_path = '/etc/python3/debian_config'
print(os.path.dirname(example_path))
print(os.path.basename(example_path))
print(type(os.path.dirname(example_path)))

print('' * 99)

print(r'''
If you need both the os.path.dirname and os.path.basename, you can call os.path.split() which returns a tuple of strings with the dir name and base name of the path passed as argument
>>>os.path.split('example_path')
('C:\\Windows\\System32', 'calc.exe')
''')
print(os.path.split(example_path))

print('' * 99)

print(r'''
To get all the parts of a path as a string, use the split() string method and split on the string in os.sep
os.sep variable is set to the correct folder-separating slash for the Operating system your code is running on - i.e '\\' for Windows and '/' for MacOs and Linux
>>>example_path.split(os.sep)
['C:', 'Windows', 'System32', 'calc.exe']
''')
print("In Linux and Mac, the returned list from split() will begin with a blank string")
print(example_path.split(os.sep))
print('' * 99)
