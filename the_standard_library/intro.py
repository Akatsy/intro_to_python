print("https://docs.python.org/3/library/")
print(r'''
There is an entire library of built-in modules that just come with Python - this is the Python Standard Library

You can import and use these modules which provide new types of objects and functions for a range of common and specialized tasks

Using modules from the Python Standard library to easily access and use existing code gives you a lot of computing power 

The Python Standard Library is organized into modules - many of which are simply Python files like the scripts we write

An import statement runs the code in the module - Running the code will make all the module's functions and types of objects available to use

Modules typically contain a lot of definitions and usually do not show any output

The Python Standard Library has good documentation for each of its modules and it is a good idea to read the relevant page whenever you use one

Modules in the documentation of the Python Standard Library are listed in groups based on their uses. Clicking on a name takes you to the documentation for the module which often has examples as well to test out.
''')

import math
print("Factorial of 9 is ", math.factorial(9))
print("e to the power of 3 is ", math.exp(4))

print('#' * 99)

print(r'''
he Python Standard Library has a lot of modules! Here are a selection of a few Python Standard Library modules and why we use them!

csv: very convenient for reading and writing csv files
collections: useful extensions of the usual data types including OrderedDict, defaultdict and namedtuple
random: generates pseudo-random numbers, shuffles sequences randomly and chooses random items
string: more functions on strings. This module also contains useful collections of letters like string.digits (a string containing all characters which are valid digits).
re: pattern-matching in strings via regular expressions
math: some standard mathematical functions
os: interacting with operating systems
os.path: submodule of os for manipulating path names
sys: work directly with the Python interpreter
json: good for reading and writing json files (good for web work)
''')

print('#' * 99)
