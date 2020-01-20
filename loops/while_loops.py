# problem sets

# Find the factorial of a number using a while loop.

number = 10 # number to find factorial of. change to any value
factorial = 1 # result of the factorial

while number >= 1:
    factorial *= number
    number -= 1
print(factorial)

# another solution
number = 35 # number to find factorial of. change to any value
current = 1 # number to keep track of number we working on
while current <= number:
    factorial *= current
    current += 1
print(factorial)