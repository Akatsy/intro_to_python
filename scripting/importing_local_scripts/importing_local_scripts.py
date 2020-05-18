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

What if the script we import has executable statements which we do not need to use in our current script?
This is where the >>>if __name__ == '__main__': statement comes in.
By including the executable statements inside if name is main statement (if __name__ == '__main__':), we tell Python to execute that code only when the main program being executed is that script. If the script is imported in another script, that code will not run

Generally, it is good practice to write executable statements inside an if main block or alternatively include them in a function called main and call this function in the if name is main block
>>>def main():
    pass

>>if __name__ == '__main__':
    main()


Whenever we run a script, Python actually creates a special builtin variable called __name__ for any module
When we run a script, Python recognizes this module as the main program, and sets the __name__ variable for this module to the string "__main__".
For any modules that are imported in this script, this built-in __name__ variable is just set to the name of that module. Therefore, the condition if __name__ == "__main__"is just checking whether this module is the main program
''')