print("given a list, we can create a new list from it using for loops to iterate\
 through each element and then evaluating some expression for each to create the\
 elements for the new list for example:")
print('#' * 99)

letters = ['a', 'b', 'c', 'd', 'e', 'w', 'm', 'r']
upper_cased = []
for letter in letters:
    upper_cased.append(letter.upper())


print("Given a list letters = ['a', 'b', 'c', 'd', 'e', 'w', 'm', 'r'], we can\
 create a new list with the letters in uppercase. First, we create an empty list\
 upper_cased = [] then use a for loop to convert each letter to uppercase then\
 append it to the new list as follows:\nfor letter in letters:\n\t\
upper_cased.append(letter.upper())\nprint(upper_cased)\n{}".format(upper_cased))
print(upper_cased)

print('#' * 99)

print("Turns out, we can more quickly and precisely create a new list from an\
 existing list or another iterable in Python using a construct called list comprehensions")
print('#' * 99)

print("A list comprehension is created using square brackets and inside them\
 including expressions, for loops and conditional statements as neccessary to create the new list.")
print('#' * 99)

print("For example, we can convert the upper_cased list above to a lower_cased list as follows:\
 lower_cased = [letter.lower() for letter in letters] to get;")
lower_cased = [letter.lower() for letter in letters]
print(lower_cased)
print('#' * 99)

print("We do not need to initialize an empty list to append to when using list\
 comprehensions. We reduce the code we could have used in a for loop to just one\
 line. Notice, we use the for statement similar to one we would use but without the colon")
print('#' * 99)

squares = [num**2 for num in range(21)]

print("Suppose we want to create a list of all squares of numbers from 0 to 20, we could use list comprehensions as follows:\nsquares = [num**2 for num in range(21)]\nprint(squares)")
print(squares)
print('#' * 99)

print("We can add conditional statements to the list comprehensions as follows:")
print("Suppose we want to print out just the squares of even numbers. We could add a conditional as follows:\neven_squares = [num**2 for num in range(21) if x % 2 ==0]")
even_squares = [num**2 for num in range(21) if num % 2 == 0]
print(even_squares)
print('#' * 99)

print("If you want to add an else statement, you have to move the conditional to the beginning of the list comprehension just after the expression to be evaluated for each element")
print("for example, say we wanted if the number is not even to cube it instead")

weird_squares = [num**2 if num % 2 == 0 else num**3 for num in range(21)] 
print(weird_squares)
print('#' * 99)
#practice

# Quiz: Extract First Names
# Use a list comprehension to create a new list first_names containing just the first names in names in lowercase.

names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split()[0].lower() for name in names]
print(first_names)

print('#' * 99)
# Use a list comprehension to create a list multiples_3 containing the first 20 multiples of 3.
multiples_3 = [num * 3 for num in range(1, 21)]
print(multiples_3)
print('#' * 99)

# Quiz: Filter Names by Scores
# Use a list comprehension to create a list of names passed that only include those that scored at least 65.

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name, score in scores.items() if score>=65]
print(passed)

print('#' * 99)
print(r'''
List comprehensions syntax summary is as follows:

[expression for iteration_variable in iterable singular condition]
[expression multiple conditionals for iteration_variable in iterable]
''')