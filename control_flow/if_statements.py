print("Python code is normally read and executed line by line from top to bottom")
print("However, sometimes we might want to have some block of code executed and other blocks skipped depending on some conditions")
print("if statements are conditional statements that execute or skip blocks of code depending on whether the conditions they check evaluate to True or False")
print('#' * 79)
print("An if statement is declared as follows:\n\tYou begin with the if keyword followed by a condition which must be a boolean expression then end with a full colon(:)\n\tBelow that you then have an indented block of code that you wish to be evaluated if the conditional statement evaluates to True, or otherwise skipped if it evaluates to False")
print('#' * 79)
print("Python indents blocks of code using spaces (4 spaces by default - use spaces instead of TABS according to Python specification but you can still use TABS long as you are consistent and do not mix them).")
print("The indented block of code beneath an if statement is executed if and only if the condition in the if clause executes to True")
print('#' * 79)
print("Sometimes, you have a few conditions which have different conditions you want executed depending on which condition executes to True.\n In this case, Python has two more clauses you can use to have your different conditions and their corresponding blocks of code for execution as follows:")
print('#' * 79)
print("1. elif(short for else if) statement - This is a conditional clause that begins with the elif keyword followed by a condition to be checked then a full colon(:) and below it a block of code that will execute if True")
print("You can have as many elif clauses, each with its condition to check if the other clauses above it executes to false")
print('#' * 79)
print("2. else - This clause is the last in an if statement. It will execute if all other clauses(the if and elifs) execute to false. It does not need a condition(boolean expression) just define it using the else keyword followed by a colon(:)")

print("An example of an if statement:\")\nweather = 'rainy'\nif weather == 'sunny':\n\tprint(\"Wear light clothes\")\nelif weather == 'cold':\n\tprint(\"Wear warm clothes\")\nelif weather == 'rainy':\n\tprint(\"Carry an umbrella\")\nelse:\n\tprint(\"Weather is confusing!")

weather = 'rainy'
if weather == 'sunny':
    print("Wear light clothes")
elif weather == 'cold':
    print("Wear warm clothes")
elif weather == 'rainy':
    print("Carry an umbrella")
else:
    print("Weather is confusing!")

print("After the example, you can see the line printed is 'Carry an umbrella' because that is the block that will be executed since our weather variable is set to 'rainy'")