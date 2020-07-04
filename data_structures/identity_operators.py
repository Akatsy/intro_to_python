# check if two objects are identical or not (i.e if they are the same object)
# using the identity operators
print("Python provides two identity operators:\n\t1.is \n\t2.is not")

print("is checks whether both sides of the operator have the same value")

print("is not checks whether both sides of the operator have different values")
print('#' * 79)

a = [1,2,3]
b = a
c = [1,2,3]

print("Given the following assignments a = [1,2,3] b = a and c = [1,2,3] using\
 the identity operators, we can check for identity as follows:")

print("a is b evaluates to {}\n b is a evaluates to {}\n a is c evaluates to {}\n\
 c is a evaluates to {}\n b is c evaluates to {}\n c is b evaluates to {}\n".format\
(a is b, b is a, a is c, c is a, b is c, c is b))
print('#' * 79)

print("a is not b evaluates to {}\n b is not a evaluates to {}\n a is not c evaluates\
 to {}\n c is not a evaluates to {}\n b is not c evaluates to {}\n c is not b evaluates\
 to {}\n".format(a is not b, b is not a, a is not c, c is not a, b is not c, c is not b))
print('#' * 79)

print("Identity and equality are not the same. Identity is checking if two variables\
 point to the same object while equality checks if two items are similar in the values\
 they contain")

print("Using the same example above, we can check for equality non-equality and\
 the results will be different as follows:")

print("a == b evaluates to {}\n b == a evaluates to {}\n a == c evaluates to {}\n\
 c == a evaluates to {}\n b == c evaluates to {}\n c == b evaluates to\
 {}\n".format(a == b, b == a, a == c, c == a, b == c, c == b))
print('#' * 79)

print("a != b evaluates to {}\n b != a evaluates to {}\n a != c evaluates to {}\n\
 c != a evaluates to {}\n b != c evaluates to {}\n c != b evaluates to\
 {}\n".format(a != b, b != a, a != c, c != a, b != c, c != b))
print("The values stored by the three objects (lists) a, b and c are equal but a\
 and b point to the same object while c points to a different object thus a and b\
 are identical but c is not of the same identity as a and b")