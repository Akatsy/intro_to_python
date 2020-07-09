print("lambda expressions can be used to create anonymous functions i.e functions\
 without a name")

print("They are helpful when we want to create quick functions that are not needed\
 later in your code")

print("This can be especially useful in higher order functions (i.e functions that\
 take other functions as arguments)")
print('#' * 99)

print("A lambda expression has the following parts:")

print("1. the lambda keyword which signifies that this is a lambda expression")

print("2. Following the lambda keyword is one or more arguments separated by a comma\
 and then a colon(:). This will be passed as inputs to the function. (Their naming is just arbitrary)")

print("3. Finally, after the colon is a statement that the function is to evaluate\
 to get an output value, similar to what we would find in a return statement in a named function ")

print("Given this structure, lambda expressions are not ideal for complex functions\
 but can be very useful for simple functions")
print('#' * 99)
print("for example the following function\n {} can be converted to a lambda function\
 as follows:\n {}".format("def cubed(num):\n\treturn num ** 3\n\n", "\ncubed = lambda num: num**3"))

def cubed(num):
    return num ** 3

cubed = lambda num: num**3
print("cubed(9) = ", cubed(9))

# example of lambda with higher order functions
print('#' * 99)
print("map() is a higher order built-in function that takes in a function and an\
 iterable as arguments and returns an iterator that applies the function to every\
 element in the iterable")
print('#' * 99)

print("for example we can use map to get a list containing the means (average) of\
 each list contained in a list, numbers:\n\
 numbers = [[23, 45, 67, 98, 67],[54, 12, 37, 98, 94],[900, 24, 546, 786, 909],[24, 8, 23, 33, 66]]")
print('#' * 99)

print("First we can define a function called mean to return the average given a\
 list of numbers. Then we can call the map method passing in the mean function\
 and the iterable (list named numbers). Finally, we pass the result of this to the\
 list function to form a list from the iterator returned by the map method as follows")

print("def mean(num_list):\n\treturn sum(num_list)/len(num_list)\n\naverage = list(map(mean, numbers))")
print('#' * 99)

print("The mean function described above can be reduced to a lambda expression that\
 is called directly by the map function like below")
print("average = list(map(lambda num_list: sum(num_list)/len(num_list)),numbers)")
numbers = [
    [23, 45, 67, 98, 67],
    [54, 12, 37, 98, 94],
    [900, 24, 546, 786, 909],
    [24, 8, 23, 33, 66]
]

def mean(num_list):
    return sum(num_list)/len(num_list)

average = list(map(mean, numbers))
average = list(map(lambda num_list: sum(num_list)/len(num_list),numbers))
print("list of averages is", average)

print('#' * 99)
print('#' * 99)

# lambda with filter

print("filter is a higher order built-in function that takes in a function and an\
 iterable as arguments and returns an iterator with the elements from the iterable\
 for which the function returns True")
print('#' * 99)

print("for example suppose we have a list of cities as follows:\n\
 cities = ['New York', 'Barcelona', 'Madrid', 'Amsterdam', 'Cape Town', 'New Delhi',\
 'Massachusetts', 'Dubai', 'Meru', 'Nairobi', 'Mombasa']\n and we want to find\
 cities with short names (i.e less than 8 characters) then we could define a method\
 to return a boolean of whether the length of the name of a city is less than 8.\
 Then using the filter built-in function, we could pass this function and the cities\
 list to get back an iterator which we pass to the list method to create a list-- short_cities")
print('#' * 99)

print("def is_short(name):\n\treturn len(name)<8")

print("\nshort_cities = list(filter(is_short, cities))\nprint(short_cities)")
print('#' * 99)
print('#' * 99)

print("We can define an anonymous function to replace the is_short function using\
 lambda expressions and use it in the call to the filter function as follows:\
\nshort_cities = list(filter(lambda name: len(name)<8), cities)")
def is_short(name):
    return len(name)<8

cities = ['New York', 'Barcelona', 'Madrid', 'Amsterdam', 'Cape Town', 'New Delhi',\
 'Massachusetts', 'Dubai', 'Meru', 'Nairobi', 'Mombasa']

short_cities = list(filter(is_short, cities))
short_cities = list(filter(lambda name: len(name)<8, cities))
print(short_cities)

print('#' * 99)
print(r'''
Lambda expressions syntax

lambda arg1,arg2: statement / expression to execute
''')