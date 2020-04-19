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