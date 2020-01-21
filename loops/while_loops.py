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

print('#' * 79)
# Suppose you want to count from some number start_num by another number count_by until you hit a final number end_num. Use break_num as the variable that you'll change each time through the loop. For simplicity, assume that end_num is always larger than start_num and count_by is always positive.
start_num = 5 #provide some start number
end_num = 100 #provide some end number that you stop when you hit
count_by = 2 #provide some number to count by 

# write a while loop that uses break_num as the ongoing number to 
#   check against end_num
break_num = start_num
while break_num < end_num:
    print(break_num)
    break_num += count_by
print(break_num)

print('#' * 79)
# Suppose you want to count from some number start_num by another number count_by until you hit a final number end_num, and calculate break_num the way you did in the last quiz.

# Now in addition, address what would happen if someone gives a start_num that is greater than end_num. If this is the case, set result to "Oops! Looks like your start value is greater than the end value. Please try again." Otherwise, set result to the value of break_num.
start_num = 10 #provide some start number
end_num = 9 #provide some end number that you stop when you hit
count_by = 1 #provide some number to count by 

# write a condition to check that end_num is larger than start_num before looping
# write a while loop that uses break_num as the ongoing number to 
#   check against end_num
break_num = start_num
if end_num > start_num:
    result = break_num
else:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."
while break_num < end_num:
    print(break_num)
    break_num += count_by
print(result)