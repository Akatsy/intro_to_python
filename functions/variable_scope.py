print("Variable scope is which part of a program a variable can be referenced (used)")
print("There are two types of variable scope:\n\t1. local scope\n\t2.global scope")
print("Variables defined within a function are said to have a scope that is local meaning that the variable can only be accessed and used within that function. Using or accessing a variable with a local scope outside the function it is defined in is not possible")
print('#' * 99)
print("eg of a local variable")
random_string = "VGJYJJjEIRCNFWuEVBHiYzVJsmMYlWMlHQrarfCcWzprOHEjksmzvlHlFwnxQqmzurrBkpasHIWqQawKKcBYszvsyXzOLyogy"
def word_count(string, search_term):
    count = 0
    for letter in string:
        if letter == search_term:
            count += 1
    return count

print(word_count(random_string, 'a'))

print('#' * 99)

def random_str_generator(len_str):
    import random
    import string
    random_str = ""
    alpha_numeric_chars = list(string.ascii_letters) + list(string.digits)
    while len(random_str) <= len_str:
        random_str += random.choice(alpha_numeric_chars)
    return random_str
    
print(random_str_generator(1000))

