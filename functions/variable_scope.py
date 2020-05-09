print("Variable scope is which part of a program a variable can be referenced (used)")
print("Scope is like a container for variables")
print("There are two types of variable scope:\n\t1. local scope\n\t2. global scope")
print("Parameters and Variables defined (assigned) within a function are said to have a scope that is local. Using or accessing a variable with a local scope outside the function it is defined in is not possible")
print('#' * 99)
print("A variable defined outside all functions is said to have a global scope.")
print('#' * 99)
print("local variable - a variable that exists in a local scope")
print("global variable - a variable that exists in a global scope")
print("A variable cannot be both local and global. It has to be one of the two")
print('#' * 99)
print("When a scope is destroyed, all the values stored in variables in the scope are forgotten")
print('#' * 99)

print("There is only one global scope. This is created when a program begins")
print("When a program terminates, the global scope is destroyed and all the variables are forgotten, so the next time you run your program, the variables do not remember the values from last program execution")
print('#' * 99)
print("Local scope is created whenever a function is called. Any variable assigned in the function exists within the function's local scope and when the function returns (exits), the local scope is destroyed and so these variables are forgotten")
print("The next time you call the function, the local variables will not remember the values stored from the previous time the function was called")
print('#' * 99)
print("What is the importance of scope??")
print("1. Code in the global scope outside of all functions cannot use any local variable")
print("2. Code in a local scope can access global variables")
print("3. You can use the same name for different variables if they are in different scopes")
print('#' * 99)
print("Local variable cannot be used in global scope".upper())
print("Consider the following code and look at the result")
print("def spam():\n\teggs = 300\nspam()\nprint(eggs)")
def spam():
    eggs = 300
spam()
try:
    print(eggs)
except Exception as e:
    print(e)

print()
print("The result (name 'eggs' is not defined') is proof that when program execution is in global scope, there is no local scope thus no local variable exists.")
print("This is what happens in the code above. Since the first two lines are a function definition, program execution skips them and goes straight to the function call on the third line. The function call has the program execution enter the function, creating a local scope and executes the body where the local variable eggs is assigned to the value 300. The function then exits meaning the local scope together with the local variable is destroyed. The next line printing out the value of eggs is in the global scope and there does not exist a global variable eggs thus the NameError generated")
print('#' * 99)
print("Local scopes cannot use local variables in other local scopes".upper())
print("A new local scope is created whenever a function is called even if the function is called within another function / from another function")
print("Consider the following block of code and what is printed after it executes")
print()
print("def spam():\n\teggs = 30\n\tbacon()\n\tprint(eggs)\ndef bacon():\n\teggs = 60\nspam()")
def spam():
    eggs = 30
    bacon()
    print(eggs)
def bacon():
    eggs = 60

spam()
print()
print("30 is printed out after the code executes. Why??")
print("Program execution begins at the function call spam() which creates a new local scope and causes program execution to enter the spam function and begin execution at the first line in the body which assigns 30 to the local variable eggs. The next line is a call to the bacon function which creates a new local scope and program execution immediately moves into the bacon function where it assigns 60 to a new local variable eggs which is different from the one in the spam function. The function is one line so after that line it exits (finishes) and thus its local scope and all variables in it is destroyed and program execution moves to the next line after the bacon() function call which instructs it to print the value of the variable eggs. We are still within the spam's local scope, so the variable eggs of that scope is what is printed which is 30 and once done the program is finished so it exits and the scope is destroyed together with any variables in it")


print('#' * 99)
print("Global values can be read (accessed) from local scope".upper())
print("The following code snippet supports the above fact")

print("def spam():\n\tprint(eggs)\neggs = 90\nspam()\nprint(eggs)")
def spam():
    print(eggs)
eggs = 90
spam()
print(eggs)
print()
print("When the spam() function is called, program execution enters it's body and executes the statement to print out the value of the variable eggs and since there is no local variable eggs assigned in its scope, it prints out the global variable eggs which has the value 90 and exits then the next line is in the global scope and prints out the global variable eggs")

print('#' * 99)
print("Local and global values can have the same name".upper())
print("The following code uses the same name 'eggs' for the variables. This is however confusing in some instances. Avoid it if you can")
print("def spam():\n\teggs = 'spam local'\n\tprint(eggs)\ndef bacon():\n\teggs = 'bacon local'\n\tprint(eggs)\n\tspam()\n\tprint(eggs)\neggs = 'global'\nbacon()\nprint(eggs)")
print()

def spam():
    eggs = 'spam local'
    print(eggs)
def bacon():
    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs)
eggs = 'global'
bacon()
print(eggs)

print('#' * 99)
print('#' * 99)
print("GLOBAL STATEMENT")
print("If you want to modify a global variable within a function (local scope), you can do so by using the global statement")
print("An example:")

print("def add():\n\tglobal a # the global statement\n\ta += 2\n\tprint(a)\na=1\nadd()\nprint(a)")

def add():
    global a # the global statement
    a += 2
    print(a)
a = 1
add()
print(a)

print("The global statement at the top of the function tells Python that in this function the variable 'a' refers to the global variable so that is what is modified")
print('#' * 99)
print('#' * 99)

print("4 rules to tell whether a variable is in local or global scope".upper())
print("1. If a variable is being used in the global scope i.e outside of all functions then it is always a global variable")
print("2. If there is a global statement for that variable in a function, it is always a global variable")
print("3. Otherwise, if the variable is used in an assignment  statement in a function, it is a local variable")
print("4. But if the variable is not used in an assignment statement, it is a global variable")

print('#' * 99)
print('#' * 99)
print("def spam():\n\tglobal eggs\n\teggs = 'spam' # global variable\n\ndef bacon():\n\teggs = 'bacon' # local variable\n\ndef ham():\n\tprint(eggs)  # global variable\n\neggs = 30 # global")

def spam():
    global eggs
    eggs = 'spam' # global variable

def bacon():
    eggs = 'bacon' # local variable

def ham():
    print(eggs)  # global variable

eggs = 30 # global

print('#' * 99)
print('#' * 99)

print("def spam():\n\tprint(eggs)\n\teggs = 30\neggs = 42\nspam()")
def spam():
    print(eggs)
    eggs = 30
eggs = 42
try:
    spam()
except Exception as e:
    print(e)

print("The above code results in an error 'local variable \'eggs\' referenced before assignment' as shown above. Why??")

print("This error happens because Python sees that there is an assignment statement in the function thus it considers eggs to be a local variable but because the print function is called before the eggs variable has been assigned a value, the local eggs variable therefore does not exist and since a function can only have either a global or local variable, Python cannot fall back to using the global eggs variable that exists thus the error")
print('#' * 99)
print('#' * 99)


print("eg of a local variable count used to get the number of occurences of a substring in a string")
print("def word_count(string, search_term):\n\tcount = 0\n\tfor letter in string:\n\t\tcount += 1\n\treturn count")
print("Calling the function as follows: print(word_count(random_string, 'a')) after defining a random_string: random_string = \"VGJYJJjEIRCNFWuEVBHiYzVJsmMYlWMlHQrarfCcWzprOHEjksmzvlHlFwnxQqmzurrBkpasHIWqQawKKcBYszvsyXzOLyogy\" would give us:")
random_string = "VGJYJJjEIRCNFWuEVBHiYzVJsmMYlWMlHQrarfCcWzprOHEjksmzvlHlFwnxQqmzurrBkpasHIWqQawKKcBYszvsyXzOLyogy"
def word_count(string, search_term):
    count = 0
    for letter in string:
        if letter == search_term:
            count += 1
    return count

print(word_count(random_string, 'a'))

print("It is recommended that when writing programs, we define variables in the lowest scope needed so that we avoid errors even though functions can still access variables defined in a higher scope")
print("Just keep variables local. They are easier to work with and modify")

print('#' * 99)
print("If you have two variable names that are similar, one global and one local, then the local one is the one used inside the function (takes precedence)")
print('#' * 99)
print("To remedy the situation where you cannot modify a global variable using a function, we can pass the global variable as an argument to the function, then modify it outside the function e.g:")
print("eggs_count = 0\ndef buy_eggs(number):\n\treturn number + 30\n\neggs_count = buy_eggs(eggs_count)\nprint(eggs_count)")
eggs_count = 0
def buy_eggs(number):
    return number + 30

eggs_count = buy_eggs(eggs_count)
print(eggs_count)
print('#' * 99)
print('#' * 99)


# generate a random string using alphanumeric characters 
def random_str_generator(len_str):
    import random
    import string
    random_str = ""
    alpha_numeric_chars = list(string.ascii_letters) + list(string.digits)
    while len(random_str) < len_str:
        random_str += random.choice(alpha_numeric_chars)
    return random_str
    
print(random_str_generator(10))

# return the largest square given an integer input

def largest_square(number):
    i = 0
    while (i+1)**2 < number:
        i += 1
    return i**2
print(largest_square(500))