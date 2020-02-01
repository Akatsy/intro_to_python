print("lambda expressions can be used to create anonymous functions i.e functions without a name")
print("They are helpful when we want to create quick functions that are not needed later in your code")
print("This can be especially useful in higher order functions (functions that take other functions as arguments)")
print('#' * 99)

print("A lambda expression has the following parts:")
print("1. the lambda keyword which signifies that this is a lambda expression")
print("2. Following the lambda keyword is one or more arguments separated by a comma and then a colon(:). This will be passed as inputs to the function. (Their naming is just arbitrary)")
print("3. Finally, after the colon is a statement that the function is to evaluate to get an output value, similar to what we would find in a return statement in a named function ")
print('#' * 99)
print("for example the following function\n {} can be converted to a lambda function as follows:\n {}".format("def cubed(num)\n\treturn num ** 3\n\n", "\ncubed = lambda num: num**3"))

def cubed(num):
    return num ** 3

cubed = lambda num: num**3
# print(cubed(9))