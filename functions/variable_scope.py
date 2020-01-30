print("Variable scope is which part of a program a variable can be referenced (used)")
print("There are two types of variable scope:\n\t1. local scope\n\t2.global scope")
print("Variables defined within a function are said to have a scope that is local meaning that the variable can only be accessed and used within that function. Using or accessing a variable with a local scope outside the function it is defined in is not possible")
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

print('#' * 99)
print("A variable defined outside any function is said to have a global scope. It is accessible inside any function within the program but it's value can only be accessed and cannot be changed")
print("Trying to change a global variable within a function will give an UnboundLocalVariable error because Python does not allow a function to modify a global variable")
print('#' * 99)

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

