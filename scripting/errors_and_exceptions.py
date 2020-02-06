print("Errors in our programs cause them to crash and exit(stop running)")
print("There are two types of errors in Python- syntax(parsing) errors and exceptions")
print('#' * 99)
print("Syntax errors occur when Python cannot interpret our code because we have used incorrect syntax e.g forgeting a closing quotation mark when creating a string: greeting = 'Hello World ")
print('#' * 99)
print("Exceptions occur during run-time when something unexpected occurs e.g if we try to divide a number by zero print(7/0) we get a ZeroDivisionError because we cannot divide a number by zero ")
# print(7/0)
print('#' * 99)
print("Python has a better way to handle errors so that our programs do not always crash when they occur- bu using the try block")
print("Try block is used to handle exceptions and has 4 clauses we can use:")
print('#' * 99)
print("1. try: This is the only mandatory clause in the try statement and its code block is the first to be executed in the try statement")
print("2. except: If Python runs into any exception while running code in the try block, it jumps to the except block that handles the exception")
print("3. else: If Python runs into no exceptions while running the code in the try block, it will execute the code in else after executing the try block")
print("4. finally: This block will always be executed under any circumstances before the try statement exists even if it is ending the program. The finally block is useful for cleaning up actions in our code e.g closing a file we attempted opening using a try statement")
print('#' * 99)

print("There are many built-in exceptions in Python and when they occur, Python's error messages point out wha t exception was catched before the program crashed e.g")
print("1. ValueError: An object of the correct type but inappropriate value is passed as input to a built-in function or operation e.g passing to the int method a value of 'ten' instead of '10' or a value of '10.5'")
print("2. TypeError: An object of an unsupported type is passed to a function or operation e.g passing to the + operator two dictionary objects")
print("3. IndexError: An exception that occurs when a sequence subscript is out of range")
print("4. AssertionError: An exception that occurs when an assert statement fails")
print("1. KeyError: An exception that occurs when a key does not exist in a dictionary")
print('#' * 99)

while True:
    try:
        x = int(input("Enter a number: "))
    except:
        print('Not a valid number')
    else:
        print("Number inputted- {}".format(x))
        break
    finally:
        print("Attempted input")
    

