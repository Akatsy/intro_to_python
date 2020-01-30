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

