# best practices for code style in Python
print("When you call a function, put the opening parantheses straight after the\
 name of the function e.g print(8) and not print (8)")
print('#' * 99)
print("Do not put any extra spaces immediately after the parantheses either e.g\
 print( 8*5 ) is bad style. Rather print(8*5) is better")
print('#' * 99)
print("Whitespace in between the operators and values doesn’t matter for Python\
 (except for the indentation at the beginning of the line), but a single space\
 is convention.")
print('#' * 99)
print("If you are mixing operators with different priorities, add a space around\
 the lower priority (the one that comes later in the arithmetic order of operations)\
 to make the code easier to read e.g")
print("5*7 + 4")
print('#' * 99)
print("Do not write extremely long lines of code. Limit your lines to 79-99\
 characters long")
print('#' * 79)
print("For more style guidelines, read the official style guide-\
 PEP 8 -- Style Guide for Python Code at https://www.python.org/dev/peps/pep-0008/")
print("You can also split up a single instruction across multiple lines using\
 the \ line continuation character at the end. Think of \ as saying, “This instruction\
 continues on the next line.” The indentation on the line after a \ line\
 continuation is not significant.")