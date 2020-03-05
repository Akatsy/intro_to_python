print("The dir() built-in fuction returns information about an object. It can be useful when you have an object and want to quickly find out what you can do with it. It returns some of the attributes and methods of that object(Remember every object you encounter in Python has a type and this is what will determine the attributes and methods returned)")
print('#' * 79)
num = 5
print("Say you have an integer like 5 assigned to the variable num, calling dir() on num will result in the following attributes")
for index, attribute in enumerate(dir(num)):
    print(index, attribute)
print('#' * 79)
print("Calling dir() on a string like dir('s') would result in the following:")
for index, attrib in enumerate(dir('s')):
    print(index, attrib)
print('#' * 79)

print("The information printed is not very useful so we have another builtin function called help() which gives a short description of any of the attributes returned by dir(). You call help() on the attribute using the dot notation e.g help(num.__add__)")
print('#' * 79)
