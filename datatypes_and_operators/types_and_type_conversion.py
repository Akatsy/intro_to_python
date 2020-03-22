# convert data from one data type to another
print("The python data types; int, float, bool and str have constructor methods that can be used to convert one type to another")
print("The constructor methods are: {}, {}, {} and {}".format('int()', 'float()', 'str()', 'bool()'))
print('#' * 79)
print("int() converts a float to an integer by cutting off the decimal part (and not rounding off). Also converts a string data type that has a whole number as its value to an integer data type as shown below:")
num_float = 456.967
num_str = '912'
print("num_float = 456.967 and num_str = '912' when both are passed on to the int() function the results are: {} and {}".format(int(num_float), int(num_str)))
print('#' * 79)
print("float() converts an integer or a string with an integer as its value to a float by adding the decimal part (.0). Also converts a string data type that has a floating point number as it's value to its float data type equivalent as shown below:")
num_int = 234
num_str = '56'
num_str2 = '345.09'
print("num_int = 234, num_str = '56' and num_str2 = '345.09' when passed on to the float() function the results are: {}, {} and {}".format(float(num_int), float(num_str), float(num_str2)))
print('#' * 79)
print("str() method is used to convert any of the other data types into a string e.g:")
num_int = 49
num_float = 67.08
my_bool = True
print("num_int = 49, num_float = 67.08 and my_bool = True when passed on to the str() function the results are: {}, {} and {}. If you check their type they will be {}, {}, {}".format(str(num_int), str(num_float), str(my_bool), type(str(num_int)), type(str(num_float)), type(str(my_bool))))
print('#' * 79)
print("bool() converts any value of any data type passed to it to a boolean value:")
print("bool(10) is {}, bool(90.45) is {}, bool('345') is {}, bool('she') is {}, bool('') is {}".format(bool(10), bool(90.45), bool('345'), bool('she'), bool('')))