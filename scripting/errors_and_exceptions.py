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
    

