print("Errors in our programs cause them to crash and exit S(stop running)")
print("There are two types of errors in Python- syntax S(parsing) errors and exceptions")
print('#' * 99)
print("Syntax errors occur when Python cannot interpret our code because we have used incorrect syntax e.g forgetting a closing quotation mark when creating a string: greeting = 'Hello World ")
print('#' * 99)
print("Exceptions occur during run-time when something unexpected occurs e.g if we try to divide a number by zero print(7/0) we get a ZeroDivisionError because we cannot divide a number by zero ")
# print(7/0)
print('#' * 99)
print("Python has a better way to handle errors so that our programs do not always crash when they occur- by using the try block")
print("Try block is used to handle exceptions and has 4 clauses we can use:")
print('#' * 99)
print("1. try: This is the only mandatory clause in the try statement and its code block is the first to be executed in the try statement")
print("2. except: If Python runs into any exception while running code in the try block, it jumps to the except block that handles the exception. Once the execution jumps to the code in the except clause, it does not return to the try clause. Instead, it just continues moving down the program as normal")
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
print("When we use the except keyword only in the except clause, it catches all exceptions that may be raised including KeyInterrupt among others, thus if we try to exit the code using ctrl+c, the code still will not exit because the except block catches it as an exception.")
print("There is a way around this since we can state the exception we want the except block to catch as follows: except ValueError: or we could catch multiple errors by using a paranthesised tuple with the exceptions separated by a comma e.g except (ValueError, TypeError): or we could just have multiple except blocks if we want to run a different code block for each error")
print('#' * 99)


while True:
    try:
        x = int(input("Enter a number: "))
    except ValueError:
        print('\nNot a valid number\n')
        continue
    except KeyboardInterrupt:
        print('\nYou have not entered a number. Try again\n')
        continue
    else:
        print("\nNumber inputted- {}\n".format(x))
        break
    finally:
        print("\nThank you for trying\n")
    
print('#' * 99)
print("We can still access an error message after we have handled an exception to prevent the program from crashing")
print("try:\n\t#some code\nexcept ZeroDivisionError as e:\n\tprint('ZeroDivisionError occured: {}'.format(e))")
print("This would output:")
try:
    5/0
except ZeroDivisionError as e:
    print("ZeroDivisionError occured: {}".format(e))

print('#' * 99)
print("If we are not handling a specific exception, we can still access the error message using the base class for exceptions as follows:")
print("try:\n\t5 + 's'\nexcept Exception as e:\n\tprint(\"The following exception occured: {}\".format(e))")
print("This would output:")
try:
    5 + 's'
except Exception as e:
    print("The following exception occured: {}".format(e))
print('#' * 99)
print("'Exception' is the base class for all built in exceptions")
