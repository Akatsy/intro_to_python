print("Variables store references (ids) to the computer memory locations where values assigned to them are stored")
a = 42
print("a = 42\nWhen you assign 42 to the variable a as above, you are actually creating the value 42 in the computer's memory then storing the reference (id) of that memory location in the variable a")

print('#' * 79)

print("Python has a builtin function id() that returns the id of any value in Python.\nid(a) will return {} which is the reference for the value".format(id(a)))

print('#' * 79)
b = a
print("What happens then when you assign the value in a to another variable b? like so b = a")
print("Python does not copy the value stored in a and store it to b. Rather, Python copies the reference value of value stored in a and stores it in b. So id(b) will be the same value as id(a) i.e id(b) == id(a) will result in {}".format(id(a) == id(b)))

print('#' * 79)
a = 100
print("If you later change the value in a like so a = 100, what you are doing is creating a new value 100 in memory with a completely different reference (id) and assigning that new id to the variable a. This does not then change the reference stored in b, so id(a) == id(b) will result in {} ".format(id(a) == id(b)))

print("Integers are immutable values that do not change")
print('#' * 79)
print("The behaviour for mutable values is a bit different")
a = [1,2,3,4]
b = a
a[1] = 5
print("Consider the following:\n a = [1,2,3,4] \n b = a \n a[1] = 5 \n print(a) \n print(b)")
print(a)
print(b)
print("Why does the change in a affect b??")
print("When we create the list, we assign its reference to the variable a. Then we assign a to b, in effect copying the reference for the list to variable b. Note that this means a and b thus refer to the same underlying list. So when you modify a, you are modifying the same list b refers to and hence the results above")

print('#' * 79)
print("All values in Python have a unique identity that can be obtained with the id() function e.g \nprint(id(print))\nprint(id(False))\nprint(id(1))\nwill output:")
print(id(print))
print(id(False))
print(id(1))

print("The id() function returns the numeric memory address where a value is stored")

print("Python picks this address based on which memory bytes happen to be free on your computer at the time so the value is different each time you run the code")

print('#' * 79)
print("For immutable data types, if you change the value stored in a variable, a new value is being created in memory and the reference to it being stored in the new variable and the old value's reference being forgotten, thus the old value has no variable referring to it.")
print("Python's automatic garbage collection deletes any values not being referred to by any variable to free up memory. Manual garbage collection in other PLs like C is a common source of bugs")