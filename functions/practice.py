# Quiz: Population Density Function
# Write a function named population_density that takes two arguments, population
# and land_area, and returns a population density calculated from those values.

# function
def population_density(population, land_area):
    return population/land_area

# test cases for function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))


print('#' * 99)

# Quiz: readable_timedelta
# Write a function named readable_timedelta. The function should take one argument,
# an integer days, and return a string that says how many weeks and days that is.
# For example, calling the function and printing the result like this:

# print(readable_timedelta(10))
# should output the following:

# 1 week(s) and 3 day(s).

def readable_timedelta(days):
    wks = days // 7
    num_days = days % 7
    return "{} week (s) and {} day (s).".format(wks, num_days)
print(readable_timedelta(15))
print(readable_timedelta(100))
print(readable_timedelta(366))
print(readable_timedelta(365))

print('#' * 99)

# The Collatz Sequence
# Write a function named collatz() that has one parameter named number. If number
# is even, then collatz() should print number // 2 and return this value. If 
# number is odd, then collatz() should print and return 3 * number + 1.

# Then write a program that lets the user type in an integer and that keeps
# calling collatz() on that number until the function returns the value 1. 
# (Amazingly enough, this sequence actually works for any integer—sooner or later,
# using this sequence, you’ll arrive at 1! Even mathematicians aren’t sure why.
# Your program is exploring what’s called the Collatz sequence, sometimes called
# “the simplest impossible math problem.”)

def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3*number + 1

import sys
while True:
    try:
        num = int(input("Enter any integer value: "))
        if num <= 0:
            print("Please input a positive value")
        else:
            print("The collatz sequence for {} is".format(num))
            while num != 1:
                num = collatz(num)
                print(num)
            sys.exit()
    except ValueError:
        print("Please input an integer value")


print('#' * 99)
# Comma Code
# Say you have a list value like this:

# spam = ['apples', 'bananas', 'tofu', 'cats']

# Write a function that takes a list value as an argument and returns a string
# with all the items separated by a comma and a space, with and inserted before
# the last item. For example, passing the previous spam list to the function 
# would return 'apples, bananas, tofu, and cats'. But your function should be
# able to work with any list value passed to it. Be sure to test the case where
# an empty list [] is passed to your function.

def comma_seperated_items(arr):
    return_str = ''
    for idx, item in enumerate(arr):
        if idx == len(arr)-1:
            return_str += 'and ' + item
        else:
            return_str += item + ', '
    return return_str

spam = ['apples', 'bananas', 'tofu', 'cats']
print(comma_seperated_items(spam))
print(comma_seperated_items([])) # comment out the collatz sequence code for this
# code to run coz of the sys.exit() statement