print("Variable scope is which part of a program a variable can be referenced (used)")
print("Scope is like a container for variables")
print("There are two types of variable scope:\n\t1. local scope\n\t2.global scope")
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