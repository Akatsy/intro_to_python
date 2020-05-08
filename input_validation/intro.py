print("Input validation checks that values entered by the user in your program are formatted correctly")
print("This helps in avoiding bugs, making sure your programs do not crash later on due to invalid values for example if you ask a user for their age, you expect a number (digit value) - an integer to be precise which should not be negative ofcourse. If a user input does not adhere to the above rules, you should prompt them to re-enter the value again")

print('#' * 99)

print("Input validation also can help avoid security vulnerabilities")
print("For example say you were implementing a withdraw_from_account() function and the user had to input the amount they want to withdraw. You have to make sure that the user does not enter a negative amount because subtracting a negative amount from the account would end up actually adding. Therefore, the 'withdrawal' would end up adding money to the account instead of subtracting")

print('#' * 99)

# input validation example
# while True:
#     age = input("Enter your age:\n")
#     try:
#         age = int(age)
#     except:
#         print("Please input a number in digits")
#         continue
#     if age < 1:
#         print("Age cannot be negative. Input a positive number")
#         continue
#     elif age > 150:
#         print("You cannot be that old. Come on!!")
#         continue
#     else:
#         break
# print(f'Hey {age} years old human!')

print('#' * 99)

print("PyInputPlus".center(99, '='))
print("PyInputPlus is a Python3 module to provide input()-like functions with additional validation features")
print("PyInputPlus is not part of the Python Standard Library thus has to be installed separately using pip as follows\n 'pip3 install pyinputplus' ")
print("The module contains functions similar to the standard Python input() function for different kinds of data e.g email addresses, dates, numbers e.t.c")

print('#' * 99)

print("If a user ever enters an invalid input of the kind of data specified by any of the PyInputPlus input functions, eg a wrongly formatted date, PyInputPlus will re-prompt them to enter the input again")
print("In addition to re-prompting, PyInputPlus has other useful features e.g a limit of the number of times to re-prompt user for input, a timeout feature if the user is required to respond within a specific time duration")

print('#' * 99)

print("PyInputPlus Functions".center(99, '='))
pyip_functions = {
    'inputStr()': "Prompts the user to enter any string input. This is similar to Python’s input() function but with PyInputPlus’s additional features such as timeouts, retry limits, stripping, allowlist/blocklist, etc",
    'inputNum()': "Prompts the user to enter a number, either an integer or a floating-point value. Returns an int or float value (depending on if the user entered a decimal in their input.)",
    'inputChoice()': "Prompts the user to enter one of the provided choices. Returns the selected choice as a string.",
    'inputMenu()': "Prompts the user to enter one of the provided choices. Also displays a small menu with bulleted, numbered, or lettered options. Returns the selected choice as a string.",
    'inputDatetime()': "Prompts the user to enter a datetime, formatted as a strptime-format in the formats list. Returns a datetime.datetime object.",
    'inputYesNo': "Prompts the user to enter a yes/no response. The user can also enter y/n and use any case. Returns the yesVal or noVal argument (which default to 'yes' and 'no'), depending on the user’s selection.",
    'inputBool()': "Prompts the user to enter a True/False response. The user can also enter t/f and in any case. Returns a boolean value.",
    'inputEmail()': "Prompts the user to enter an email address. Returns the email address as a string",
    'inputFilepath()': "Prompts the user to enter a filepath. If mustExist is True, then this filepath must exist on the local filesystem. Returns the filepath as a string",
    'inputPassword()': "Prompts the user to enter a password. Mask characters will be displayed instead of the actual characters"
}
import pprint
print(pprint.pformat(pyip_functions))

print('#' * 99)
print("Here are some PyInputFunctions and what they do".center(99, '='))
for function, definition in pyip_functions.items():
    print(function)
    print(definition)

print('#' * 99)