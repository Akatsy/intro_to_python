print("https://docs.python.org/3/library/")
print(r'''
All Python programs can call a basic set of functions called built-in functions
e.g print(), input() e.t.c

There is an entire library of built-in modules that just come with Python - this
is the Python Standard Library

You can import and use these modules which provide new types of objects and 
functions for a range of common and specialized tasks

Using modules from the Python Standard library to easily access and use existing
code gives you a lot of computing power 

The Python Standard Library is organized into modules - many of which are simply
Python files like the scripts we write

An import statement runs the code in the module - Running the code will make all
the module's functions and types of objects available to use

Modules typically contain a lot of definitions and usually do not show any output

The Python Standard Library has good documentation for each of its modules and it
is a good idea to read the relevant page whenever you use one

Modules in the documentation of the Python Standard Library are listed in groups
based on their uses. Clicking on a name takes you to the documentation for the 
module which often has examples as well to test out.

When you save your Python scripts, take care not to give them a name that is used
by one of Python’s modules, such as random.py, sys.py, os.py, or math.py. If you
accidentally name one of your programs, say, random.py, and use an import random
statement in another program, your program would import your random.py file
instead of Python’s random module. This can lead to errors such as
AttributeError: module 'random' has no attribute 'randint', since your random.py
doesn’t have the functions that the real random module has. Don’t use the names
 of any built-in Python functions either, such as print() or input()
''')

import math
print("Factorial of 9 is ", math.factorial(9))
print("e to the power of 3 is ", math.exp(4))

print('#' * 99)

print(r'''
The Python Standard Library has a lot of modules! Here are a selection of a few
Python Standard Library modules and why we use them!

csv: very convenient for reading and writing csv files

collections: useful extensions of the usual data types including OrderedDict,
defaultdict and namedtuple

random: generates pseudo-random numbers, shuffles sequences randomly and chooses
random items

string: more functions on strings. This module also contains useful collections
of letters like string.digits (a string containing all characters which are valid digits).

re: pattern-matching in strings via regular expressions

math: some standard mathematical functions

os: interacting with operating systems

os.path: submodule of os for manipulating path names

sys: work directly with the Python interpreter

json: good for reading and writing json files (good for web work)
''')

print('#' * 99)

print(r'''
Importing modules with the syntax >>>import module_name makes all the classes of
objects and functions of that module available via dot-notation

There are other variants of import statements useful under different conditions:
1. To import an individual function or class from a module:
   >>>from module_name import object_name
   This gives access only to the object you have imported via the object_name. 
   Trying to access the object via dot-notation or even trying to access the
   module itself will raise a NameError exception
   Importing individual objects from a module means you only take what you need
   and you do not need to use dot-notation to access it

2. To import multiple individual objects from a module:
    >>>from module_name import first_object, second_object

    You can import multiple individual objects by separating them with a comma
    This technique is common when importing pieces from large libraries

3. To rename a module:
    >>>import module_name as new_name

    This is useful if the name of the module is too long or if there is a clash
    with another identifier in your code,
    When renaming modules, it is nice to use standard abbreviations as this makes
    your code consistent with others and also easier to read

4. To import an object from a module and rename it:
    >>>from module_name import object_name as new_name

    This can be useful if you have multiple objects with similar names from
    different packages in your namespace hence you give them the descriptive
    names to differentiate e.g a jsonreader and a csvreader

5. To import every object individually from a module (DO NOT DO THIS):
    >>>from module_name import *

Using this asterisk will import every object from a module individually and allow
you to access each of them directly via its name (not via the dot-notation)

The problem arises in that modules may contain many objects each of which has a
name and including all these names in your namespace may overwrite or be overwritten
by other names in your program
import * also makes it impossible for collaboraters to find where an imported object was defined

A reader may look for a definition of a function and not find it and they will not
know which import * statement introduced it.

If you really want to use all of the objects from a module, use the standard
import module_name statement instead and access each of the objects with the dot notation.
    >>>import module_name
''')

print('#' * 99)

print(r'''
Some of the modules in the PySL (Python Standard Library), have a lot in them.
In order to manage code better, they are split down into sub-modules that are
contained within a package

A package is simply a module that contains submodules
A submodule is specified with the usual dot-notation
Modules that are sub-modules are specified with the package name and then the
sub-module name separated by a dot (.)
You can then access the objects and functions using the dot-notation
>>>import os.path
>>>os.path.isdir('/)

You can also just import the whole package and everything in the submodule will
still be accessible
>>>import os
>>>os.path.isdir('/)

''')

print('#' * 99)

print(r'''
Sometimes naming can be a point of confusion when working with modules for example
a module might be named after one of the imported classes or functions within it.
In such cases, you really need to think about your import statements
>>>from datetime import datetime

The above imports the datetime class from the datetime module
Note after the import, datetime refers to the datetime class not the module
''')

print('#' * 99)

print(r'''
Programs always terminate if the program execution reaches the bottom of the 
instructions i.e the last line of code

However, you can cause the program to exit before it reaches the last instruction
by using the exit() function found in the sys module
>>>import sys
>>>sys.exit()
''')

print('#' * 99)
