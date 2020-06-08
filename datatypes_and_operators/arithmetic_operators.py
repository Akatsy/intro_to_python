#Arithmetic operators - perform mathematical operations
print("The '+' symbol is the python arithmetic operator for addition as shown below:")
print("3 + 5 = ", 3+5)
print('#' * 79)
print("The '-' symbol is the python arithmetic operator for subtraction as shown below:")
print("100 - 56 = ", 100-56)
print('#' * 79)
print("The '*' (asterisk) symbol is the python arithmetic operator for multiplication as shown below:")
print("25 * 38 = ", 25*38)
print('#' * 79)
print("The '**' (double asterisk) is the python arithmetic operator for exponentiation (i.e raising one number to the power of another) as shown below:")
print("15 ** 8 = ", 15**8)
print('#' * 79)
print("The '/' (forward slash) symbol is the python arithmetic operator for division (float division) as shown below:")
print("Note that the result of the '/' operator is always a float even when the result is a whole number")
print("65 / 5 = ", 65/5)
print('#' * 79)
print("The '//' (double forward slash) is the python arithmetic operator for integer division as shown below:")
print("Integer division means the answer is rounded down to the nearest integer and this applies to even negative real numbers")
print("43 // 5 = ", 43//5)
print("-53 // 7 = ", -53//7)
print('#' * 79)
print("The '%' (percentage) symbol is the python arithmetic operator for modulo operation (i.e finds the remainder after division of one number by another (called the modulus of the operation)) as shown below:")
print("38 % 4 = ", 38%4)
print('#' * 79)
print("The mathematical order of operation holds in Python i.e given a mixture of arithmetic operations in the same equation, then they will be executed using the following order from first to last: PEMDAS (Parantheses, Exponentiation, Multiplication, Division, Addition, Subtraction)")
print("For example the equation: 3 + 5 - 5 * 6 ** 4 / 2 // 2 % 5 will evaluate to", 3 + 5 - 5 * 6 ** 4 / 2 // 2 % 5)
print('#' * 79)
print("To change the order of operation i.e to have an operation executed first, wrap parantheses around that operation. You can nest parantheses inside parantheses and execution begins in the innermost parantheses and once finished it goes to the next parantheses till execution is done")
print("For example altering the order of the equation from before will result in a different answer as follows: 3 + (5 - 5) * 6 ** 4 / 2 // 2 % 5 will evaluate to", 3 + (5 - 5) * 6 ** 4 / 2 // 2 % 5)

print(r'''
The most basic kind of instruction in Python is an expression.
An expression is made up of values and operators
Expressions have a characteristic that they can always reduce (evaluate down) to
a single value. Therefore you can use an expression anywhere in Python that you
could also use a single value.
A single value with no operator is also considered an expression although it just
evaluates to itself.
''')