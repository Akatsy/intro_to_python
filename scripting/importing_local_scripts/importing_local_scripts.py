print('''
We can import Python code from other scripts into our programs
If the Python file you want to import is in the same folder as your current script, you just type import followed by the name of the file without the .py extension
Import statements are written at the top of a Python script, each one on a separate line although Python will still run if they are included later in the script (Note: You are only able to access what you have imported after the import statement)
Having the import statement at the top of a file is nice as readers get to see what your script depends on before reading the rest of the code.
''')

print('#' * 99)

print('''
To access objects in other scripts from our current script, we cannot just type the name of the object - this will raise a NameError exception. 
We need to use the name of the file (module) we imported followed by a dot (.) then the object name - This tells Python to look for the object in that file
When Python runs a script, it only has direct access to objects defined in that script. If the script has an import statement, then one of the objects the current script has access to is the module object created by the import statement. The name of the object is the name given after the import keyword and the object is of type module
A module is just a file with Python definitions and statements
''')

print('#' * 99)

print('''
You can create an alias when importing a module so that you do not have to type the whole name of the module whenever you need to access its objects using the 'import module_name as alias' statement
''')