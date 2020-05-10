print("functions have the advantage of making code easier to understand by making it easier to read and write blocks of code")
print("functions can help break down a program into smaller chunks by implementing a singular task that is part of the whole")
print("By naming functions using descriptive names of what task they accomplish, we help in improving understanding of code")
print('#' * 99)
print("Apart from using descriptive names for functions, we can also add documentation to help other programmers and our future selves understand what a funtion does")
print("DOCSTRINGS (documentation strings) are a type of comments that describe the purpose of a function and how to use it.")
print('#' * 99)

print("A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition. Such a docstring becomes the __doc__ special attribute of that object")
print("All modules should normally have docstrings, and all functions and classes exported by a module should also have docstrings. Public methods (including the __init__ constructor) should also have docstrings. A package may be documented in the module docstring of the __init__.py file in the package directory.")

print("String literals occurring elsewhere in Python code may also act as documentation. They are not recognized by the Python bytecode compiler and are not accessible as runtime object attributes (i.e. not assigned to __doc__), but two types of extra docstrings may be extracted by software tools:")

print('1. String literals occurring immediately after a simple assignment at the top level of a module, class, or __init__ method are called "attribute docstrings".')
print('2. String literals occurring immediately after another docstring are called "additional docstrings"')

print('#' * 99)

print('For consistency, always use """triple double quotes""" around docstrings. Use r"""raw triple double quotes""" if you use any backslashes in your docstrings. For Unicode docstrings, use u"""Unicode triple-quoted strings""".')

print('#' * 99)

print("There are two forms of docstrings: one-liners and multi-line docstrings.")
print("One-liners are for really obvious cases. They should really fit on one line")
print("Notes for one-liners:")
print("1. Triple quotes are used even though the string fits on one line. This makes it easy to later expand it")
print("2. The closing quotes are on the same line as the opening quotes. This looks better for one-liners")
print("3. There's no blank line either before or after the docstring")
print('4. The docstring is a phrase ending in a period. It prescribes the function or method\'s effect as a command ("Do this", "Return that"), not as a description; e.g. don\'t write "Returns the pathname ...".')

print('#' * 99)

print("Multi-line docstrings consist of a summary line just like a one-line docstring, followed by a blank line, followed by a more elaborate description.")
print("The summary line may be used by automatic indexing tools; it is important that it fits on one line and is separated from the rest of the docstring by a blank line.")
print("The summary line may be on the same line as the opening quotes or on the next line. The entire docstring is indented the same as the quotes at its first line")


print('#' * 99)

print('''The docstring of a script (a stand-alone program) should be usable as its "usage" message, printed when the script is invoked with incorrect or missing arguments (or perhaps with a "-h" option, for "help"). Such a docstring should document the script's function and command line syntax, environment variables, and files. Usage messages can be fairly elaborate (several screens full) and should be sufficient for a new user to use the command properly, as well as a complete quick reference to all options and arguments for the sophisticated user.''')

print('#' * 99)

print('''The docstring for a module should generally list the classes, exceptions and functions (and any other objects) that are exported by the module, with a one-line summary of each. (These summaries generally give less detail than the summary line in the object's docstring.) The docstring for a package (i.e., the docstring of the package's __init__.py module) should also list the modules and subpackages exported by the package.''')

print('#' * 99)

print('''The docstring for a function or method should summarize its behavior and document its arguments, return value(s), side effects, exceptions raised, and restrictions on when it can be called (all if applicable). Optional arguments should be indicated. It should be documented whether keyword arguments are part of the interface.''')

print('#' * 99)

print('''The docstring for a class should summarize its behavior and list the public methods and instance variables. If the class is intended to be subclassed, and has an additional interface for subclasses, this interface should be listed separately (in the docstring). The class constructor should be documented in the docstring for its __init__ method. Individual methods should be documented by their own docstring.

If a class subclasses another class and its behavior is mostly inherited from that class, its docstring should mention this and summarize the differences. Use the verb "override" to indicate that a subclass method replaces a superclass method and does not call the superclass method; use the verb "extend" to indicate that a subclass method calls the superclass method (in addition to its own behavior)''')

print('#' * 99)

print("Here is Google's docstring format:")
print('''This is an example of Google style.

Args:
    param1: This is the first param.
    param2: This is a second param.

Returns:
    This is a description of what is returned.

Raises:
    KeyError: Raises an exception.
''')

print('#' * 99)


print("The first line of a docstring gives a brief description of what the function does. This is enough if the function is not that complicated")
print('#' * 99)
print("If the function is a little complicated, you can include a paragraph to further describe the function")
print("The next line after the brief description is a description of the inputs (arguments) to the function. Here you list the arguments the function will take and their expected types, Then a description of what the arguments actually are (what they represent)")
print("After the inputs description, it is good to give a description of the output of the function also (what the function returns or prints out)")
print('#' * 99)
print('#' * 99)
print("an example of a docstring")
print("def population_density(population, land_area):\n\t\"\"\" Calculate the population density of an area\n\t\tINPUT:\n\t\tpopulation: int. The number of people in an area\n\t\tland_area: int or float. This is unit-agostic meaning if you give the area in a certain unit,\n\t\tsay kilometres or miles, the answer will be given in that unit\n\t\tOUTPUT:\n\t\tpopulation_density: population/land_area. The population density of a given area \"\"\"\n\treturn population/land_area")
print('#' * 99)

def population_density(population, land_area):
    """ Calculate the population density of an area
        INPUT:
        population: int. The number of people in an area
        land_area: int or float. This is unit-agostic meaning if you give the area in a certain unit, say kilometres or miles, the answer will be given in that unit
        OUTPUT:
        population_density: population/land_area. The population density of a given area """ 
    return population/land_area
print(population_density(900, 90))

print('#' * 99)
# Quiz: Write a Docstring
# Write a docstring for the readable_timedelta function
# Given an integer that represents a number of days, write a function that returns a string that states the number of weeks and number of days for example if days = 10, it should return 1 week(s) and 3 day(s)

def readable_timedelta(days):
    """ calculate number of weeks and days given a number of days
        INPUT:
        days: int. a number representing the number of days
        OUTPUT:
        a string stating the number of days given, and the number of weeks and days that evaluates to"""
    weeks = days // 7
    remainder = days % 7
    return "Given {} days that is {} week(s) and {} days(s)".format(days, weeks, remainder)

print(readable_timedelta(90))
# help(readable_timedelta)


print('#' * 99)
# a better way to define the docstring
def readable_timedelta(days):
    """
    Return a string of days input and the number of weeks and days included in days

    Parameters:
    days -- number of days to convert(int)

    Returns:
    a string of days input and the number of weeks and days included in days
    """
    weeks = days // 7
    remainder = days % 7
    return "Given {} days that translates to {} week(s) and {} day(s)".format(days, weeks, remainder)

print(readable_timedelta(366))
# help(readable_timedelta)