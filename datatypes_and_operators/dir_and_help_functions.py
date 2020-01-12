print("The dir() builtin fuction returns information about an object. It can be useful when you have an object and want to quickly find out what you can do with it. It returns some of the attributes of that object(Remember every object you encounter in Python has a type and this is what will influence the attributes returned)")
print('#' * 79)
num = 5
print("Say you have an integer like 5 assigned to the variable num, calling dir() on num will result in {}".format(dir(num)))
print('#' * 79)
print("The information printed is not very useful so we have another builtin function called help() which gives a short description of any of the attributes returned by dir(). You call help() on the attribute using the dot notation e.g help(num.__add__)")
print('#' * 79)
