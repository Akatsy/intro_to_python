# Quiz: Population Density Function
# Write a function named population_density that takes two arguments, population and land_area, and returns a population density calculated from those values.

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
# Write a function named readable_timedelta. The function should take one argument, an integer days, and return a string that says how many weeks and days that is. For example, calling the function and printing the result like this:

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